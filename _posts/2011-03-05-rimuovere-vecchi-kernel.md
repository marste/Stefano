---
id: 59
title: Rimuovere vecchi kernel
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/rimuovere-vecchi-kernel
permalink: /rimuovere-vecchi-kernel/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 8900436871909718260
  - 8900436871909718260
  - 8900436871909718260
dsq_thread_id:
  - 2746155954
categories:
  - Linux
tags:
  - kernel
  - rimuovere
---
  - vedi che kernel stai usando   
`uname -r`  

  - lista dei kernel nel grub  
`ls /boot/ | grep initrd`   

  - diventa root   
`sudo -s`   
`apt-get -s remove linux-image-2.6.35-22-generic`   
`apt-get remove  --purge linux-image-2.6.35-22-generic`   

Per il kernel 3.x:   

	sudo apt-get remove $(dpkg -l|awk '/^ii  linux-image-/{print $2}'|sed 's/linux-image-//'|awk -v v=`uname -r` 'v>$0'|sed 's/-generic//'|awk '{printf("linux-headers-%snlinux-headers-%s-genericnlinux-image-%s-genericn",$0,$0,$0)}')