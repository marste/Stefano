---
id: 2818
title: Aggiungere una immagine ad un file audio
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2818
permalink: /aggiungere-una-immagine-ad-un-file-audio/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2611078639
categories:
  - Linux
  - Windows
tags:
  - audio
  - image
  - immagine
  - mp3
  - youtube
---
Molto utile se volete caricare una traccia audio su youtube.

Esempio:

`ffmpeg -loop 1 -i c:\image.jpg -i c:\audio.mp3 -c:v libx264 -c:a aac -strict experimental -b:a 192k -shortest c:\output.mp4`