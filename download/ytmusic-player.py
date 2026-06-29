#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════╗
║      Terminal Music Player v3.0              ║
║  YouTube + SoundCloud  •  Chart Italia Top100║
╚══════════════════════════════════════════════╝

Requirements:
  sudo apt install pip
  pip install -U yt-dlp --break-system-packages
  pip install yt-dlp
  sudo apt install mpv       # Debian/Ubuntu
  sudo pacman -S mpv         # Arch
  sudo dnf install mpv       # Fedora

Usage:
  python3 ytmusic-player.py
  # oppure, se installato come comando:
  music
"""

import curses
import subprocess
import threading
import time
import json
import socket
import os
import sys
import urllib.request
import urllib.error
from dataclasses import dataclass, field
from typing import List, Optional, Dict
from queue import Queue, Empty


# ─────────────────────────────────────────────
#  DATA MODEL
# ─────────────────────────────────────────────

@dataclass
class Track:
    title:    str
    artist:   str
    duration: int          # seconds (0 = unknown)
    url:      str          # stream/page URL; empty = non ancora risolto
    video_id: str  = ""
    source:   str  = "youtube"   # "youtube" | "soundcloud"
    resolved: bool = True        # False = chart track, URL da cercare on-demand
    rank:     int  = 0           # posizione in classifica (0 = non da chart)

    def fmt_duration(self) -> str:
        if self.duration <= 0:
            return "--:--"
        m, s = divmod(self.duration, 60)
        return f"{m}:{s:02d}"

    def display(self) -> str:
        if self.artist:
            return f"{self.artist} – {self.title}"
        return self.title

    def source_icon(self) -> str:
        return "☁" if self.source == "soundcloud" else "🎬"


# ─────────────────────────────────────────────
#  MPV IPC CONTROLLER
# ─────────────────────────────────────────────

class MPVController:
    SOCKET = "/tmp/ytmusic-mpv.sock"

    def __init__(self):
        self.process = None
        self.sock: Optional[socket.socket] = None
        self._lock   = threading.Lock()
        self._req_id = 0
        self._running = False
        self._buf     = b""
        self._resp_qs: Dict[int, Queue] = {}
        self._props:   dict = {}
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

    def on_event(self, event: str, cb):
        self._event_cbs.setdefault(event, []).append(cb)

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

    def quit(self):
        self._running = False
        try:
            self.sock.close()
        except Exception:
            pass
        if self.process:
            self.process.terminate()


# ─────────────────────────────────────────────
#  ITALY CHARTS  (iTunes/Apple Music public API)
# ─────────────────────────────────────────────

class Charts:
    # Apple Music RSS – top 30 Italia, JSON pubblico, nessuna autenticazione
    URL = "https://itunes.apple.com/it/rss/topsongs/limit=100/json"

    @classmethod
    def fetch(cls) -> List[Track]:
        try:
            req = urllib.request.Request(cls.URL, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=10) as r:
                data = json.loads(r.read().decode())

            tracks: List[Track] = []
            entries = data.get("feed", {}).get("entry", [])
            for i, entry in enumerate(entries, 1):
                title  = entry.get("im:name",   {}).get("label", "Unknown")
                artist = entry.get("im:artist", {}).get("label", "")
                # im:duration è in millisecondi
                dur_ms = int(entry.get("im:duration", {}).get("label", 0) or 0)
                dur    = dur_ms // 1000
                tracks.append(Track(
                    title    = title,
                    artist   = artist,
                    duration = dur,
                    url      = "",        # verrà risolto on-demand
                    source   = "youtube",
                    resolved = False,
                    rank     = i,
                ))
            return tracks
        except Exception:
            return []


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
                if d.get("_type", "") in ("playlist", "channel"):
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
        except Exception as e:
            return [], str(e)

    @classmethod
    def search_youtube(cls, query: str, limit: int = 12) -> List[Track]:
        lines, _ = cls._run([f"ytsearch{limit}:{query}"])
        tracks = cls._parse_lines(lines, "youtube")
        if tracks:
            return tracks
        lines, _ = cls._run([f"ytmsearch{limit}:{query}"])
        tracks = cls._parse_lines(lines, "youtube")
        if tracks:
            return tracks
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

    @classmethod
    def resolve(cls, track: Track, source: str = "youtube") -> Optional[str]:
        """Cerca su YouTube/SC il brano da classifica e restituisce l'URL."""
        query = f"{track.artist} {track.title}"
        results = cls.search(query, source, limit=1)
        if results:
            return results[0].url
        return None


