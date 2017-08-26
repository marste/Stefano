---
id: 797
title: GRUB con cursore lampeggiante
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=797
permalink: /grub-con-cursore-lampeggiante/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2028214329
categories:
  - Linux
tags:
  - grub
---
Metti il cd di installazione, anzichè fare l&#8217;install fai il rescue (senza attivare la rete), una volta in rescue scrivi:

`chroot /mnt/sysimage`

poi

`grub-install /dev/sda`

riavvia