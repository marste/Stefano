---
id: 2002
title: Convertire video con mencoder
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2002
permalink: /convertire-video-mencoder/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
tagazine-media:
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";i:0;s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2013-09-19 10:37:47";}'
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";i:0;s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2013-09-19 10:37:47";}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1905581799
dsq_needs_sync:
  - 1
categories:
  - Linux
  - Windows
tags:
  - convert
  - convertire
  - mencoder
  - video
---
`mencoder c:\input.flv -oac mp3lame -ovc lavc -o c:\output.avi`  
(partendo da un file di 270 Mb, viene portato a 190 Mb)

`mencoder c:\input.flv -o c:\output.avi -oac mp3lame -lameopts cbr:br=64 -srate 22050 -ovc xvid -xvidencopts fixed_quant=6`  
(partendo da un file di 270 Mb, viene portato a 50 Mb e la qualità è molto simile a quella sopra)

`mencoder c:\input.flv -oac mp3lame -lameopts cbr:mode=2:br=96 -af resample=44100 -srate 44100 -ofps 20 -ovc lavc -lavcopts vcodec=mpeg4:mbd=2:o=mpv_flags=+cbp_rd:trell:vbitrate=300 -ffourcc XVID -o c:\output.avi`  
(partendo da un file di 270 Mb, viene portato a 80 Mb qualità molto simile alle precedenti)

Esempio di conversione DVD:  
`mencoder dvd://1 -vf crop=720:416:0:80,scale=704:304 -ovc xvid -xvidencopts bvhq=1:chroma_opt:quant_type=mpeg:bitrate=658:pass=2 -alang en -oac mp3lame -lameopts br=96:cbr:vol=6 -o output.avi`