# ─────────────────────────────────────────────
#  MAIN APPLICATION
# ─────────────────────────────────────────────

class App:
    HEADER_H = 3
    SEARCH_H = 3
    NP_H     = 4
    CTRL_H   = 2

    def __init__(self, stdscr):
        self.scr = stdscr
        self.mpv = MPVController()
        self.mpv.start()
        self.mpv.on_event("end-file", self._on_end)

        # Search / chart state
        self.query      = ""
        self.results:   List[Track] = []
        self.searching  = False
        self.source     = "youtube"
        self.mode       = "chart"   # "chart" | "search"  (tipo di risultati visibili)

        # Chart state
        self.chart:     List[Track] = []
        self.chart_loading = True

        # Queue state
        self.queue:     List[Track] = []
        self.q_idx      = -1

        # UI state
        self.view       = "search"  # "search" | "queue"  (pannello attivo)
        self.typing     = False
        self.sel_r      = 0
        self.sel_q      = 0
        self.off_r      = 0
        self.off_q      = 0
        self.current: Optional[Track] = None
        self.status     = "Caricamento classifica Italia Top 30 …"
        self.status_ts  = time.time() + 9999

        # Curses
        curses.start_color()
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_CYAN,    -1)
        curses.init_pair(2, curses.COLOR_GREEN,   -1)
        curses.init_pair(3, curses.COLOR_YELLOW,  -1)
        curses.init_pair(4, curses.COLOR_WHITE,   -1)
        curses.init_pair(5, curses.COLOR_RED,     -1)
        curses.init_pair(6, curses.COLOR_BLACK,   curses.COLOR_CYAN)
        curses.init_pair(7, curses.COLOR_BLACK,   curses.COLOR_GREEN)
        curses.init_pair(8, curses.COLOR_MAGENTA, -1)
        curses.init_pair(9, curses.COLOR_BLACK,   curses.COLOR_YELLOW)

        curses.curs_set(0)
        self.scr.nodelay(True)
        self.scr.keypad(True)

        # Avvia subito il fetch della classifica in background
        threading.Thread(target=self._load_chart, daemon=True).start()

    # ── Charts ─────────────────────────────────

    def _load_chart(self):
        self.chart = Charts.fetch()
        self.chart_loading = False
        if self.chart:
            self._set_status(
                f"🏆 Classifica Apple Music Italia – Top {len(self.chart)} "
                f"· [C] ricarica · [Enter] riproduci · [A] in coda"
            )
            if self.mode == "chart":
                self.results = self.chart   # mostra subito
        else:
            self._set_status("✗ Classifica non disponibile – verifica la connessione")

    def _reload_chart(self):
        self.chart_loading = True
        self._set_status("Ricaricamento classifica …")
        threading.Thread(target=self._load_chart, daemon=True).start()

    # ── Events ─────────────────────────────────

    def _on_end(self, msg):
        if msg.get("reason") in ("eof", ""):
            threading.Thread(target=self._auto_next, daemon=True).start()

    def _auto_next(self):
        time.sleep(0.3)
        self._play_next()

    # ── Playback ───────────────────────────────

    def _start(self, track: Track):
        """Avvia la riproduzione; se la traccia è da classifica, risolve l'URL prima."""
        self.current = track
        if not track.resolved or not track.url:
            icon = "🏆" if track.rank else "⏳"
            self._set_status(f"{icon} Ricerca: {track.display()} …")
            def resolve_and_play():
                url = Searcher.resolve(track, self.source)
                if url:
                    track.url      = url
                    track.resolved = True
                    self.mpv.play(url)
                    self._set_status(f"▶ {track.display()}")
                else:
                    self._set_status(f"✗ Non trovato: {track.display()}")
            threading.Thread(target=resolve_and_play, daemon=True).start()
        else:
            src_icon = "☁" if track.source == "soundcloud" else "🎬"
            self._set_status(f"⏳ Loading {src_icon}: {track.display()}")
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
        import copy
        t = copy.copy(track)   # copia per non modificare la classifica originale
        self.queue.append(t)
        self._set_status(f"✚ In coda: {t.display()}")
        if self.q_idx == -1:
            self.q_idx = len(self.queue) - 1
            self._start(t)

    def _play_now(self, track: Track):
        import copy
        t = copy.copy(track)
        insert_at = self.q_idx + 1 if self.q_idx >= 0 else 0
        self.queue.insert(insert_at, t)
        self.q_idx = insert_at
        self._start(t)
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
            self._set_status(f"✕ Rimosso: {name}")

    # ── Search ─────────────────────────────────

    def _search(self):
        if not self.query.strip():
            return
        self.searching = True
        self.mode      = "search"
        self.results   = []
        self.sel_r = self.off_r = 0
        q   = self.query.strip()
        src = self.source
        self._set_status(f"🔍 Cerco su {SOURCE_LABELS[src]}: {q} …")

        def worker():
            self.results  = Searcher.search(q, src)
            self.searching = False
            n = len(self.results)
            if n:
                self._set_status(f"✓ {n} risultati da {SOURCE_LABELS[src]} per '{q}'")
            else:
                self._set_status("✗ Nessun risultato – prova: yt-dlp --update")

        threading.Thread(target=worker, daemon=True).start()

    def _show_chart(self):
        """Torna alla visualizzazione classifica."""
        self.mode    = "chart"
        self.results = self.chart
        self.sel_r   = 0
        self.off_r   = 0
        if self.chart:
            self._set_status(f"🏆 Classifica Apple Music Italia – Top {len(self.chart)}")
        elif self.chart_loading:
            self._set_status("Caricamento classifica …")
        else:
            self._set_status("Classifica non disponibile")

    def _toggle_source(self):
        idx = SOURCES.index(self.source)
        self.source = SOURCES[(idx + 1) % len(SOURCES)]
        self._set_status(f"Sorgente: {SOURCE_LABELS[self.source]}  (/ per cercare)")

    # ── Status ─────────────────────────────────

    def _set_status(self, msg: str, secs: float = 7):
        self.status    = msg
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
        self._w(y, 0,     "║", curses.color_pair(1))
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
        self._draw_header(y, w);              y += self.HEADER_H
        self._draw_search(y, w);              y += self.SEARCH_H
        self._draw_content(y, content_h, w);  y += content_h
        self._draw_nowplaying(y, w);          y += self.NP_H
        self._draw_controls(y, w)
        self.scr.refresh()

    def _draw_header(self, y, w):
        C = curses.color_pair(1)
        try:
            self.scr.addstr(y, 0, "╔" + "═" * (w - 2) + "╗", C)
        except curses.error:
            pass
        title = "  🎵  Terminal Music Player  –  YouTube · SoundCloud · Chart Italia"
        self._w(y + 1, 0, "║", C)
        self._w(y + 1, 1, title.ljust(w - 2), C | curses.A_BOLD)
        self._w(y + 1, w - 1, "║", C)
        self._hline(y + 2)

    def _draw_search(self, y, w):
        C  = curses.color_pair(1)
        C3 = curses.color_pair(3)
        C8 = curses.color_pair(8)
        C9 = curses.color_pair(9)

        # Badge sorgente + barra di ricerca
        src_label  = f" {SOURCE_LABELS[self.source]} "
        badge_attr = C9 if self.source == "soundcloud" else curses.color_pair(6)
        self._w(y, 0, "║", C)
        self._w(y, 1, src_label, badge_attr | curses.A_BOLD)
        x0 = 1 + len(src_label)

        prefix = " / "
        caret  = "█" if self.typing and int(time.time() * 2) % 2 == 0 else " "
        max_q  = w - x0 - len(prefix) - 4
        q_vis  = self.query[-max_q:] if len(self.query) > max_q else self.query
        line   = f"{prefix}{q_vis}{caret}"
        attr   = C8 | curses.A_BOLD if self.typing else C3
        self._w(y, x0, line.ljust(w - x0 - 1), attr)
        self._w(y, w - 1, "║", C)

        # Seconda riga: tab Results / Queue + indicatore chart
        self._hline(y + 1)
        chart_lbl = "🏆 Chart" if self.mode == "chart" else "   Chart"
        res_lbl   = (" ▶ Ricerca " if self.mode == "search" and self.view == "search"
                     else "   Ricerca ")
        res_lbl  += f"({len(self.results)})" if self.results and self.mode == "search" else ""
        q_lbl     = (" ▶ Coda   " if self.view == "queue" else "   Coda   ")
        q_lbl    += f"({len(self.queue)})" if self.queue else ""
        tabs      = f"  {chart_lbl}    {res_lbl}    {q_lbl}    [S] sorgente"
        self._w(y + 1, 1, tabs.ljust(w - 2), C | curses.A_BOLD)
        self._w(y + 1, w - 1, "║", C)

    def _draw_content(self, y, h, w):
        C     = curses.color_pair(1)
        inner = w - 2

        # Lista da mostrare
        if self.view == "queue":
            items  = self.queue
            sel    = self.sel_q
            offset = self.off_q
        else:
            items  = self.results
            sel    = self.sel_r
            offset = self.off_r

        # Messaggio vuoto
        if not items:
            if self.chart_loading and self.mode == "chart":
                msg = "  ⏳ Caricamento classifica Italia …"
            elif self.searching:
                msg = "  🔍 Ricerca in corso …"
            elif self.view == "queue":
                msg = "  Coda vuota · [A] aggiunge · [Enter] riproduce subito"
            elif self.mode == "chart":
                msg = "  Classifica non disponibile – verifica la connessione"
            else:
                msg = "  Premi / per cercare musica"

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

            track      = items[idx]
            is_sel     = idx == sel
            is_playing = (self.view == "queue" and idx == self.q_idx)

            dur = track.fmt_duration()

            # Numero / rank
            if track.rank:
                num = f"{track.rank:>3}."
            else:
                num = f"{idx + 1:>3}."

            # Icona
            if is_playing:
                icon = "▶ "
            elif track.rank and not track.resolved:
                icon = "🏆 "
            elif track.source == "soundcloud":
                icon = "☁ "
            else:
                icon = "  "

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
            elif track.rank and not track.resolved:
                attr = curses.color_pair(3)   # chart in giallo
            else:
                attr = curses.color_pair(4)

            self._w(ry, 1, line[:inner], attr)

    def _draw_nowplaying(self, y, w):
        C  = curses.color_pair(1)
        C2 = curses.color_pair(2)
        C3 = curses.color_pair(3)
        C4 = curses.color_pair(4)

        self._hline(y)
        inner = w - 2

        if self.current:
            pause_icon = "⏸" if self.mpv.paused() else "▶"
            if self.current.rank:
                src_icon = f"🏆{self.current.rank}"
            elif self.current.source == "soundcloud":
                src_icon = "☁"
            else:
                src_icon = "🎬"
            vol   = self.mpv.volume()
            qi    = f"[{self.q_idx + 1}/{len(self.queue)}]"
            right = f" Vol:{vol:3d}%  {qi} "
            name  = f" {pause_icon} {src_icon}  {self.current.display()}"
            nl    = inner - len(right)
            if len(name) > nl:
                name = name[:nl - 1] + "…"
            self._border_col(y + 1)
            self._w(y + 1, 1, name.ljust(nl) + right, C2 | curses.A_BOLD)

            pos    = self.mpv.position()
            dur    = self.mpv.total()
            pos_s  = self._fmt_t(pos)
            dur_s  = self._fmt_t(dur)
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
            self._w(y + 1, 1, "  Nessuna traccia in riproduzione".ljust(inner), C4)
            self._border_col(y + 2)
            self._w(y + 2, 1, ("░" * inner)[:inner], C)

        self._border_col(y + 3)
        status = self.status if time.time() < self.status_ts else ""
        self._w(y + 3, 1, status[:inner].ljust(inner), C3)

    def _draw_controls(self, y, w):
        C = curses.color_pair(1)
        self._hline(y)
        ctrl = ("  [/] Cerca  [C] Chart  [S] Sorgente  [Space] Play/Pause  "
                "[N] Succ  [P] Prec  [A] Coda  [Enter] Riproduci  "
                "[Del] Rimuovi  [←][→] ±10s  [<][>] ±30s  [+][-] Vol  [Tab] Vista  [Q] Esci")
        self._border_col(y + 1)
        self._w(y + 1, 1, ctrl[:w - 2].ljust(w - 2), C)

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
        if k == 27:
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
            self.view   = "search"

        elif k in (ord('c'), ord('C')):
            if self.view == "search":
                self._show_chart()
            else:
                self._reload_chart()

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
            subprocess.run([cmd, "--version"], capture_output=True, check=True)
        except (FileNotFoundError, subprocess.CalledProcessError):
            missing.append(cmd)
    return missing


def main():
    missing = check_deps()
    if missing:
        print("╔═══════════════════════════════════════╗")
        print("║   Terminal Player – dipendenze mancanti║")
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