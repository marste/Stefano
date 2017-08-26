---
id: 987
title: Unire più files AVI o FLV
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=987
permalink: /unire-avi-flv-files/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2207662142
categories:
  - Linux
  - Windows
tags:
  - avi
  - film
  - flv
  - join
  - mencoder
  - movie
  - unire
---
`sudo apt-get install transcode transcode-utils`  
`avimerge -i cd1.avi cd2.avi -o cd_completo.avi`  
`mencoder -forceidx -of lavf -oac copy -ovc copy -o video.flv video1.flv video2.flv video3.flv`