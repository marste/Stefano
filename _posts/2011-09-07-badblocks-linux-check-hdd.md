---
id: 970
title: Verificare se ci sono settori danneggiati
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=970
permalink: /badblocks-linux-check-hdd/
authorsure_include_css:
  - 
dsq_thread_id:
  - 1957502277
categories:
  - Linux
tags:
  - badblock
  - check
  - danneggiati
  - hdd
  - settori
---
Prendi una distribuzione live di linux (va benissimo ubuntu), l&#8217;avvii, apri il terminal e scrivi:

`sudo badblocks -sv -o log.log /dev/sda`