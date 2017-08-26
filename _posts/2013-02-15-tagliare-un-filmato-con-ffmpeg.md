---
id: 1398
title: Tagliare un filmato con ffmpeg
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1398
permalink: /tagliare-un-filmato-con-ffmpeg/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:24;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:24;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2046580192
categories:
  - Linux
  - Windows
---
`ffmpeg -vcodec copy -acodec copy -i ~/Desktop/movie.avi -ss 01:41:50.0 -t 00:01:58.0 ~/movie/out4.avi`

Poi se vogliamo convertirlo:  
`ffmpeg -i ~/movie/out4.avi -target pal-dvd -ps 2000000000 -aspect 16:9 ~/movie/output4.mpeg`