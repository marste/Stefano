#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════╗
║      Terminal Music Player v2.0              ║
║  YouTube Music + SoundCloud via yt-dlp + mpv ║
╚══════════════════════════════════════════════╝

Requirements:
  pip install yt-dlp
  sudo apt install mpv       # Debian/Ubuntu
  sudo pacman -S mpv         # Arch
  sudo dnf install mpv       # Fedora

Usage:
  python3 ytmusic-player.py
"""

import curses
import subprocess
import threading
import time
import json
import socket
import os
import sys
from dataclasses import dataclass
from typing import List, Optional, Dict
from queue import Queue, Empty


# ─────────────────────────────────────────────
#  DATA MODEL
# ─────────────────────────────────────────────

@dataclass
class Track:
    title: str
    artist: str
    duration: int        # seconds
    url: str
    video_id: str = ""
    source: str = "youtube"   # "youtube" | "soundcloud"

    def fmt_duration(self) -> str:
        m, s = divmod(max(0, self.duration), 60)
        return f"{m}:{s:02d}"

    def display(self) -> str:
        if self.artist:
            return f"{self.artist} – {self.title}"
        return self.title

    def source_icon(self) -> str:
        return "☁" if self.source == "soundcloud" else "▶"


# ─────────────────────────────────────────────
#  MPV IPC CONTROLLER
# ─────────────────────────────────────────────

class MPVController:
    SOCKET = "/tmp/ytmusic-mpv.sock"

    def __init__(self):
        self.process = None
        self.sock: Optional[socket.socket] = None
        self._lock = threading.Lock()
        self._req_id = 0
        self._running = False
        self._buf = b""
        self._resp_qs: Dict[int, Queue] = {}
        self._props: dict = {}
        self._event_cbs: Dict[str, list] = {}

    def start(self):
        if os.path.exists(self.SOCKET):
            os.remove(self.SOCKET)

        self.process = subprocess.Popen(
            ["mpv", "--no-video", f"--input-ipc-server={self.SOCKET}",
             "--idle=yes", "--really-quiet", "--no-terminal"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
        )
        for _ in range(80):
            if os.path.exists(self.SOCKET):
                break
            time.sleep(0.05)

        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.connect(self.SOCKET)
        self._running = True
        threading.Thread(target=self._listen, daemon=True).start()

        for prop in ("time-pos", "duration", "pause", "volume", "eof-reached"):
            self._observe(prop)

    # ── Low-level IPC ──────────────────────────

    def _send(self, cmd: dict) -> int:
        with self._lock:
            self._req_id += 1
            rid = self._req_id
            cmd["request_id"] = rid
            self._resp_qs[rid] = Queue()
            try:
                self.sock.send(json.dumps(cmd).encode() + b"\n")
            except Exception:
                pass
            return rid

    def _send_wait(self, cmd: dict, timeout=3.0):
        rid = self._send(cmd)
        try:
            return self._resp_qs[rid].get(timeout=timeout)
        except Empty:
            return None
        finally:
            self._resp_qs.pop(rid, None)

    def _listen(self):
        while self._running:
            try:
                data = self.sock.recv(4096)
                if not data:
                    break
                self._buf += data
                while b"\n" in self._buf:
                    line, self._buf = self._buf.split(b"\n", 1)
                    if line.strip():
                        self._handle(json.loads(line))
            except Exception:
                time.sleep(0.05)

    def _handle(self, msg: dict):
        rid = msg.get("request_id")
        if rid and rid in self._resp_qs:
            self._resp_qs[rid].put(msg)

        event = msg.get("event")
        if event == "property-change":
            self._props[msg.get("name")] = msg.get("data")
            for cb in self._event_cbs.get(f"prop:{msg.get('name')}", []):
                cb(msg.get("data"))
        elif event:
            for cb in self._event_cbs.get(event, []):
                cb(msg)

    def _observe(self, name: str):
        with self._lock:
            self._req_id += 1
            rid = self._req_id
        cmd = {"command": ["observe_property", rid, name], "request_id": rid}
        self._resp_qs[rid] = Queue()
        try:
            self.sock.send(json.dumps(cmd).encode() + b"\n")
        except Exception:
            pass
        self._resp_qs.pop(rid, None)

    # ── Public API ─────────────────────────────

    def on_event(self, event: str, cb):
        self._event_cbs.setdefault(event, []).append(cb)

    def on_prop(self, name: str, cb):
        self._event_cbs.setdefault(f"prop:{name}", []).append(cb)

    def play(self, url: str):
        self._send({"command": ["loadfile", url, "replace"]})

    def toggle_pause(self):
        self._send({"command": ["cycle", "pause"]})

    def stop(self):
        self._send({"command": ["stop"]})

    def seek(self, secs: float):
        self._send({"command": ["seek", secs, "relative"]})

    def volume(self) -> int:
        return int(self._props.get("volume") or 100)

    def set_volume(self, v: int):
        self._send({"command": ["set_property", "volume", max(0, min(150, v))]})

    def position(self) -> float:
        return float(self._props.get("time-pos") or 0)

    def total(self) -> float:
        return float(self._props.get("duration") or 0)

    def paused(self) -> bool:
        return bool(self._props.get("pause", False))

    def eof(self) -> bool:
        return bool(self._props.get("eof-reached", False))

    def quit(self):
        self._running = False
        try:
            self.sock.close()
        except Exception:
            pass
        if self.process:
            self.process.terminate()


# ─────────────────────────────────────────────
#  MULTI-SOURCE SEARCH  (YouTube + SoundCloud)
# ─────────────────────────────────────────────

SOURCES       = ["youtube", "soundcloud"]
SOURCE_LABELS = {"youtube": "🎬 YouTube", "soundcloud": "☁  SoundCloud"}

class Searcher:
    @staticmethod
    def _parse_lines(lines: list, source: str = "youtube") -> List[Track]:
        tracks: List[Track] = []
        for line in lines:
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
                kind = d.get("_type", "")
                if kind in ("playlist", "channel"):
                    continue

                raw_title = d.get("title") or "Unknown"
                uploader  = d.get("uploader") or d.get("channel") or ""
                artist    = uploader.replace(" - Topic", "").strip()
                title     = raw_title

                if " - " in raw_title and not artist:
                    parts  = raw_title.split(" - ", 1)
                    artist = parts[0].strip()
                    title  = parts[1].strip()

                vid     = d.get("id") or ""
                webpage = d.get("webpage_url") or d.get("url") or ""
                if not vid and not webpage:
                    continue

                if source == "soundcloud":
                    url = webpage if webpage else f"https://soundcloud.com/{vid}"
                else:
                    url = f"https://www.youtube.com/watch?v={vid}" if vid else webpage

                dur = int(d.get("duration") or 0)
                tracks.append(Track(title=title, artist=artist,
                                    duration=dur, url=url,
                                    video_id=vid, source=source))
            except Exception:
                continue
        return tracks

    @staticmethod
    def _run(args: list, timeout: int = 30):
        try:
            r = subprocess.run(
                ["yt-dlp", "--no-warnings", "--no-playlist",
                 "-j", "--flat-playlist"] + args,
                capture_output=True, text=True, timeout=timeout
            )
            return r.stdout.strip().splitlines(), r.stderr.strip()
        except subprocess.TimeoutExpired:
            return [], "timeout"
        except FileNotFoundError:
            return [], "yt-dlp not found"
        except Exception as e:
            return [], str(e)

    @classmethod
    def search_youtube(cls, query: str, limit: int = 12) -> List[Track]:
        # Strategy 1: ytsearch (most reliable)
        lines, _ = cls._run([f"ytsearch{limit}:{query}"])
        tracks = cls._parse_lines(lines, "youtube")
        if tracks:
            return tracks
        # Strategy 2: ytmsearch (YouTube Music specific)
        lines, _ = cls._run([f"ytmsearch{limit}:{query}"])
        tracks = cls._parse_lines(lines, "youtube")
        if tracks:
            return tracks
        # Strategy 3: URL-based fallback
        url = "https://www.youtube.com/results?search_query=" + query.replace(" ", "+")
        lines, _ = cls._run([url])
        return cls._parse_lines(lines, "youtube")

    @classmethod
    def search_soundcloud(cls, query: str, limit: int = 12) -> List[Track]:
        lines, _ = cls._run([f"scsearch{limit}:{query}"])
        return cls._parse_lines(lines, "soundcloud")

    @classmethod
    def search(cls, query: str, source: str = "youtube", limit: int = 12) -> List[Track]:
        if source == "soundcloud":
            return cls.search_soundcloud(query, limit)
        return cls.search_youtube(query, limit)


# ─────────────────────────────────────────────
#  MAIN APPLICATION
# ─────────────────────────────────────────────

class App:
    HEADER_H   = 3
    SEARCH_H   = 3   # search bar + source/tab row
    NP_H       = 4   # now-playing panel
    CTRL_H     = 2   # controls bar

    def __init__(self, stdscr):
        self.scr = stdscr
        self.mpv = MPVController()
        self.mpv.start()
        self.mpv.on_event("end-file", self._on_end)

        # Search state
        self.query        = ""
        self.results:  List[Track] = []
        self.searching    = False
        self.source       = "youtube"   # "youtube" | "soundcloud"

        # Queue state
        self.queue:    List[Track] = []
        self.q_idx        = -1

        # UI state
        self.view         = "search"   # "search" | "queue"
        self.typing       = False
        self.sel_r        = 0
        self.sel_q        = 0
        self.off_r        = 0
        self.off_q        = 0
        self.current: Optional[Track] = None
        self.status       = "Press / to search · S switches source · Tab switches view · Q quits"
        self.status_ts    = time.time() + 9999

        # Curses setup
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_CYAN,    -1)   # frame
        curses.init_pair(2, curses.COLOR_GREEN,   -1)   # playing
        curses.init_pair(3, curses.COLOR_YELLOW,  -1)   # accent
        curses.init_pair(4, curses.COLOR_WHITE,   -1)   # normal
        curses.init_pair(5, curses.COLOR_RED,     -1)   # error
        curses.init_pair(6, curses.COLOR_BLACK,   curses.COLOR_CYAN)    # selected
        curses.init_pair(7, curses.COLOR_BLACK,   curses.COLOR_GREEN)   # playing+sel
        curses.init_pair(8, curses.COLOR_MAGENTA, -1)   # typing
        curses.init_pair(9, curses.COLOR_BLACK,   curses.COLOR_YELLOW)  # SC source

        curses.curs_set(0)
        self.scr.nodelay(True)
        self.scr.keypad(True)

    # ── Event handlers ─────────────────────────

    def _on_end(self, msg):
        if msg.get("reason") in ("eof", ""):
            threading.Thread(target=self._auto_next, daemon=True).start()

    def _auto_next(self):
        time.sleep(0.3)
        self._play_next()

    # ── Playback ───────────────────────────────

    def _start(self, track: Track):
        self.current = track
        icon = "☁" if track.source == "soundcloud" else "🎬"
        self._set_status(f"⏳ Loading {icon}: {track.display()}")
        self.mpv.play(track.url)

    def _play_next(self):
        if self.q_idx < len(self.queue) - 1:
            self.q_idx += 1
            self._start(self.queue[self.q_idx])

    def _play_prev(self):
        if self.mpv.position() > 3:
            self.mpv.seek(-self.mpv.position())
        elif self.q_idx > 0:
            self.q_idx -= 1
            self._start(self.queue[self.q_idx])

    def _enqueue(self, track: Track):
        self.queue.append(track)
        self._set_status(f"✚ Queued: {track.display()}")
        if self.q_idx == -1:
            self.q_idx = len(self.queue) - 1
            self._start(track)

    def _play_now(self, track: Track):
        insert_at = self.q_idx + 1 if self.q_idx >= 0 else 0
        self.queue.insert(insert_at, track)
        self.q_idx = insert_at
        self._start(track)
        self.view = "queue"

    def _remove_from_queue(self, idx: int):
        if 0 <= idx < len(self.queue):
            name = self.queue[idx].display()
            self.queue.pop(idx)
            if idx < self.q_idx:
                self.q_idx -= 1
            elif idx == self.q_idx:
                if self.q_idx >= len(self.queue):
                    self.q_idx = len(self.queue) - 1
                if self.q_idx >= 0:
                    self._start(self.queue[self.q_idx])
                else:
                    self.current = None
                    self.mpv.stop()
            self.sel_q = min(self.sel_q, max(0, len(self.queue) - 1))
            self._set_status(f"✕ Removed: {name}")

    # ── Search ─────────────────────────────────

    def _search(self):
        if not self.query.strip():
            return
        self.searching = True
        self.results = []
        self.sel_r = self.off_r = 0
        q = self.query.strip()
        src = self.source
        label = SOURCE_LABELS[src]
        self._set_status(f"🔍 Searching {label}: {q} …")

        def worker():
            self.results = Searcher.search(q, src)
            self.searching = False
            n = len(self.results)
            if n:
                self._set_status(f"✓ {n} risultati da {label} per '{q}'")
            else:
                self._set_status(
                    f"✗ Nessun risultato su {label} – prova: yt-dlp --update"
                )

        threading.Thread(target=worker, daemon=True).start()

    def _toggle_source(self):
        idx = SOURCES.index(self.source)
        self.source = SOURCES[(idx + 1) % len(SOURCES)]
        self.results = []
        self.sel_r = self.off_r = 0
        self._set_status(f"Sorgente: {SOURCE_LABELS[self.source]}  (/ per cercare)")

    # ── Status ─────────────────────────────────

    def _set_status(self, msg: str, secs: float = 6):
        self.status = msg
        self.status_ts = time.time() + secs

    # ── Drawing ────────────────────────────────

    def _w(self, y, x, text, attr=0):
        h, w = self.scr.getmaxyx()
        if y < 0 or y >= h or x < 0 or x >= w:
            return
        avail = w - x - 1
        if avail <= 0:
            return
        try:
            self.scr.addstr(y, x, text[:avail], attr)
        except curses.error:
            pass

    def _hline(self, y, left="╠", mid="═", right="╣"):
        _, w = self.scr.getmaxyx()
        try:
            self.scr.addstr(y, 0, left + mid * (w - 2) + right,
                            curses.color_pair(1))
        except curses.error:
            pass

    def _border_col(self, y):
        _, w = self.scr.getmaxyx()
        self._w(y, 0, "║", curses.color_pair(1))
        self._w(y, w - 1, "║", curses.color_pair(1))

    def draw(self):
        self.scr.erase()
        h, w = self.scr.getmaxyx()
        if h < 16 or w < 52:
            self._w(0, 0, "Terminal too small – resize to ≥52×16")
            self.scr.refresh()
            return

        content_h = h - self.HEADER_H - self.SEARCH_H - self.NP_H - self.CTRL_H
        y = 0
        self._draw_header(y, w);            y += self.HEADER_H
        self._draw_search(y, w);            y += self.SEARCH_H
        self._draw_content(y, content_h, w); y += content_h
        self._draw_nowplaying(y, w);        y += self.NP_H
        self._draw_controls(y, w)
        self.scr.refresh()

    def _draw_header(self, y, w):
        C = curses.color_pair(1)
        try:
            self.scr.addstr(y, 0, "╔" + "═" * (w - 2) + "╗", C)
        except curses.error:
            pass
        title = "  🎵  Terminal Music Player  –  YouTube + SoundCloud"
        self._w(y + 1, 0, "║", C)
        self._w(y + 1, 1, title.ljust(w - 2), C | curses.A_BOLD)
        self._w(y + 1, w - 1, "║", C)
        self._hline(y + 2)

    def _draw_search(self, y, w):
        C  = curses.color_pair(1)
        C3 = curses.color_pair(3)
        C8 = curses.color_pair(8)
        C9 = curses.color_pair(9)   # SoundCloud badge

        # Source badge + search bar
        src_label = f" {SOURCE_LABELS[self.source]} "
        badge_attr = C9 if self.source == "soundcloud" else (curses.color_pair(6))
        self._w(y, 0, "║", C)
        self._w(y, 1, src_label, badge_attr | curses.A_BOLD)
        x_after_badge = 1 + len(src_label)

        prefix = " / "
        caret = "█" if self.typing and int(time.time() * 2) % 2 == 0 else " "
        max_q = w - x_after_badge - len(prefix) - 4
        q_vis = self.query[-max_q:] if len(self.query) > max_q else self.query
        line = f"{prefix}{q_vis}{caret}"
        attr = C8 | curses.A_BOLD if self.typing else C3
        self._w(y, x_after_badge, line.ljust(w - x_after_badge - 1), attr)
        self._w(y, w - 1, "║", C)

        # Tab bar
        self._hline(y + 1)
        tab_s = (" ▶ Results " if self.view == "search" else "   Results ") + \
                (f"({len(self.results)})" if self.results else "")
        tab_q = (" ▶ Queue   " if self.view == "queue"  else "   Queue   ") + \
                (f"({len(self.queue)})" if self.queue else "")
        tabs = f"  {tab_s}    {tab_q}    [S] switch source"
        self._w(y + 1, 1, tabs.ljust(w - 2), C | curses.A_BOLD)
        self._w(y + 1, w - 1, "║", C)

    def _draw_content(self, y, h, w):
        C     = curses.color_pair(1)
        inner = w - 2

        items  = self.results if self.view == "search" else self.queue
        sel    = self.sel_r   if self.view == "search" else self.sel_q
        offset = self.off_r   if self.view == "search" else self.off_q

        if not items:
            if self.searching:
                msg = "  Searching …"
            elif self.view == "search":
                msg = "  Press / to search, then Enter"
            else:
                msg = "  Queue is empty · Add songs with [A] or [Enter]"

        for row in range(h):
            ry = y + row
            self._w(ry, 0,     "║", C)
            self._w(ry, w - 1, "║", C)

            idx = row + offset
            if not items:
                if row == h // 2:
                    self._w(ry, 1, msg.ljust(inner), curses.color_pair(3))
                continue

            if idx >= len(items):
                continue

            track = items[idx]
            is_sel     = idx == sel
            is_playing = (self.view == "queue" and idx == self.q_idx)

            dur  = track.fmt_duration()
            num  = f"{idx + 1:>3}."
            icon = ("▶ " if is_playing else "☁ ") if track.source == "soundcloud" \
                   else ("▶ " if is_playing else "  ")
            name  = track.display()
            avail = inner - len(num) - len(icon) - len(dur) - 1
            if len(name) > avail:
                name = name[:avail - 1] + "…"
            line = num + icon + name.ljust(avail) + dur

            if is_playing and is_sel:
                attr = curses.color_pair(7) | curses.A_BOLD
            elif is_sel:
                attr = curses.color_pair(6) | curses.A_BOLD
            elif is_playing:
                attr = curses.color_pair(2) | curses.A_BOLD
            else:
                attr = curses.color_pair(4)

            self._w(ry, 1, line[:inner], attr)

    def _draw_nowplaying(self, y, w):
        C  = curses.color_pair(1)
        C2 = curses.color_pair(2)
        C3 = curses.color_pair(3)
        C4 = curses.color_pair(4)

        self._hline(y, "╠", "═", "╣")
        inner = w - 2

        if self.current:
            pause_icon = "⏸" if self.mpv.paused() else "▶"
            src_icon   = "☁" if self.current.source == "soundcloud" else "🎬"
            vol   = self.mpv.volume()
            qi    = f"[{self.q_idx + 1}/{len(self.queue)}]"
            right = f" Vol:{vol:3d}%  {qi} "
            name  = f" {pause_icon} {src_icon}  {self.current.display()}"
            nl    = inner - len(right)
            if len(name) > nl:
                name = name[:nl - 1] + "…"
            self._border_col(y + 1)
            self._w(y + 1, 1, name.ljust(nl) + right, C2 | curses.A_BOLD)

            pos   = self.mpv.position()
            dur   = self.mpv.total()
            pos_s = self._fmt_t(pos)
            dur_s = self._fmt_t(dur)
            time_s = f" {pos_s}/{dur_s} "
            bar_w  = inner - len(time_s)
            if bar_w > 4 and dur > 0:
                filled = int(pos / dur * bar_w)
                bar = "█" * filled + "░" * (bar_w - filled)
            else:
                bar = "░" * max(0, bar_w)
            self._border_col(y + 2)
            self._w(y + 2, 1, bar[:bar_w], C3)
            self._w(y + 2, 1 + bar_w, time_s, C4)
        else:
            self._border_col(y + 1)
            self._w(y + 1, 1, "  No track playing".ljust(inner), C4)
            self._border_col(y + 2)
            self._w(y + 2, 1, ("░" * inner)[:inner], C)

        self._border_col(y + 3)
        status = self.status if time.time() < self.status_ts else ""
        self._w(y + 3, 1, status[:inner].ljust(inner), C3)

    def _draw_controls(self, y, w):
        C = curses.color_pair(1)
        self._hline(y, "╠", "═", "╣")
        controls = ("  [/] Search  [S] Source  [Space] Play/Pause  [N] Next  [P] Prev  "
                    "[A] Queue  [Enter] Play Now  [Del] Remove  "
                    "[←][→] ±10s  [<][>] ±30s  [+][-] Vol  [Tab] Switch  [Q] Quit")
        self._border_col(y + 1)
        self._w(y + 1, 1, controls[:w - 2].ljust(w - 2), C)

    def _fmt_t(self, secs: float) -> str:
        if secs <= 0:
            return "0:00"
        s = int(secs)
        m, s = divmod(s, 60)
        return f"{m}:{s:02d}"

    # ── Input ──────────────────────────────────

    def handle_key(self) -> bool:
        try:
            k = self.scr.getch()
        except Exception:
            return True

        if k == -1:
            return True

        if self.typing:
            return self._key_typing(k)
        return self._key_normal(k)

    def _key_typing(self, k) -> bool:
        if k == 27:   # Esc
            self.typing = False
        elif k in (10, 13):
            self.typing = False
            self._search()
        elif k in (curses.KEY_BACKSPACE, 127, 8):
            self.query = self.query[:-1]
        elif 32 <= k <= 126:
            self.query += chr(k)
        return True

    def _key_normal(self, k) -> bool:
        h, w = self.scr.getmaxyx()
        vis = h - self.HEADER_H - self.SEARCH_H - self.NP_H - self.CTRL_H

        if k in (ord('q'), ord('Q')):
            return False

        elif k == ord('/'):
            self.typing = True
            self.view = "search"

        elif k in (ord('s'), ord('S')):
            self._toggle_source()

        elif k == ord('\t'):
            self.view = "queue" if self.view == "search" else "search"

        elif k == ord(' '):
            if self.current:
                self.mpv.toggle_pause()

        elif k in (ord('n'), ord('N')):
            self._play_next()
        elif k in (ord('p'), ord('P')):
            self._play_prev()

        elif k in (ord('+'), ord('=')):
            self.mpv.set_volume(self.mpv.volume() + 5)
        elif k == ord('-'):
            self.mpv.set_volume(self.mpv.volume() - 5)

        # Seek: arrows = ±10s, < > = ±30s
        elif k == curses.KEY_LEFT:
            self.mpv.seek(-10)
        elif k == curses.KEY_RIGHT:
            self.mpv.seek(10)
        elif k == ord('<'):
            self.mpv.seek(-30)
        elif k == ord('>'):
            self.mpv.seek(30)

        elif k == curses.KEY_UP:
            if self.view == "search":
                self.sel_r = max(0, self.sel_r - 1)
                if self.sel_r < self.off_r:
                    self.off_r = self.sel_r
            else:
                self.sel_q = max(0, self.sel_q - 1)
                if self.sel_q < self.off_q:
                    self.off_q = self.sel_q

        elif k == curses.KEY_DOWN:
            if self.view == "search":
                self.sel_r = min(len(self.results) - 1, self.sel_r + 1)
                if self.sel_r >= self.off_r + vis:
                    self.off_r = self.sel_r - vis + 1
            else:
                self.sel_q = min(len(self.queue) - 1, self.sel_q + 1)
                if self.sel_q >= self.off_q + vis:
                    self.off_q = self.sel_q - vis + 1

        elif k == curses.KEY_PPAGE:
            if self.view == "search":
                self.sel_r = max(0, self.sel_r - vis)
                self.off_r = max(0, self.off_r - vis)
            else:
                self.sel_q = max(0, self.sel_q - vis)
                self.off_q = max(0, self.off_q - vis)

        elif k == curses.KEY_NPAGE:
            if self.view == "search":
                self.sel_r = min(len(self.results) - 1, self.sel_r + vis)
                if self.sel_r >= self.off_r + vis:
                    self.off_r = self.sel_r - vis + 1
            else:
                self.sel_q = min(len(self.queue) - 1, self.sel_q + vis)
                if self.sel_q >= self.off_q + vis:
                    self.off_q = self.sel_q - vis + 1

        elif k in (10, 13):
            if self.view == "search" and self.results:
                self._play_now(self.results[self.sel_r])
            elif self.view == "queue" and self.queue:
                self.q_idx = self.sel_q
                self._start(self.queue[self.q_idx])

        elif k in (ord('a'), ord('A')):
            if self.view == "search" and self.results:
                self._enqueue(self.results[self.sel_r])

        elif k in (curses.KEY_DC, ord('d'), ord('D')):
            if self.view == "queue" and self.queue:
                self._remove_from_queue(self.sel_q)

        return True

    # ── Main loop ──────────────────────────────

    def run(self):
        try:
            while True:
                self.draw()
                if not self.handle_key():
                    break
                time.sleep(0.05)
        finally:
            self.mpv.quit()


# ─────────────────────────────────────────────
#  DEPENDENCY CHECK + ENTRY POINT
# ─────────────────────────────────────────────

def check_deps():
    missing = []
    for cmd in ("yt-dlp", "mpv"):
        try:
            subprocess.run([cmd, "--version"],
                           capture_output=True, check=True)
        except (FileNotFoundError, subprocess.CalledProcessError):
            missing.append(cmd)
    return missing


def main():
    missing = check_deps()
    if missing:
        print("╔═══════════════════════════════════════╗")
        print("║   Terminal Player – Missing deps       ║")
        print("╠═══════════════════════════════════════╣")
        for dep in missing:
            if dep == "yt-dlp":
                print("║  • yt-dlp:  pip install yt-dlp         ║")
            else:
                print("║  • mpv:     sudo apt install mpv        ║")
        print("╚═══════════════════════════════════════╝")
        sys.exit(1)

    curses.wrapper(lambda scr: App(scr).run())


if __name__ == "__main__":
    main()
