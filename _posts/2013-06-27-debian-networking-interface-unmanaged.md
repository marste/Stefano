---
id: 1813
title: 'Debian: Networking interface unmanaged'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1813
permalink: /debian-networking-interface-unmanaged/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
tagazine-media:
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";i:0;s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2013-06-27 07:12:43";}'
  - 'a:7:{s:7:"primary";s:0:"";s:6:"images";a:0:{}s:6:"videos";a:0:{}s:11:"image_count";i:0;s:6:"author";s:6:"116741";s:7:"blog_id";s:8:"21149954";s:9:"mod_stamp";s:19:"2013-06-27 07:12:43";}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1903759490
categories:
  - Linux
tags:
  - debian
  - interface
  - Networking
  - unmanaged
---
Edita:  
`sudo nano /etc/NetworkManager/NetworkManager.conf`

Troverai:  
`[ifupdown]
managed=false`

Cambialo in true:  
`[ifupdown]
managed=true`

Riavvia rete:  
`/etc/init.d/network-manager restart`