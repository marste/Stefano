---
id: 77
title: Se il led del wifi del portatile blinka
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/se-il-led-del-wifi-del-portatile-blinka
permalink: /led-wifi-notebook-blink-debian/
image: 'http://marzorati.co/img/wifi.png'
share-img: 'http://marzorati.co/img/wifi.png'
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