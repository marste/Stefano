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
# --- SPECIFICO IPTV (LIVE STREAMING) ---
deinterlace=yes                 # Attiva il deinterlacciamento automatico
cache=yes
demuxer-max-bytes=500MiB        # Buffer generoso per flussi 4K o HD instabili
demuxer-max-back-bytes=100MiB
cache-secs=30                   # 30 secondi di sicurezza contro i cali di conn>
demuxer-readahead-secs=15       # Legge molto avanti per una riproduzione fluida

# --- QUALITÀ IMMAGINE (MESA/AMD/INTEL) ---
# Ottimo scaling senza distruggere la durata della batteria (se su laptop)
scale=ewa_lanczos
cscale=mitchell
# Rimuove gli artefatti "a scalino" (banding) comuni nelle IPTV compresse
debian-debnd=yes
```

###### Thanks to [https://github.com/shahin8r/iptv](https://github.com/shahin8r/iptv)
