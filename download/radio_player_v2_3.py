#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║            🎵  Terminal Radio Player  v2.3                   ║
║         Debian 13 · mpv · Python curses · Fire Theme        ║
╚══════════════════════════════════════════════════════════════╝

Dipendenze:
  sudo apt install mpv python3 alsa-utils

Per aggiungere/togliere stazioni modifica la lista STATIONS qui sotto,
poi premi R nell'app per ricaricarle senza riavviare.
"""

import curses
import subprocess
import os
import sys
import signal
import time
import math
import random
import threading

# ╔══════════════════════════════════════════════════════════════════════════════╗
# ║  STAZIONI — aggiungi, togli o riordina liberamente                          ║
# ║  Ogni voce: {"name": "Nome", "url": "https://..."}                          ║
# ╚══════════════════════════════════════════════════════════════════════════════╝
STATIONS = [
    {"name": "M2O",                  "url": "https://4c4b867c89244861ac216426883d1ad0.msvdn.net/radiom2o/radiom2o/play1.m3u8"},
    {"name": "Hardcore Power Radio", "url": "https://hardcorepower.beheerstream.nl:8012/stream"},
    {"name": "90s 90s Techno",       "url": "https://regiocast.streamabc.net/regc-90s90stechno2195701-mp3-192-2408420"},
    {"name": "Techno Revival",       "url": "https://techno-revival.stream.laut.fm/techno-revival?ref=web-app&start_time=1759669832984"},
    {"name": "Toxic Sickness Radio", "url": "https://s7.citrus3.com:8152/stream"},
    {"name": "Radio Deejay",         "url": "https://4c4b867c89244861ac216426883d1ad0.msvdn.net/radiodeejaybck/radiodeejaybck/play1.m3u8"},
    {"name": "Deejay Time",          "url": "https://vdnvsxa1-4c4b867c89244861ac216426883d1ad0.msvdn.net/webradio/deejaytime/live.m3u8"},
    {"name": "30 Songs - Deejay",    "url": "https://4c4b867c89244861ac216426883d1ad0.msvdn.net/radiodeejay30songs/radiodeejay30songs/play1.m3u8"},
    {"name": "538 Dance Department", "url": "https://22713.live.streamtheworld.com/TLPSTR01.mp3?dist=538_web"},
    {"name": "ON Club",              "url": "https://n32a-eu.rcs.revma.com/prbak410t13vv?rj-ttl=5&rj-tok=AAABm7aZVdkAXZEe-G3o3PLkeQ"},
    {"name": "Disco Radio",          "url": "https://stream.discoradio.radio/audio/disco.stream_aac64/chunklist.m3u8"},
    {"name": "80s 80s",              "url": "https://regiocast.streamabc.net/regc-80s80smweb2517500-mp3-192-1672667"},
    {"name": "Deep House FM",        "url": "https://altair.streamerr.co:8124/stream"},
    {"name": "Venus Radio",          "url": "https://sh.onweb.gr:7115/;"},
    {"name": "Smooth Jazz",          "url": "https://smoothjazz.cdnstream1.com/2585_128.mp3"},
    {"name": "Il Sole 24 Ore",       "url": "https://ilsole24ore-radio.akamaized.net/hls/live/2035301/radio24/playlist-48000.m3u8"},
]

CONNECT_TIMEOUT = 10
MAX_RETRIES = 3

# ─── Colori ───────────────────────────────────────────────────────────────────
C_DEFAULT   = 1
C_SEL       = 2
C_PLAYING   = 3
C_HEADER    = 4
C_STATUS    = 5
C_HELP      = 6
C_TITLE     = 7
C_WAVE_1    = 8   # basso = verde
C_WAVE_2    = 9   # verde chiaro
C_WAVE_3    = 10  # giallo
C_WAVE_4    = 11  # giallo/rosso
C_WAVE_5    = 12  # rosso
C_BORDER    = 13
C_CLOCK     = 14
C_DIM       = 15
C_PEAK      = 16
C_PANEL     = 17
C_NUM       = 18  # numeri stazione

# Caratteri per le barre verticali (dal più basso al più alto)
BAR_CHARS = " ▁▂▃▄▅▆▇█"

SPINNER = ["◐","◓","◑","◒"]
WAVE_ROWS = 8


def init_colors():
    curses.start_color()
    curses.use_default_colors()
    # Base
    curses.init_pair(C_DEFAULT,  curses.COLOR_WHITE,   -1)
    curses.init_pair(C_SEL,      curses.COLOR_BLACK,   curses.COLOR_CYAN)
    curses.init_pair(C_PLAYING,  curses.COLOR_BLACK,   curses.COLOR_GREEN)
    curses.init_pair(C_HEADER,   curses.COLOR_CYAN,    -1)
    curses.init_pair(C_STATUS,   curses.COLOR_BLACK,   curses.COLOR_YELLOW)
    curses.init_pair(C_HELP,     curses.COLOR_YELLOW,  -1)
    curses.init_pair(C_TITLE,    curses.COLOR_GREEN,   -1)
    # Gradient FIRE: verde (basso) → giallo → rosso (alto)
    curses.init_pair(C_WAVE_1,   curses.COLOR_GREEN,   -1)
    curses.init_pair(C_WAVE_2,   curses.COLOR_GREEN,   -1)
    curses.init_pair(C_WAVE_3,   curses.COLOR_YELLOW,  -1)
    curses.init_pair(C_WAVE_4,   curses.COLOR_YELLOW,  -1)
    curses.init_pair(C_WAVE_5,   curses.COLOR_RED,     -1)
    curses.init_pair(C_BORDER,   curses.COLOR_BLUE,    -1)
    curses.init_pair(C_CLOCK,    curses.COLOR_MAGENTA, -1)
    curses.init_pair(C_DIM,      curses.COLOR_BLACK,   -1)
    curses.init_pair(C_PEAK,     curses.COLOR_WHITE,   -1)
    curses.init_pair(C_PANEL,    curses.COLOR_BLUE,    curses.COLOR_BLACK)
    curses.init_pair(C_NUM,      curses.COLOR_BLUE,    -1)


# ─── Visualizer a barre verticali FERME ───────────────────────────────────────
class StaticBarVisualizer:
    def __init__(self, n_bars=60):
        self.n      = n_bars
        self.levels = [0.0] * n_bars
        self.peaks  = [0.0] * n_bars
        self.peak_t = [0]   * n_bars
        self._t     = 0
        self._freqs = []
        self._phases = []
        for i in range(n_bars):
            norm = i / max(1, n_bars - 1)
            freq = 0.5 + norm * 4.0
            self._freqs.append(freq)
            self._phases.append(random.random() * 2 * math.pi)

    def resize(self, n_bars):
        if n_bars == self.n:
            return
        old_levels = self.levels
        old_peaks  = self.peaks
        old_peak_t = self.peak_t
        old_freqs  = self._freqs
        old_phases = self._phases

        self.n      = n_bars
        self.levels = [0.0] * n_bars
        self.peaks  = [0.0] * n_bars
        self.peak_t = [0]   * n_bars
        self._freqs = []
        self._phases = []

        for i in range(n_bars):
            if i < len(old_levels):
                self.levels[i] = old_levels[i]
                self.peaks[i]  = old_peaks[i]
                self.peak_t[i] = old_peak_t[i]
                self._freqs.append(old_freqs[i])
                self._phases.append(old_phases[i])
            else:
                norm = i / max(1, n_bars - 1)
                freq = 0.5 + norm * 4.0
                self._freqs.append(freq)
                self._phases.append(random.random() * 2 * math.pi)

    def tick(self, playing: bool):
        self._t += 1
        dt = 0.08

        for i in range(self.n):
            if playing:
                f = self._freqs[i]
                phase = self._phases[i] + self._t * dt * f

                spectrum_shape = 1.0 - (i / self.n) * 0.4

                base = math.sin(phase)
                harm2 = 0.3 * math.sin(phase * 2.1 + 1.0)
                harm3 = 0.15 * math.sin(phase * 3.7 + 2.3)
                noise = random.gauss(0, 0.06)

                beat = 0.0
                if self._t % 30 < 3:
                    beat = 0.2 * math.exp(-((self._t % 30) ** 2) / 4.0)

                target = max(0.0, min(1.0,
                    0.25 * spectrum_shape
                    + 0.35 * spectrum_shape * (base + harm2 + harm3 + 1.0) / 2.5
                    + beat * spectrum_shape
                    + noise
                ))

                alpha = 0.65 if target > self.levels[i] else 0.10
                self.levels[i] = self.levels[i] * (1 - alpha) + target * alpha
            else:
                self.levels[i] *= 0.82

            if self.levels[i] >= self.peaks[i]:
                self.peaks[i] = self.levels[i]
                self.peak_t[i] = 0
            else:
                self.peak_t[i] += 1
                if self.peak_t[i] > 25:
                    self.peaks[i] = max(0.0, self.peaks[i] - 0.025)

    def render_line(self, width):
        self.resize(width)
        out = []
        for i in range(width):
            lvl = self.levels[i]
            idx = int(lvl * (len(BAR_CHARS) - 1))
            ch  = BAR_CHARS[idx]
            if lvl > 0.75:
                cp = C_WAVE_5
            elif lvl > 0.55:
                cp = C_WAVE_4
            elif lvl > 0.40:
                cp = C_WAVE_3
            elif lvl > 0.20:
                cp = C_WAVE_2
            else:
                cp = C_WAVE_1
            out.append((ch, cp))
        return out


# ─── Volume Manager (senza ricaricare mpv) ────────────────────────────────────
class VolumeManager:
    def __init__(self):
        self.volume = 40
        self._detect_mixer()
        self.set_volume(self.volume)

    def _detect_mixer(self):
        r = subprocess.run(["which", "amixer"], capture_output=True)
        self._has_amixer = r.returncode == 0
        r = subprocess.run(["which", "pactl"], capture_output=True)
        self._has_pactl = r.returncode == 0

    def set_volume(self, vol):
        self.volume = max(0, min(100, vol))
        if self._has_amixer:
            subprocess.run(
                ["amixer", "-q", "sset", "Master", f"{self.volume}%"],
                capture_output=True
            )
        elif self._has_pactl:
            subprocess.run(
                ["pactl", "set-sink-volume", "@DEFAULT_SINK@", f"{self.volume}%"],
                capture_output=True
            )

    def volume_up(self, step=5):
        self.set_volume(self.volume + step)

    def volume_down(self, step=5):
        self.set_volume(self.volume - step)


# ─── Player con retry automatico ─────────────────────────────────────────────
class RadioPlayer:
    def __init__(self):
        self.process      = None
        self.current_idx  = None
        self.current_url  = None
        self.volume       = 40
        self.status_msg   = "Premi INVIO per avviare una stazione"
        self.is_connecting= False
        self._retry_count = 0
        self._retry_url   = None
        self._retry_idx   = None

    def play(self, url, idx, _retry=False):
        self._kill_process()
        self.current_idx   = idx
        self.current_url   = url
        self.is_connecting = True
        if _retry:
            self.status_msg = f"🔄 Retry {self._retry_count}/{MAX_RETRIES}…"
        else:
            self._retry_count = 0
            self.status_msg   = "⏳ Connessione…"

        cmd = [
            "mpv", "--no-video", "--really-quiet",
            "--cache=yes",
            "--cache-secs=15",
            "--demuxer-max-bytes=8MiB",
            "--network-timeout=10",
            url,
        ]
        try:
            self.process = subprocess.Popen(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                preexec_fn=os.setsid,
            )
            self._retry_url = url
            self._retry_idx = idx
            threading.Thread(target=self._watch, daemon=True).start()
        except FileNotFoundError:
            self.status_msg    = "❌ mpv non trovato — sudo apt install mpv"
            self.is_connecting = False
            self.current_idx   = None

    def _kill_process(self):
        if self.process:
            try:
                os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
            except Exception:
                pass
            self.process = None

    def _watch(self):
        deadline = time.time() + CONNECT_TIMEOUT
        while time.time() < deadline:
            if self.process is None:
                return
            if self.process.poll() is not None:
                break
            time.sleep(0.3)

        if self.process is None:
            return

        if self.process.poll() is not None:
            self._on_fail()
        else:
            self.is_connecting = False

    def _on_fail(self):
        self._retry_count += 1
        if self._retry_count <= MAX_RETRIES and self._retry_url:
            time.sleep(1.5)
            self.play(self._retry_url, self._retry_idx, _retry=True)
        else:
            self.status_msg    = f"❌ Stream non raggiungibile dopo {MAX_RETRIES} tentativi"
            self.is_connecting = False
            self.current_idx   = None

    def stop(self):
        self._retry_url  = None
        self._retry_idx  = None
        self._kill_process()
        self.current_idx   = None
        self.is_connecting = False
        self.status_msg    = "⏹  Stop"

    def is_playing(self):
        return self.process is not None and self.process.poll() is None


# ─── Helpers UI ───────────────────────────────────────────────────────────────
def safe_addstr(stdscr, y, x, text, attr=0):
    h, w = stdscr.getmaxyx()
    if y < 0 or y >= h - 1 or x < 0 or x >= w:
        return
    text = text[:max(0, w - x)]
    if not text:
        return
    try:
        stdscr.addstr(y, x, text, attr)
    except curses.error:
        pass

def draw_hline(stdscr, row, col, length, ch="─", attr=0):
    safe_addstr(stdscr, row, col, ch * length, attr)

def volume_bar(vol, width=18):
    filled = int(vol / 100 * width)
    return f"▕{'█' * filled}{'░' * (width - filled)}▏{vol:3d}%"


def draw_waveform_block(stdscr, viz, player, stations, frame, w, playing, connecting):
    n_bars = max(1, w - 4)
    viz.resize(n_bars)
    levels = viz.levels
    peaks  = viz.peaks
    steps = len(BAR_CHARS) - 1
    total = WAVE_ROWS * steps

    attr_map = {
        0: curses.color_pair(C_WAVE_5) | curses.A_BOLD,
        1: curses.color_pair(C_WAVE_5),
        2: curses.color_pair(C_WAVE_4) | curses.A_BOLD,
        3: curses.color_pair(C_WAVE_4),
        4: curses.color_pair(C_WAVE_3) | curses.A_BOLD,
        5: curses.color_pair(C_WAVE_2) | curses.A_BOLD,
        6: curses.color_pair(C_WAVE_2),
        7: curses.color_pair(C_WAVE_1),
    }
    attr_peak = curses.color_pair(C_PEAK) | curses.A_BOLD
    attr_dim  = curses.color_pair(C_DIM)
    attr_empty= curses.color_pair(C_DIM) | curses.A_DIM

    for row_i in range(WAVE_ROWS):
        cell_bot = total - row_i * steps
        cell_top = cell_bot - steps

        line_chars = []
        line_attrs = []

        for b in range(n_bars):
            lvl  = levels[b] if b < len(levels) else 0.0
            peak = peaks[b]  if b < len(peaks)  else 0.0
            bar_sub  = lvl  * total
            peak_sub = peak * total
            is_peak_here = cell_top <= peak_sub < cell_bot and peak > 0.02

            if bar_sub >= cell_bot:
                ch = "█"
                attr = attr_map.get(row_i, attr_map[7]) if playing else attr_dim
            elif bar_sub > cell_top:
                frac = (bar_sub - cell_top) / steps
                sub_i = max(1, int(frac * steps))
                ch = BAR_CHARS[sub_i]
                attr = attr_map.get(row_i, attr_map[7]) if playing else attr_dim
            elif is_peak_here:
                peak_frac = (peak_sub - cell_top) / steps
                sub_i = max(1, int(peak_frac * steps))
                ch = BAR_CHARS[sub_i]
                attr = attr_peak if playing else attr_dim
            else:
                ch = " "
                attr = attr_empty

            line_chars.append(ch)
            line_attrs.append(attr)

        for j, (ch, attr) in enumerate(zip(line_chars, line_attrs)):
            safe_addstr(stdscr, row_i, 2 + j, ch, attr)

    # Bordi laterali
    for r in range(WAVE_ROWS):
        safe_addstr(stdscr, r, 0, "│", curses.color_pair(C_BORDER))
        safe_addstr(stdscr, r, w - 1, "│", curses.color_pair(C_BORDER))

    # Orologio in alto a destra
    clock = time.strftime("%H:%M:%S")
    safe_addstr(stdscr, 0, max(0, w - len(clock) - 2), clock,
                curses.color_pair(C_CLOCK) | curses.A_BOLD)

    # Nome stazione centrato sulla riga più bassa del visualizer
    if player.current_idx is not None and playing:
        sname = stations[player.current_idx]["name"]
        spin = " " + SPINNER[frame % len(SPINNER)] + " " if connecting else " ♫ "
        label = f"{spin}{sname}{spin}"
        lx = max(2, (w - len(label)) // 2)
        safe_addstr(stdscr, WAVE_ROWS - 1, lx - 1, " " * (len(label) + 2),
                    curses.color_pair(C_DEFAULT) | curses.A_REVERSE)
        safe_addstr(stdscr, WAVE_ROWS - 1, lx, label,
                    curses.color_pair(C_PLAYING) | curses.A_BOLD)


def draw_screen(stdscr, stations, selected, scroll_offset, player, viz, frame):
    stdscr.erase()
    h, w = stdscr.getmaxyx()
    playing    = player.is_playing()
    connecting = player.is_connecting

    # ── 1. Waveform ───────────────────────────────────────────────────────────
    draw_waveform_block(stdscr, viz, player, stations, frame, w, playing, connecting)
    row = WAVE_ROWS

    draw_hline(stdscr, row, 0, w, "═", curses.color_pair(C_BORDER) | curses.A_BOLD)
    row += 1

    # ── 2. Header lista (centrato, senza colonna STATO) ──────────────────────
    # Calcola larghezza per centrare
    num_w = 4  # spazio per " #  "
    name_w = w - num_w - 2  # -2 per margine
    hdr_text = "STAZIONE"
    # Centra "STAZIONE" nello spazio disponibile
    pad_left = (name_w - len(hdr_text)) // 2
    hdr = f" {'#':>2}  {' ' * pad_left}{hdr_text}"
    safe_addstr(stdscr, row, 0, hdr[:w].ljust(w),
                curses.color_pair(C_HEADER) | curses.A_REVERSE | curses.A_BOLD)
    row += 1
    list_top = row

    # ── 3. Lista stazioni (senza colonna STATO, nome centrato) ───────────────
    bottom_reserve = 3
    list_h = max(1, h - list_top - bottom_reserve)

    for i, st in enumerate(stations[scroll_offset: scroll_offset + list_h]):
        abs_idx = scroll_offset + i
        is_sel  = abs_idx == selected
        is_play = abs_idx == player.current_idx

        # Simboli a sinistra: ▶ per in riproduzione, › per selezionato
        if is_play:
            prefix = "▶"
            attr  = curses.color_pair(C_PLAYING) | curses.A_BOLD
        elif is_sel:
            prefix = "›"
            attr  = curses.color_pair(C_SEL) | curses.A_BOLD
        else:
            prefix = " "
            attr  = curses.color_pair(C_DEFAULT)

        # Numero stazione (colore diverso)
        num_str = f"{abs_idx + 1:>2}"

        # Nome centrato nello spazio rimanente
        name_avail = w - 6  # spazio dopo " #  "
        name = st['name']
        if len(name) > name_avail:
            name = name[:name_avail - 1] + "…"
        pad = (name_avail - len(name)) // 2

        line = f" {num_str}  {prefix}{' ' * pad}{name}"
        safe_addstr(stdscr, list_top + i, 0, line[:w].ljust(w), attr)

        # Se la riga è selezionata ma non in play, colora solo il numero di diverso
        if is_sel and not is_play:
            safe_addstr(stdscr, list_top + i, 1, num_str, curses.color_pair(C_NUM))

    # Scrollbar
    if len(stations) > list_h:
        sb_col  = w - 1
        thumb_h = max(1, int(list_h * list_h / len(stations)))
        thumb_y = int(scroll_offset / max(1, len(stations) - list_h) * (list_h - thumb_h))
        for sr in range(list_h):
            ch = "█" if thumb_y <= sr < thumb_y + thumb_h else "░"
            safe_addstr(stdscr, list_top + sr, sb_col, ch, curses.color_pair(C_BORDER))

    # ── 4. Status + Volume ────────────────────────────────────────────────────
    sep_row = h - bottom_reserve
    draw_hline(stdscr, sep_row, 0, w, "─", curses.color_pair(C_BORDER))

    status_row = sep_row + 1
    if playing and not connecting:
        left = " 🔊  In ascolto"
    else:
        left = f" {player.status_msg}"
    right = f"Vol: {volume_bar(player.volume)} "
    gap   = max(1, w - len(left) - len(right))
    safe_addstr(stdscr, status_row, 0, (left + " " * gap + right)[:w].ljust(w),
                curses.color_pair(C_STATUS) | curses.A_BOLD)

    # ── 5. Help ───────────────────────────────────────────────────────────────
    help_row = status_row + 1
    keys = [("↑↓","Nav"), ("↵","Avvia"), ("S","Stop"),
            ("+/-","Vol"), ("R","Ricarica"), ("Q","Esci")]
    help_str = "  ".join(f"[{k}] {v}" for k, v in keys)
    safe_addstr(stdscr, help_row, 0, f" {help_str}"[:w], curses.color_pair(C_HELP))

    stdscr.refresh()


# ─── Main ─────────────────────────────────────────────────────────────────────
def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(60)
    init_colors()

    stations      = list(STATIONS)
    player        = RadioPlayer()
    vol_mgr       = VolumeManager()
    viz           = StaticBarVisualizer()
    selected      = 0
    scroll_offset = 0
    frame         = 0

    while True:
        h, w = stdscr.getmaxyx()

        viz.tick(player.is_playing())
        draw_screen(stdscr, stations, selected, scroll_offset, player, viz, frame)
        frame += 1

        key = stdscr.getch()

        list_top       = WAVE_ROWS + 2
        bottom_reserve = 3
        list_h         = max(1, h - list_top - bottom_reserve)

        if key in (ord("q"), ord("Q")):
            player.stop()
            break

        elif key == curses.KEY_UP:
            if selected > 0:
                selected -= 1
                if selected < scroll_offset:
                    scroll_offset = selected

        elif key == curses.KEY_DOWN:
            if selected < len(stations) - 1:
                selected += 1
                if selected >= scroll_offset + list_h:
                    scroll_offset = selected - list_h + 1

        elif key in (curses.KEY_ENTER, 10, 13):
            player.play(stations[selected]["url"], selected)

        elif key in (ord("s"), ord("S")):
            player.stop()

        elif key in (ord("+"), ord("=")):
            vol_mgr.volume_up()
            player.volume = vol_mgr.volume

        elif key in (ord("-"), ord("_")):
            vol_mgr.volume_down()
            player.volume = vol_mgr.volume

        elif key in (ord("r"), ord("R")):
            stations = list(STATIONS)
            selected = min(selected, len(stations) - 1)
            player.status_msg = f"✅ Lista ricaricata ({len(stations)} stazioni)"

        # Stream caduto inaspettatamente?
        if (player.current_idx is not None
                and not player.is_playing()
                and not player.is_connecting):
            player.status_msg  = "⚠️  Stream interrotto"
            player.current_idx = None


if __name__ == "__main__":
    if subprocess.run(["which", "mpv"], capture_output=True).returncode != 0:
        print("❌  mpv non trovato. Installalo con:")
        print("    sudo apt install mpv")
        sys.exit(1)
    try:
        curses.wrapper(main)
    except KeyboardInterrupt:
        pass
    print("👋  Ciao!")
