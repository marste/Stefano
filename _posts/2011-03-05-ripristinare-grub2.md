---
id: 95
title: Ripristinare grub2
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/ripristinare-grub2
permalink: /ripristinare-grub2/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 8014609777984960921
  - 8014609777984960921
  - 8014609777984960921
categories:
  - Linux
tags:
  - grub
  - Windows
---
Parti con un LiveCD

`sudo fdisk -l`

Poniamo che questo sia il risultato:

`/dev/sda5 8163 13338 41576188+ 83 Linux`  
`/dev/sda6 13339 13452 915673+ 82 Linux swap`

Dobbiamo montare /dev/sda5, cioè l’unica partizione su cui è installata Ubuntu, ovviamente dovrete adattare la procedura nel caso abbiate più partizioni (ad esempio per /boot)

`sudo mount /dev/sda5 /mnt`  
`sudo mount --bind /dev /mnt/dev`  
`sudo mount --bind /proc /mnt/proc`

Adesso dobbiamo effettuare un chroot nella partizione che abbiamo montato in /mnt:

`chroot /mnt`

`grub-install /dev/sda`  
`update-grub`

`exit`  
`sudo umount /mnt/dev`  
`sudo umount /mnt/proc`  
`sudo umount /mnt`  
`reboot`

Potrebbe presentarsi il caso in cui la partizione con Windows non venga rilevata e che sia quindi impossibile avviarla. Per aggirare questo fastidio entriamo nel nostro sistema Ubuntu abituale, installiamo il pacchetto os-prober, usiamolo e ripetiamo le operazioni di prima. Via di terminale:

`sudo apt-get install os-prober`  
`sudo os-prober`  
`sudo update-grub`