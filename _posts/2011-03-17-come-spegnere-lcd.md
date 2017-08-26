---
id: 377
title: Come spegnere LCD su Linux
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=377
permalink: /come-spegnere-lcd-linux/
tagazine-media:
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2011-03-17 22:53:44";}'
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2011-03-17 22:53:44";}'
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2011-03-17 22:53:44";}'
categories:
  - Linux
---
Se esiste questo file: `cat /proc/acpi/info`   

Allora puoi spegnere l'lcd con questo comando: `xset dpms force off`