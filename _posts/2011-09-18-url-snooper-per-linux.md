---
id: 989
title: Url Snooper per Linux
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=989
permalink: /url-snooper-per-linux/
tagazine-media:
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2011-09-18 06:41:32";}'
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2011-09-18 06:41:32";}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1926730883
categories:
  - Linux
tags:
  - grep
  - host
  - media
  - sniff
  - snooper
  - url
  - video
---
Per scoprire le url di video o audio da una pagina web, digita questo comando mentre apri la pagina dalla quale vuoi scaricare il video.  
Vedrai la voce &#8220;host&#8221; e &#8220;url&#8221;, unisci le due e scarica il file.

`sudo ngrep -lqi -p -W none ^get|^post tcp dst port 80 -d eth0 | egrep '(flv|f4v|mp4|m4v|mp3|wmv|mov)'`