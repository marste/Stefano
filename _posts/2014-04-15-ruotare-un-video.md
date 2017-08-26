---
id: 2825
title: Ruotare un video
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2825
permalink: /ruotare-un-video/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2654029268
categories:
  - Linux
  - Windows
tags:
  - rotate
  - ruotare
  - video
---
Questo comando ruoterà il video di 90° in senso orario:

`ffmpeg -i c:\input.mp4 -filter:v 'transpose=1' c:\rotated-video.mp4`

Questo comando ruoterà il video di 180° in senso antiorario.

`ffmpeg -i c:\input.mp4 -filter:v 'transpose=2,transpose=2' c:\rotated-video.mp4`