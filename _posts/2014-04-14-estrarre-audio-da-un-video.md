---
id: 2809
title: Estrarre audio da un video
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2809
permalink: /estrarre-audio-da-un-video/
authorsure_include_css:
  - 
categories:
  - Linux
  - Windows
tags:
  - audio
  - extract
  - video
---
Esempio:

`ffmpeg -i c:\video.mp4 -vn -ab 256 c:\audio.mp3`