---
id: 1015
title: Creare un thumbnail da un video da command line
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1015
permalink: /thumb-video-command-line/
tagazine-media:
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2011-11-01 20:50:52";}'
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2011-11-01 20:50:52";}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 2116349184
categories:
  - Linux
  - Windows
tags:
  - command line
  - screenshot
  - thumb
  - video
---
`ffmpeg -ss 1:00:00 -i /home/marste/Videos/Amici.Di.Letto.avi -vframes 1 -s 320x240 thumb.jpg`