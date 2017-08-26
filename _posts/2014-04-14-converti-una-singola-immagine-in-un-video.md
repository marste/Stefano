---
id: 2820
title: Converti una singola immagine in un video
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2820
permalink: /converti-una-singola-immagine-in-un-video/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2611078253
categories:
  - Linux
  - Windows
tags:
  - convert
  - image
  - video
---
Esempio:

`ffmpeg -loop 1 -i c:\image.png -c:v libx264 -t 30 -pix_fmt yuv420p c:\video.mp4`

Il parametro -t specifica la durate del video