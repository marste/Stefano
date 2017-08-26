---
id: 972
title: Scaricare musica da GrooveShark con WireShark
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=972
permalink: /download-music-grooveshark-wireshark/
tagazine-media:
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2011-09-09 13:23:49";}'
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2011-09-09 13:23:49";}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 2001995114
categories:
  - Linux
  - Windows
tags:
  - download
  - grooveshark
  - music
  - wireshark
---
Fai partire una canzone da http://grooveshark.com  
Avvia WireShark  
Metti il seguente filtro:  
`http.content_type == "audio/mpeg"`

Uscirà solo una riga  
Tasto destro su &#8220;Media Type&#8221;  
&#8220;Export selected packet bites&#8221;