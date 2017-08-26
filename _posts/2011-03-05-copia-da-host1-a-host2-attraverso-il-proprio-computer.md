---
id: 49
title: Copia da host1 a host2, attraverso il proprio computer
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/copia-da-host1-a-host2-attraverso-il-proprio-computer
permalink: /copia-da-host1-a-host2-attraverso-il-proprio-computer/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 2303347723917483407
  - 2303347723917483407
  - 2303347723917483407
dsq_thread_id:
  - 2289072601
categories:
  - Linux
tags:
  - copiare
  - copy
---
`ssh root@host1 "cd /somedir/tocopy/ && tar -cf - ." | ssh root@host2 "cd /samedir/tocopyto/ && tar -xf -"`