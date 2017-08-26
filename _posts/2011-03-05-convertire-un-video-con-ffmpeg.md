---
id: 65
title: Convertire un video con ffmpeg
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/convertire-un-video-con-ffmpeg
permalink: /convertire-un-video-con-ffmpeg/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 7658465244279252903
  - 7658465244279252903
  - 7658465244279252903
geo_public:
  - 0
  - 0
  - 0
dsq_thread_id:
  - 2200961900
authorsure_include_css:
  - 
categories:
  - Linux
tags:
  - convert
  - ffmpeg
---
`ffmpeg -i /home/prova.mov -target pal-dvd -ps 2000000000 -aspect 16:9 /home/test.avi`  
Oppure  
`ffmpeg -i c:\spot.avi -qscale 0 -s 1920x1080 -aspect 16:9 c:\spot_ok.avi`  
`ffmpeg -i in.avi -b 8500k -vcodec libx264 -acodec libfaac -s 720x576 out.avi`