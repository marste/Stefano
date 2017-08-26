---
id: 56
title: Cambiare tempo attesa grub
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/cambiare-tempo-attesa-grub
permalink: /cambiare-tempo-attesa-grub/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 6211133971236777209
  - 6211133971236777209
  - 6211133971236777209
dsq_thread_id:
  - 1922669689
categories:
  - Linux
tags:
  - grub
  - time
---
`cd /etc/default`  
`sudo gedit grub`

modifica la riga con quanti secondi vuoi: GRUB_TIMEOUT=4

poi  
`sudo update-grub`