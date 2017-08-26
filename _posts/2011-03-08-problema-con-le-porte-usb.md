---
id: 127
title: Problema con le porte USB
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/08/problema-con-le-porte-usb
permalink: /problema-con-le-porte-usb/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 2482039675280911995
  - 2482039675280911995
  - 2482039675280911995
categories:
  - Linux
tags:
  - port
  - usb
---
`lspci | grep USB`

`dmesg | grep USB`  
\___\___\___\___\___\_____

`sudo gedit /etc/modules`

e aggiungi alla fine questa riga:

**usb-storage**