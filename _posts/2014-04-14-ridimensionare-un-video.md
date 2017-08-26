---
id: 2813
title: Ridimensionare un video
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2813
permalink: /ridimensionare-un-video/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2611076700
categories:
  - Linux
  - Windows
tags:
  - resize
  - video
---
Esempio:

`ffmpeg -i c:\input.mp4 -s 480x320 -c:a copy c:\output.mp4`