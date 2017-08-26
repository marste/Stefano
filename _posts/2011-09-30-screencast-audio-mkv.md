---
id: 998
title: Screencast con audio
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=998
permalink: /screencast-audio-mkv/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2135467331
categories:
  - Linux
  - Windows
tags:
  - audio
  - ffmpeg
  - screencast
---
`ffmpeg -f alsa -ac 2 -i pulse -f x11grab -r 30 -s 1280x800 -i :0.0 -acodec pcm_s16le -vcodec libx264 -vpre lossless_ultrafast -threads 0 ./Desktop/mydesktop.mkv`