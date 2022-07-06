---
title: "Scaricare l'audio da un video di youtube"
author: Stefano Marzorati
layout: post
categories:
  - Linux
tags:
  - audio
  - mp3
  - video
  - youtube
---
Esempio:

`youtube-dl -t --extract-audio --audio-format mp3 http://www.youtube.com/watch?v=BjFSwWlgsXI`

``url="http://www.youtube.com/watch?v=BjFSwWlgsXI";audio=$(youtube-dl -s -e $url);wget -q -O - `youtube-dl -g $url`| ffmpeg -i - -f mp3 -vn -acodec libmp3lame - > "$audio.mp3"``