---
id: 2811
title: Convertire video in immagini
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2811
permalink: /convertire-video-in-immagini/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2611078561
categories:
  - Linux
  - Windows
tags:
  - convert
  - ffmpeg
  - images
  - video
---
Esempio:

`ffmpeg -i movie.mp4 -r 0.25 frames_%04d.png`

Questo comando salva le immagini ogni 4 secondi.