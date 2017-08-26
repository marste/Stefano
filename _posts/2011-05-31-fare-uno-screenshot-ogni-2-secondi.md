---
id: 886
title: Fare uno screenshot ogni 2 secondi
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=886
permalink: /fare-uno-screenshot-ogni-2-secondi/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2025957560
categories:
  - Linux
tags:
  - screenshot
  - scrot
---
`sudo apt-get install scrot`  
`i=0;while :; do i=$(expr "$i" + 1); scrot "$i".png; sleep 2; done;`