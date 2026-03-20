---
title: "IPTV direttamente da terminal con MPV su Debian"
date: 2026-03-20 07:30:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/debian.png'
share-img: 'https://marzorati.co/img/debian.png'
layout: post
categories: [Linux]
tags: [debian, mpv, iptv, digitale terrestre]
---
Scarica il file iptv e copialo con questo comando:
```
sudo wget https://marzorati.co/dowanload/iptv -qO /usr/local/bin/iptv && sudo chmod +x /usr/local/bin/iptv
```

Esegui solo una volta:    
```
iptv https://raw.githubusercontent.com/maginetweb-arch/TVITALIA/refs/heads/main/iptvit.m3u
```
Esegui:   
```
iptv
```   
###### Thanks to [https://github.com/shahin8r/iptv](https://github.com/shahin8r/iptv)