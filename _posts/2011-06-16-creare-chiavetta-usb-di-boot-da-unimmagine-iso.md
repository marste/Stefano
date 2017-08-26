---
id: 903
title: 'Creare chiavetta usb di boot da un&#8217;immagine iso'
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=903
permalink: /creare-chiavetta-usb-di-boot-da-unimmagine-iso/
tagazine-media:
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2011-06-16 18:55:45";}'
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";s:1:"0";s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2011-06-16 18:55:45";}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 2009789439
categories:
  - Linux
tags:
  - boot
  - dd
  - image
  - iso
  - usb
---
`sudo dd if=/home/nomeutente/nomefile.img |pv|dd of=/dev/sdb bs=10M`