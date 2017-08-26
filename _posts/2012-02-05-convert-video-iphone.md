---
id: 1093
title: Convertire video per iPhone
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1093
permalink: /convert-video-iphone/
tagazine-media:
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2012-02-05 17:20:04";}'
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2012-02-05 17:20:04";}'
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"166209493531754496";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"166209493531754496";}}}'
authorsure_include_css:
  - 
categories:
  - Linux
  - Windows
tags:
  - convert
  - iphone
  - video
---
`ffmpeg -i input.avi -f mov -acodec libmp3lame -ab 128k -ar 48000 -ac 2 -vcodec libx264 output.mov`  
`ffmpeg -i input.avi -f mp4 -acodec libfaac -ab 128k -ar 48000 -ac 2 -vcodec libx264 output.mp4`