---
id: 1023
title: 'Scaricare l&#8217;audio da un video di youtube'
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1023
permalink: /download-audio-youtube-mp3/
tagazine-media:
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2011-11-16 08:18:16";}'
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2011-11-16 08:18:16";}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 2012260331
categories:
  - Linux
tags:
  - audio
  - mp3
  - video
  - youtube
---
Esempio:

`youtube-dl -t --extract-audio --audio-format mp3 http://www.youtube.com/watch?v=BjFSwWlgsXI`

``url="http://www.youtube.com/watch?v=BjFSwWlgsXI";audio=$(youtube-dl -s -e $url);wget -q -O - `youtube-dl -g $url`| ffmpeg -i - -f mp3 -vn -acodec libmp3lame - > "$audio.mp3"``