---
id: 980
title: Convertire files vob ad avi
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=980
permalink: /convert-vob-to-avi/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3334719963
categories:
  - Linux
  - Windows
tags:
  - avi
  - convert
  - ffmpeg
  - vob
---
`ffmpeg -i input.vob -f avi -vcodec libxvid -b 800k -g 300 -bf 2 -acodec libmp3lame -ab 128k -ar 44100 -ac 2 input.avi`