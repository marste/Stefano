---
id: 77
title: Se il led del wifi del portatile blinka
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/se-il-led-del-wifi-del-portatile-blinka
permalink: /led-wifi-notebook-blink-debian/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 1099199663445866140
  - 1099199663445866140
  - 1099199663445866140
dsq_thread_id:
  - 2232570771
categories:
  - Linux
tags:
  - led
  - notebook
---
Per vedere qual è il modulo:  
`lsmod | grep iwl`

Solitamente il modulo su debian o ubuntu è:

`iwlegacy`

Crea il nuovo file:  
`sudo nano /etc/modprobe.d/wlan.conf`

Aggiungi questa riga:  
`options iwlegacy led_mode=1`

Riavvia il pc