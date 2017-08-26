---
id: 68
title: Vedere streaming con rtmpdump
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/vedere-streaming-con-rtmpdump
permalink: /vedere-streaming-con-rtmpdump/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 8089633211182771459
  - 8089633211182771459
  - 8089633211182771459
dsq_thread_id:
  - 2099977240
categories:
  - Linux
  - Windows
tags:
  - mplayer
  - rtmp
---
`rtmpdump -v -r rtmp://livestfslivefs.fplive.net/livestfslive-live/ -y "aljazeera_en_high" -a "aljazeeraflashlive-live" -o -| mplayer -`