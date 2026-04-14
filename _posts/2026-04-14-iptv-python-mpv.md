---
title: "IPTV in Python con MPV su Windows"
date: 2026-04-14 07:30:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/tv.png'
share-img: 'https://marzorati.co/img/tv.png'
layout: post
categories: [IPTV Player]
tags: [debian, mpv, iptv, digitale terrestre, dtt, python]
---
Salva questo codice in un file e chiamalo **iptv_player.pyw**   

Requisiti:   
- Python 3.8+ python.org — spunta *Add Python to PATH* durante l'installazione
- MPV Player da mpv.io 

```
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import threading
import subprocess
import urllib.request
import re, os, sys, json, gzip
from pathlib import Path
from datetime import datetime, timezone, timedelta
import xml.etree.ElementTree as ET

# ─── Constants ────────────────────────────────────────────────────────────────
CONFIG_FILE = Path.home() / ".iptv_player_config.json"
EPG_CACHE   = Path.home() / ".iptv_player_epg_cache.json"
DEFAULT_MPV = r"C:\Program Files\mpv\mpv.exe"
EPG_URL     = "https://iptv-epg.org/files/epg-it.xml"
EPG_MAX_AGE = 3600  # secondi — ricarica EPG dopo 1 ora


# ─── M3U Parser ───────────────────────────────────────────────────────────────
def parse_m3u(content):
    channels = []
    lines = content.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if line.startswith("#EXTINF"):
            info = line
            name_match  = re.search(r'tvg-name="([^"]*)"',    info)
            id_match    = re.search(r'tvg-id="([^"]*)"',      info)
            group_match = re.search(r'group-title="([^"]*)"', info)
            logo_match  = re.search(r'tvg-logo="([^"]*)"',    info)
            comma_idx    = info.rfind(",")
            display_name = info[comma_idx+1:].strip() if comma_idx != -1 else "Sconosciuto"
            if name_match and name_match.group(1):
                display_name = name_match.group(1)
            tvg_id = id_match.group(1).strip()    if id_match    else ""
            group  = group_match.group(1).strip() if group_match else "Generale"
            logo   = logo_match.group(1).strip()  if logo_match  else ""
            j, url = i + 1, ""
            while j < len(lines):
                candidate = lines[j].strip()
                if candidate and not candidate.startswith("#"):
                    url = candidate
                    i = j
                    break
                j += 1
            if url:
                channels.append({
                    "name":   display_name,
                    "tvg_id": tvg_id,
                    "group":  group or "Generale",
                    "logo":   logo,
                    "url":    url,
                })
        i += 1
    return channels


# ─── XMLTV / EPG Parser ───────────────────────────────────────────────────────
def parse_xmltv_datetime(s):
    """Converte '20260414120000 +0200' in datetime UTC-aware."""
    s = s.strip()
    m = re.match(r"(\d{14})\s*([+-]\d{4})?", s)
    if not m:
        return None
    dt_str, tz_str = m.group(1), m.group(2) or "+0000"
    dt = datetime.strptime(dt_str, "%Y%m%d%H%M%S")
    sign = 1 if tz_str[0] == "+" else -1
    hh, mm = int(tz_str[1:3]), int(tz_str[3:5])
    offset = timezone(timedelta(minutes=sign * (hh * 60 + mm)))
    return dt.replace(tzinfo=offset).astimezone(timezone.utc)


def parse_epg_xml(raw_bytes):
    """
    Parsa XMLTV (anche gzippato).
    Restituisce dict: { channel_id: [ {start, stop, title, desc, category} ] }
    """
    try:
        raw_bytes = gzip.decompress(raw_bytes)
    except Exception:
        pass
    try:
        root = ET.fromstring(raw_bytes.decode("utf-8", errors="replace"))
    except ET.ParseError:
        return {}

    epg = {}
    now_utc = datetime.now(timezone.utc)
    cutoff  = now_utc + timedelta(hours=12)

    for prog in root.iter("programme"):
        ch_id = prog.get("channel", "").strip()
        if not ch_id:
            continue
        start = parse_xmltv_datetime(prog.get("start", ""))
        stop  = parse_xmltv_datetime(prog.get("stop",  ""))
        if not start or not stop:
            continue
        if stop < now_utc - timedelta(minutes=5):
            continue
        if start > cutoff:
            continue
        title_el = prog.find("title")
        desc_el  = prog.find("desc")
        cat_el   = prog.find("category")
        entry = {
            "start":    start.isoformat(),
            "stop":     stop.isoformat(),
            "title":    (title_el.text or "").strip() if title_el is not None else "",
            "desc":     (desc_el.text  or "").strip() if desc_el  is not None else "",
            "category": (cat_el.text   or "").strip() if cat_el   is not None else "",
        }
        epg.setdefault(ch_id, []).append(entry)

    return epg


def load_epg_cache():
    if EPG_CACHE.exists():
        try:
            data = json.loads(EPG_CACHE.read_text(encoding="utf-8"))
            age  = datetime.now(timezone.utc).timestamp() - data.get("fetched_at", 0)
            if age < EPG_MAX_AGE:
                return data.get("epg", {}), False
        except Exception:
            pass
    return {}, True


def save_epg_cache(epg_dict):
    try:
        EPG_CACHE.write_text(
            json.dumps({"fetched_at": datetime.now(timezone.utc).timestamp(),
                        "epg": epg_dict}, ensure_ascii=False),
            encoding="utf-8")
    except Exception:
        pass


# ─── Config helpers ───────────────────────────────────────────────────────────
def load_config():
    if CONFIG_FILE.exists():
        try:
            return json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"mpv_path": DEFAULT_MPV, "last_url": "", "favorites": []}


def save_config(cfg):
    CONFIG_FILE.write_text(json.dumps(cfg, indent=2), encoding="utf-8")


# ─── Main App ─────────────────────────────────────────────────────────────────
class IPTVApp(tk.Tk):
    DARK_BG   = "#0d0f14"
    PANEL_BG  = "#13161e"
    CARD_BG   = "#1a1e2a"
    DETAIL_BG = "#161a24"
    ACCENT    = "#e63946"
    ACCENT2   = "#457b9d"
    GREEN     = "#2ec27e"
    YELLOW    = "#f4d03f"
    FG        = "#e8eaf0"
    FG_DIM    = "#6b7280"
    FG_MED    = "#9ca3af"
    HOVER_BG  = "#252a38"
    SEL_BG    = "#1d3557"

    def __init__(self):
        super().__init__()
        self.cfg       = load_config()
        self.channels  = []
        self.filtered  = []
        self.favorites = set(self.cfg.get("favorites", []))
        self.show_fav  = False
        self.epg       = {}
        self.epg_loaded= False

        self.title("IPTV Player")
        self.geometry("1160x700")
        self.minsize(860, 540)
        self.configure(bg=self.DARK_BG)
        try:
            self.iconbitmap(default="")
        except Exception:
            pass

        self._build_ui()
        self._apply_styles()

        if self.cfg.get("last_url"):
            self.url_var.set(self.cfg["last_url"])

        self._start_epg_load()

    # ── UI ────────────────────────────────────────────────────────────────────
    def _build_ui(self):
        # Top bar
        top = tk.Frame(self, bg=self.PANEL_BG, height=52)
        top.pack(fill="x", side="top")
        top.pack_propagate(False)

        tk.Label(top, text="▶  IPTV", font=("Courier New", 17, "bold"),
                 bg=self.PANEL_BG, fg=self.ACCENT).pack(side="left", padx=18, pady=8)

        self.epg_status_lbl = tk.Label(top, text="EPG: in caricamento…",
                                        bg=self.PANEL_BG, fg=self.FG_DIM,
                                        font=("Segoe UI", 8))
        self.epg_status_lbl.pack(side="left", padx=8)

        tk.Button(top, text="↻ Aggiorna EPG", command=self._force_epg_reload,
                  bg=self.CARD_BG, fg=self.FG_DIM, relief="flat",
                  activebackground=self.HOVER_BG, cursor="hand2",
                  font=("Segoe UI", 8)).pack(side="left", padx=4, pady=10)

        tk.Button(top, text="⚙ MPV Path", command=self._set_mpv,
                  bg=self.CARD_BG, fg=self.FG_DIM, relief="flat",
                  activebackground=self.HOVER_BG, cursor="hand2",
                  font=("Segoe UI", 9)).pack(side="right", padx=12, pady=10)

        # URL bar
        url_frame = tk.Frame(self, bg=self.DARK_BG)
        url_frame.pack(fill="x", padx=16, pady=(10, 4))
        tk.Label(url_frame, text="URL playlist M3U:", bg=self.DARK_BG,
                 fg=self.FG_DIM, font=("Segoe UI", 9)).pack(side="left")
        self.url_var = tk.StringVar()
        url_entry = tk.Entry(url_frame, textvariable=self.url_var,
                             bg=self.CARD_BG, fg=self.FG, insertbackground=self.FG,
                             relief="flat", font=("Consolas", 10), bd=0)
        url_entry.pack(side="left", fill="x", expand=True, padx=(8, 8), ipady=6, ipadx=6)
        url_entry.bind("<Return>", lambda e: self._load_playlist())
        self.load_btn = tk.Button(url_frame, text="  Carica  ",
                                  command=self._load_playlist,
                                  bg=self.ACCENT, fg="white", relief="flat",
                                  activebackground="#c62a35", cursor="hand2",
                                  font=("Segoe UI", 9, "bold"))
        self.load_btn.pack(side="left", ipady=5, ipadx=4)

        # Search bar
        sf = tk.Frame(self, bg=self.DARK_BG)
        sf.pack(fill="x", padx=16, pady=(4, 8))
        tk.Label(sf, text="🔍", bg=self.DARK_BG, fg=self.FG_DIM,
                 font=("Segoe UI", 11)).pack(side="left")
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *_: self._filter())
        tk.Entry(sf, textvariable=self.search_var,
                 bg=self.CARD_BG, fg=self.FG, insertbackground=self.FG,
                 relief="flat", font=("Segoe UI", 10), bd=0
                 ).pack(side="left", fill="x", expand=True, padx=(6, 8), ipady=5, ipadx=6)
        self.fav_btn = tk.Button(sf, text="☆ Preferiti", command=self._toggle_favorites,
                                  bg=self.CARD_BG, fg=self.FG_DIM, relief="flat",
                                  activebackground=self.HOVER_BG, cursor="hand2",
                                  font=("Segoe UI", 9))
        self.fav_btn.pack(side="left", ipady=4, ipadx=8)
        self.group_var = tk.StringVar(value="Tutti i gruppi")
        self.group_menu = ttk.Combobox(sf, textvariable=self.group_var,
                                        state="readonly", width=22, font=("Segoe UI", 9))
        self.group_menu.pack(side="left", padx=(8, 0), ipady=2)
        self.group_menu.bind("<<ComboboxSelected>>", lambda e: self._filter())

        # Body: list + detail
        body = tk.Frame(self, bg=self.DARK_BG)
        body.pack(fill="both", expand=True, padx=16, pady=(0, 0))

        list_frame = tk.Frame(body, bg=self.CARD_BG)
        list_frame.pack(side="left", fill="both", expand=True)
        sb = tk.Scrollbar(list_frame, bg=self.CARD_BG, troughcolor=self.DARK_BG, relief="flat")
        sb.pack(side="right", fill="y")
        self.listbox = tk.Listbox(list_frame, bg=self.CARD_BG, fg=self.FG,
                                   selectbackground=self.SEL_BG, selectforeground=self.FG,
                                   activestyle="none", font=("Segoe UI", 10),
                                   relief="flat", bd=0, yscrollcommand=sb.set, cursor="hand2")
        self.listbox.pack(fill="both", expand=True, padx=2, pady=2)
        sb.config(command=self.listbox.yview)
        self.listbox.bind("<Double-Button-1>", lambda e: self._play_selected())
        self.listbox.bind("<Return>",          lambda e: self._play_selected())
        self.listbox.bind("<<ListboxSelect>>", lambda e: self._on_channel_select())
        self.listbox.bind("<Button-3>",        self._show_context_menu)

        # Detail panel
        self.detail_panel = tk.Frame(body, bg=self.DETAIL_BG, width=300)
        self.detail_panel.pack(side="right", fill="y", padx=(8, 0))
        self.detail_panel.pack_propagate(False)
        self._build_detail_panel()

        # Bottom bar
        bot = tk.Frame(self, bg=self.PANEL_BG, height=42)
        bot.pack(fill="x", side="bottom")
        bot.pack_propagate(False)
        self.status_var = tk.StringVar(value="Inserisci un URL M3U e clicca Carica")
        tk.Label(bot, textvariable=self.status_var, bg=self.PANEL_BG,
                 fg=self.FG_DIM, font=("Segoe UI", 9)).pack(side="left", padx=14)
        self.play_btn = tk.Button(bot, text="▶  Riproduci con MPV",
                                   command=self._play_selected,
                                   bg=self.ACCENT2, fg="white", relief="flat",
                                   activebackground="#2e5f7a", cursor="hand2",
                                   font=("Segoe UI", 9, "bold"), state="disabled")
        self.play_btn.pack(side="right", padx=12, pady=6, ipadx=10, ipady=4)

        # Context menu
        self.ctx_menu = tk.Menu(self, tearoff=0, bg=self.CARD_BG, fg=self.FG,
                                 activebackground=self.ACCENT, activeforeground="white", bd=0)
        self.ctx_menu.add_command(label="▶  Riproduci",             command=self._play_selected)
        self.ctx_menu.add_command(label="☆  Aggiungi ai preferiti", command=self._toggle_fav_selected)
        self.ctx_menu.add_separator()
        self.ctx_menu.add_command(label="📋  Copia URL",            command=self._copy_url)

    def _build_detail_panel(self):
        p = self.detail_panel

        self.det_name = tk.Label(p, text="", bg=self.DETAIL_BG, fg=self.FG,
                                  font=("Segoe UI", 12, "bold"), wraplength=270, justify="left")
        self.det_name.pack(anchor="w", padx=14, pady=(16, 2))

        self.det_group = tk.Label(p, text="", bg=self.DETAIL_BG, fg=self.FG_DIM,
                                   font=("Segoe UI", 8))
        self.det_group.pack(anchor="w", padx=14, pady=2)

        ttk.Separator(p, orient="horizontal").pack(fill="x", padx=14, pady=8)

        tk.Label(p, text="ORA IN ONDA", bg=self.DETAIL_BG, fg=self.ACCENT,
                 font=("Segoe UI", 7, "bold")).pack(anchor="w", padx=14)

        self.det_now_title = tk.Label(p, text="—", bg=self.DETAIL_BG, fg=self.FG,
                                       font=("Segoe UI", 10, "bold"), wraplength=270, justify="left")
        self.det_now_title.pack(anchor="w", padx=14, pady=(2, 0))

        self.det_now_time = tk.Label(p, text="", bg=self.DETAIL_BG, fg=self.FG_DIM,
                                      font=("Segoe UI", 8))
        self.det_now_time.pack(anchor="w", padx=14)

        self.prog_canvas = tk.Canvas(p, height=4, bg=self.CARD_BG,
                                      highlightthickness=0, bd=0)
        self.prog_canvas.pack(fill="x", padx=14, pady=(4, 2))
        self.prog_bar = self.prog_canvas.create_rectangle(0, 0, 0, 4,
                                                           fill=self.GREEN, outline="")

        self.det_now_desc = tk.Label(p, text="", bg=self.DETAIL_BG, fg=self.FG_MED,
                                      font=("Segoe UI", 8), wraplength=270, justify="left")
        self.det_now_desc.pack(anchor="w", padx=14, pady=(2, 6))

        ttk.Separator(p, orient="horizontal").pack(fill="x", padx=14, pady=6)

        tk.Label(p, text="PROSSIMI PROGRAMMI", bg=self.DETAIL_BG, fg=self.ACCENT2,
                 font=("Segoe UI", 7, "bold")).pack(anchor="w", padx=14)

        self.next_frame = tk.Frame(p, bg=self.DETAIL_BG)
        self.next_frame.pack(fill="x", padx=14, pady=(4, 0))

        ttk.Separator(p, orient="horizontal").pack(fill="x", padx=14, pady=8)

        self.no_epg_lbl = tk.Label(p, text="", bg=self.DETAIL_BG, fg=self.FG_DIM,
                                    font=("Segoe UI", 8, "italic"), wraplength=270)
        self.no_epg_lbl.pack(anchor="w", padx=14)

    def _apply_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TCombobox",
                        fieldbackground=self.CARD_BG, background=self.CARD_BG,
                        foreground=self.FG, selectbackground=self.SEL_BG,
                        arrowcolor=self.FG_DIM)
        style.configure("TSeparator", background=self.HOVER_BG)

    # ── EPG ───────────────────────────────────────────────────────────────────
    def _start_epg_load(self):
        cached, stale = load_epg_cache()
        if cached and not stale:
            self.epg = cached
            self.epg_loaded = True
            n = sum(len(v) for v in cached.values())
            self.epg_status_lbl.config(
                text=f"EPG: {len(cached)} canali  ({n} prog.) — cache",
                fg=self.GREEN)
        else:
            self.epg_status_lbl.config(text="EPG: download in corso…", fg=self.YELLOW)
            threading.Thread(target=self._fetch_epg, daemon=True).start()

    def _force_epg_reload(self):
        try:
            EPG_CACHE.unlink(missing_ok=True)
        except Exception:
            pass
        self.epg = {}
        self.epg_loaded = False
        self.epg_status_lbl.config(text="EPG: download in corso…", fg=self.YELLOW)
        threading.Thread(target=self._fetch_epg, daemon=True).start()

    def _fetch_epg(self):
        try:
            req = urllib.request.Request(
                EPG_URL, headers={"User-Agent": "Mozilla/5.0", "Accept-Encoding": "gzip"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read()
            epg = parse_epg_xml(raw)
            save_epg_cache(epg)
            self.after(0, self._on_epg_loaded, epg)
        except Exception as e:
            self.after(0, self._on_epg_error, str(e))

    def _on_epg_loaded(self, epg):
        self.epg = epg
        self.epg_loaded = True
        n = sum(len(v) for v in epg.values())
        self.epg_status_lbl.config(
            text=f"EPG: {len(epg)} canali  ({n} prog.)",
            fg=self.GREEN)
        sel = self.listbox.curselection()
        if sel:
            self._on_channel_select()

    def _on_epg_error(self, err):
        self.epg_status_lbl.config(text=f"EPG: errore — {err[:55]}", fg=self.ACCENT)

    def _get_epg_for_channel(self, ch):
        if not self.epg:
            return []
        # 1) match esatto tvg_id
        tvg_id = ch.get("tvg_id", "").strip()
        if tvg_id and tvg_id in self.epg:
            return self.epg[tvg_id]
        # 2) match case-insensitive
        tvg_lower = tvg_id.lower()
        for k, v in self.epg.items():
            if k.lower() == tvg_lower:
                return v
        # 3) fuzzy: nome canale contenuto nell'id EPG o viceversa
        name_lower = ch["name"].lower()
        for k, v in self.epg.items():
            k_base = k.lower().split(".")[0]
            if k_base in name_lower or name_lower in k.lower():
                return v
        return []

    def _current_and_next(self, programs):
        now = datetime.now(timezone.utc)
        current, upcoming = None, []
        for p in programs:
            try:
                start = datetime.fromisoformat(p["start"])
                stop  = datetime.fromisoformat(p["stop"])
            except Exception:
                continue
            if start <= now < stop:
                current = {**p, "_start": start, "_stop": stop}
            elif start > now:
                upcoming.append({**p, "_start": start, "_stop": stop})
        upcoming.sort(key=lambda x: x["_start"])
        return current, upcoming[:4]

    def _fmt_time(self, dt):
        return dt.astimezone().strftime("%H:%M")

    # ── Detail panel ─────────────────────────────────────────────────────────
    def _on_channel_select(self):
        sel = self.listbox.curselection()
        if not sel:
            return
        ch = self.filtered[sel[0]]
        self.det_name.config(text=ch["name"])
        self.det_group.config(text=ch["group"])

        programs = self._get_epg_for_channel(ch)
        current, upcoming = self._current_and_next(programs)

        if current:
            self.det_now_title.config(text=current["title"] or "—", fg=self.FG)
            t = f'{self._fmt_time(current["_start"])} – {self._fmt_time(current["_stop"])}'
            if current.get("category"):
                t += f'  [{current["category"]}]'
            self.det_now_time.config(text=t)
            total   = (current["_stop"] - current["_start"]).total_seconds()
            elapsed = (datetime.now(timezone.utc) - current["_start"]).total_seconds()
            pct = max(0.0, min(1.0, elapsed / total)) if total > 0 else 0.0
            self.prog_canvas.update_idletasks()
            w = self.prog_canvas.winfo_width()
            self.prog_canvas.coords(self.prog_bar, 0, 0, int(w * pct), 4)
            desc = current.get("desc", "")
            self.det_now_desc.config(text=desc[:200] + ("…" if len(desc) > 200 else ""))
            self.no_epg_lbl.config(text="")
        else:
            self.det_now_title.config(text="Nessun dato EPG", fg=self.FG_DIM)
            self.det_now_time.config(text="")
            self.prog_canvas.coords(self.prog_bar, 0, 0, 0, 4)
            self.det_now_desc.config(text="")
            if not self.epg_loaded:
                self.no_epg_lbl.config(text="EPG in caricamento…")
            elif not self.epg:
                self.no_epg_lbl.config(text="EPG non disponibile")
            elif not programs:
                self.no_epg_lbl.config(
                    text="Nessun match EPG.\nVerifica che tvg-id nella\nplaylist corrisponda all'EPG.")
            else:
                self.no_epg_lbl.config(text="Nessun programma in corso")

        for w in self.next_frame.winfo_children():
            w.destroy()
        for prog in upcoming:
            row = tk.Frame(self.next_frame, bg=self.DETAIL_BG)
            row.pack(fill="x", pady=2)
            tk.Label(row, text=self._fmt_time(prog["_start"]),
                     bg=self.DETAIL_BG, fg=self.ACCENT2,
                     font=("Consolas", 8), width=6, anchor="w").pack(side="left")
            tk.Label(row, text=prog["title"] or "—",
                     bg=self.DETAIL_BG, fg=self.FG_MED,
                     font=("Segoe UI", 9), anchor="w", wraplength=210
                     ).pack(side="left", fill="x", expand=True)
        if not upcoming and current:
            tk.Label(self.next_frame, text="Nessun altro programma disponibile",
                     bg=self.DETAIL_BG, fg=self.FG_DIM,
                     font=("Segoe UI", 8, "italic")).pack(anchor="w")

        self.after(30000, self._refresh_progress)

    def _refresh_progress(self):
        sel = self.listbox.curselection()
        if sel:
            self._on_channel_select()

    # ── Playlist ─────────────────────────────────────────────────────────────
    def _load_playlist(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showwarning("Attenzione", "Inserisci un URL M3U valido.")
            return
        self.cfg["last_url"] = url
        save_config(self.cfg)
        self.status_var.set("⏳ Download playlist in corso…")
        self.load_btn.config(state="disabled")
        threading.Thread(target=self._fetch_playlist, args=(url,), daemon=True).start()

    def _fetch_playlist(self, url):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=15) as resp:
                raw = resp.read()
            try:
                content = raw.decode("utf-8")
            except UnicodeDecodeError:
                content = raw.decode("latin-1")
            channels = parse_m3u(content)
            self.after(0, self._on_playlist_loaded, channels)
        except Exception as e:
            self.after(0, self._on_playlist_error, str(e))

    def _on_playlist_loaded(self, channels):
        self.channels = channels
        self.load_btn.config(state="normal")
        if not channels:
            self.status_var.set("⚠ Nessun canale trovato nella playlist.")
            return
        groups = sorted({c["group"] for c in channels})
        self.group_menu["values"] = ["Tutti i gruppi"] + groups
        self.group_var.set("Tutti i gruppi")
        self._filter()
        self.status_var.set(f"✅ {len(channels)} canali caricati")

    def _on_playlist_error(self, err):
        self.load_btn.config(state="normal")
        self.status_var.set(f"❌ Errore: {err}")
        messagebox.showerror("Errore caricamento", f"Impossibile scaricare la playlist:\n{err}")

    # ── Filtering ─────────────────────────────────────────────────────────────
    def _filter(self):
        query = self.search_var.get().lower()
        group = self.group_var.get()
        pool  = self.channels
        if self.show_fav:
            pool = [c for c in pool if c["name"] in self.favorites]
        if group and group != "Tutti i gruppi":
            pool = [c for c in pool if c["group"] == group]
        if query:
            pool = [c for c in pool if query in c["name"].lower()
                    or query in c["group"].lower()]
        self.filtered = pool
        self.listbox.delete(0, "end")
        for ch in pool:
            star = "★ " if ch["name"] in self.favorites else "  "
            self.listbox.insert("end", f"{star}{ch['name']}   [{ch['group']}]")
        cnt = f"{len(pool)} canali"
        if len(pool) != len(self.channels):
            cnt += f" (filtrati su {len(self.channels)})"
        self.status_var.set(cnt)
        self.play_btn.config(state="normal" if pool else "disabled")

    def _toggle_favorites(self):
        self.show_fav = not self.show_fav
        self.fav_btn.config(
            text="★ Preferiti" if self.show_fav else "☆ Preferiti",
            fg=self.YELLOW if self.show_fav else self.FG_DIM)
        self._filter()

    # ── Playback ──────────────────────────────────────────────────────────────
    def _play_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("Nessuna selezione", "Seleziona un canale dalla lista.")
            return
        ch  = self.filtered[sel[0]]
        mpv = self.cfg.get("mpv_path", DEFAULT_MPV)
        if not os.path.isfile(mpv):
            if messagebox.askyesno("MPV non trovato",
                                   f"MPV non trovato in:\n{mpv}\n\nVuoi impostare il percorso corretto?"):
                self._set_mpv()
            return
        cmd = [mpv, "--force-window=yes", "--keep-open=yes", ch["url"]]
        try:
            proc = subprocess.Popen(cmd)
            self.status_var.set(f"▶ Avvio: {ch['name']}…")
            self.after(2000, lambda: self._check_proc(proc, ch["name"]))
        except FileNotFoundError:
            messagebox.showerror("Errore MPV",
                                 f"mpv.exe non trovato:\n{mpv}\n\nVerificalo con ⚙ MPV Path.")
        except PermissionError:
            messagebox.showerror("Errore permessi",
                                 f"Impossibile eseguire:\n{mpv}\n\nProva come Amministratore.")
        except Exception as e:
            messagebox.showerror("Errore MPV", f"{type(e).__name__}: {e}")

    def _check_proc(self, proc, name):
        ret = proc.poll()
        if ret is None:
            self.status_var.set(f"▶ Riproduzione: {name}")
        else:
            self.status_var.set(f"❌ MPV uscito con codice {ret}")
            messagebox.showerror("MPV terminato",
                                 f"MPV si è chiuso subito (codice {ret}).\n\n"
                                 "• URL non raggiungibile o non valido\n"
                                 "• Stream con DRM non supportato\n"
                                 "• Codec mancanti in MPV")

    # ── Context menu ──────────────────────────────────────────────────────────
    def _show_context_menu(self, event):
        idx = self.listbox.nearest(event.y)
        if idx >= 0:
            self.listbox.selection_clear(0, "end")
            self.listbox.selection_set(idx)
            self._on_channel_select()
            self.ctx_menu.tk_popup(event.x_root, event.y_root)

    def _toggle_fav_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            return
        ch = self.filtered[sel[0]]
        if ch["name"] in self.favorites:
            self.favorites.discard(ch["name"])
        else:
            self.favorites.add(ch["name"])
        self.cfg["favorites"] = list(self.favorites)
        save_config(self.cfg)
        self._filter()

    def _copy_url(self):
        sel = self.listbox.curselection()
        if not sel:
            return
        ch = self.filtered[sel[0]]
        self.clipboard_clear()
        self.clipboard_append(ch["url"])
        self.status_var.set("📋 URL copiato negli appunti")

    # ── Settings ──────────────────────────────────────────────────────────────
    def _set_mpv(self):
        new_path = simpledialog.askstring(
            "Percorso MPV",
            "Inserisci il percorso completo di mpv.exe:",
            initialvalue=self.cfg.get("mpv_path", DEFAULT_MPV),
            parent=self)
        if new_path:
            self.cfg["mpv_path"] = new_path.strip()
            save_config(self.cfg)
            self.status_var.set("✅ Percorso MPV aggiornato")


# ─── Entry point ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app = IPTVApp()
    app.mainloop()

```
