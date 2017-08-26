---
id: 1455
title: Convertire video in gif in alta qualità
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1455
permalink: /convert-video-gif-high-quality/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1927666347
categories:
  - Linux
  - Windows
---
Partendo dal 13° minuto e 56 secondi, estrai per 10 secondi a 10 frame al secondo dei file .png.  
La dimensione delle foto sarà di 350&#215;193. Se ometti questo parametro, terrà le dimensioni originali.  
`ffmpeg -ss 00:13:56 -i C:video.avi -r 10 -t 00:00:10 -s 350x193 c:output%05d.png`

Ora di tutti i file .png crea un unico file .gif  
`converte.exe c:output*.png c:output.gif`