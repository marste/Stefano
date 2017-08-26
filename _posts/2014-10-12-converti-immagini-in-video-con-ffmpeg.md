---
id: 3126
title: Converti immagini in video con ffmpeg
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3126
permalink: /converti-immagini-in-video-con-ffmpeg/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3110232549
categories:
  - Linux
  - Windows
tags:
  - convert
  - ffmpeg
  - immagini
  - video
---
Esempio:  
`ffmpeg -framerate 1/5 -i C:\shot000%d.png -c:v libx264 -r 30 -pix_fmt yuv420p c:\video.mp4`