---
id: 2828
title: Accellerare o rallentare un video
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2828
permalink: /accellerare-o-rallentare-un-video/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2613146951
categories:
  - Linux
  - Windows
tags:
  - accellerare
  - rallentare
  - velocizzare
  - video
---
Esempio:

`ffmpeg -i c:\input.mp4 -filter:v "setpts=0.125*PTS" c:\output.mp4`

Questo comando farà il video 8x (1/8) più veloce o usa &#8220;setpts = 4 * PTS&#8221; per rendere il video 4x lento.