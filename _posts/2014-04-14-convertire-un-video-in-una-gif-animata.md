---
id: 2804
title: Convertire un video in una gif animata
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2804
permalink: /convertire-un-video-in-una-gif-animata/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2610920717
categories:
  - Linux
  - Windows
tags:
  - animata
  - gif
---
Esempio:

`ffmpeg -i c:\video.mp4 -vf scale=500:-1 -t 10 -r 10 c:\image.gif`

il parametro -t specifica la durata, mentre -r specifica il frame rate (fps)