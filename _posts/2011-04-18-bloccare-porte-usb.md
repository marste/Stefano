---
id: 790
title: Bloccare porte USB
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=790
permalink: /bloccare-porte-usb/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2220644819
categories:
  - Linux
tags:
  - blacklist
  - bloccare
  - block
  - modprobe
  - port
  - usb
---
`sudo gedit /etc/modprobe.d/blacklist.conf`  
inserire:  
`# Blocco accesso USB</span>   
<span style="font-family:monospace;">blacklist usb_storage`  
<a href="http://www.edmondweblog.com/index.php/2011/04/18/sicurezza-bloccare-porte-usb/" target="_blank">via</a>