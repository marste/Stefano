---
id: 1153
title: 'Disabilitare &#8211; Abilitare AppArmor'
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1153
permalink: /disabilitare-abilitare-apparmor/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"186837480811663360";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"186837480811663360";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1902201602
categories:
  - Linux
tags:
  - abilitare
  - apparmor
  - disabilitare
  - disable
  - enable
  - ubuntu
---
**Per disabilitare:**  
`sudo /etc/init.d/apparmor stop`  
`sudo update-rc.d -f apparmor remove`

**Per riabilitare:**  
`sudo /etc/init.d/apparmor start`  
`sudo update-rc.d apparmor defaults`