---
id: 870
title: Sistemare il plymouth di Ubuntu per NVIDIA
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=870
permalink: /sistemare-il-plymouth-di-ubuntu-per-nvidia/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2227743444
categories:
  - Linux
tags:
  - avvio
  - logo
  - nvidia
  - plymouth
  - startup
  - ubuntu
---
Chi possiede una scheda video NVIDIA, molto probabilmente non vede correttamente il logo di Ubuntu all&#8217;avvio del pc.

Per sistemarlo, ho trovato questa soluzione:

`sudo gedit /etc/default/grub`

Sotto la riga  
`#GRUB_GFXMODE=640x480`

Aggiungi questa riga e salva:  
`GRUB_GFXPAYLOAD_LINUX=1280x800`

Poi digita questi comandi:

`echo "FRAMEBUFFER=y" | sudo tee -a /etc/initramfs-tools/conf.d/splash`  
`sudo update-initramfs -u -k all`  
`sudo update-grub`