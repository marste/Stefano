---
id: 1690
title: Convertire un file m4a in mp3
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1690
permalink: /convert-m4a-sound-file-to-mp3/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1971328911
categories:
  - Linux
  - Windows
---
`ffmpeg -v 5 -y -i input.m4a -acodec libmp3lame -ac 2 -ab 192k output.mp3`