---
id: 1704
title: Guardare SkyTG24 con rtmpdump e mplayer
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1704
permalink: /guardare-skytg24-rtmpdump-mplayer/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1940708286
categories:
  - Linux
  - Windows
tags:
  - mplayer
  - rtmp
  - skytg24
---
`rtmpdump -v -r "rtmp://212.243.210.71:1935/live?_fcs_vhost=cp49989.live.edgefcs.net/streamRM1@2564" -q | mplayer -`

Se invece vuoi anche salvare lo streaming mentre lo guardi:

`rtmpdump -v -r "rtmp://212.243.210.71:1935/live?_fcs_vhost=cp49989.live.edgefcs.net/streamRM1@2564" -o  -| mplayer - -dumpstream -dumpfile Skytg24.mpeg`