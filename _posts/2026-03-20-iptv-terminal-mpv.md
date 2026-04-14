---
title: "IPTV direttamente da terminal con MPV su Debian"
date: 2026-03-20 07:30:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/debian.png'
share-img: 'https://marzorati.co/img/debian.png'
layout: post
categories: [Linux]
tags: [debian, mpv, iptv, digitale terrestre, dtt]
---
Scarica il file iptv e copialo con questo comando:
```
sudo wget https://marzorati.co/download/iptv -qO /usr/local/bin/iptv && sudo chmod +x /usr/local/bin/iptv
```

Esegui solo una volta:    
```
iptv https://raw.githubusercontent.com/maginetweb-arch/TVITALIA/refs/heads/main/iptvit.m3u
```
Esegui:   
```
iptv
```   

Crea un file di configurazione per mpv:  
```
sudo nano ~/.config/mpv/mpv.conf
```

e copia queste opzioni:  
```
# ==========================================
# CONFIGURAZIONE MPV PER IPTV / LIVE STREAMING
# ==========================================

# --- RETE & CACHE ---
cache=yes
cache-secs=15
demuxer-max-bytes=512M
demuxer-max-back-bytes=128M
stream-lavf-o=reconnect=1:reconnect_streamed=1:reconnect_delay_max=10:timeout=30
http-header-fields=User-Agent: VLC/3.0.20
network-timeout=30

# --- COMPORTAMENTO STREAMING ---
demuxer-lavf-probe-info=no
force-seekable=no
save-position-on-quit=no
keep-open=no
fs=yes

# --- VIDEO & AUDIO ---
hwdec=auto
vo=gpu
video-sync=audio
audio-sync=display-resample
interpolation=no
tscale=linear

# --- DEBUG (decommenta se necessario) ---
# demuxer-lavf-o=fflags=+genpts+igndts
# log-file=~/mpv-iptv.log
```

###### Thanks to [https://github.com/shahin8r/iptv](https://github.com/shahin8r/iptv)
