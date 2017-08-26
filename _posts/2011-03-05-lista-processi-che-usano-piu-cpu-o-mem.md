---
id: 39
title: Lista processi che usano più cpu o mem
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/lista-processi-che-usano-piu-cpu-o-mem
permalink: /lista-processi-che-usano-piu-cpu-o-mem/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 3459776518742395239
  - 3459776518742395239
  - 3459776518742395239
categories:
  - Linux
tags:
  - cpu
  - list
  - mem
  - process
---
`ps -eo pcpu,pmem,pid,user,args | sort -k 1 -r | head -10`

oppure

`top -b -n 1 | head -n 15`