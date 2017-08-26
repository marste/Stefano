---
id: 1076
title: Disabilitare il plymouth su Fedora 16
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1076
permalink: /how-to-disable-plymouth-f16/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"152030685710917632";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"152030685710917632";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1903091183
categories:
  - Linux
tags:
  - disable
  - fedora
  - plymouth
---
Editare il file:  
`/etc/default/grub`

Editare la riga:  
&#8220;GRUB\_CMDLINE\_LINUX=&#8221; &#8230; &#8221;  
eliminando la parola &#8220;rhgb&#8221;

Poi aggiorna il grub:  
`sudo grub2-mkconfig -o /boot/grub2/grub.cfg`