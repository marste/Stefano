---
id: 907
title: Identificare il file system
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=907
permalink: /identificare-il-file-system/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2027203686
categories:
  - Linux
tags:
  - ext3
  - ext4
  - file system
  - identificare
---
`sudo df -T | awk '{print $1,$2,$NF}' | grep "^/dev"`  
oppure  
`sudo cat /etc/fstab`