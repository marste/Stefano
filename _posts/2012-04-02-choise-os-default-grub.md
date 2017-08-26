---
id: 1144
title: Modificare il Sistema Operativo di default del Grub 2
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1144
permalink: /choise-os-default-grub/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"186724900239708160";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"186724900239708160";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1905211552
categories:
  - Linux
tags:
  - grub
  - os
  - scegliere
  - sistema operativo
---
Editare il file grub:  
`sudo gedit /etc/default/grub`  
Cambiare la riga sottostante scegliendo come da immagine:  
`GRUB_DEFAULT=0 </span><span style="font-family:monospace;">   
GRUB_DEFAULT=5`  
[<img class="aligncenter size-medium wp-image-1146" title="Grub_00" src="http://res.cloudinary.com/marzorati-co/image/upload/h_225,w_300/v1408108015/grub_001_n05iq5.png" alt="" />][1]

Aggiornare il Grub:  
`sudo update-grub2`

 [1]: http://ubbunti.files.wordpress.com/2012/04/grub_001.png