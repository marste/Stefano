---
id: 2815
title: Creare un video slideshow da delle immagini
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2815
permalink: /creare-un-video-slideshow-da-delle-immagini/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2611076820
categories:
  - Linux
  - Windows
tags:
  - image
  - slideshow
  - video
---
Esempio:

`ffmpeg -r 1/5 -i c:\img%03d.png -c:v libx264 -r 30 -pix_fmt yuv420p c:\slideshow.mp4`

Questo comando crea una slideshow usando una serie di immagini nominate: img001.png, img002.png, etc. Ogni immagine durerà 5 secondi (-r 1/5).