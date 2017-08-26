---
id: 1688
title: Forzare reboot o halt
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1688
permalink: /forzare-reboot-or-halt/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
geo_public:
  - 0
  - 0
authorsure_include_css:
  - 
dsq_thread_id:
  - 1899897494
categories:
  - Linux
tags:
  - force
  - halt
  - Linux
  - reboot
---
**Reboot :**   
`echo 1 > /proc/sys/kernel/sysrq`  
`echo b > /proc/sysrq-trigger`

**Per l’halt:**  
`echo 1 > /proc/sys/kernel/sysrq`  
`echo o > /proc/sysrq-trigger`

Per riavviare in sicurezza:  
   
	Alt+Sysrq+R   
	Alt+Sysrq+E   
	Alt+Sysrq+I   
	Alt+Sysrq+S   
	Alt+Sysrq+U   
	Alt+Sysrq+B   
  
Ricordati: REISUB