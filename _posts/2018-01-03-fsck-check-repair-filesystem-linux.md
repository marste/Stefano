---
title: Check and repair a linux corrupted filesystem
date: 2018-01-03 08:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'http://pngimg.com/uploads/linux/linux_PNG2.png'
share-img: 'http://pngimg.com/uploads/linux/linux_PNG2.png'
categories:
  - Linux
tags:
  - check
  - repair
  - filesystem
  - corrupted
  - linux
  - badblock
  - fsck
---
Example:   

Verifica che partizione del disco controllare con:   

`sudo fdisk -l`

Poi lancia uno di questi comandi per verificare se hai dei settori danneggiati.   

`sudo fsck -yvfM /dev/sda1`
	
`sudo fsck -y /dev/sda1`  
		
`sudo fsck -tyfc /dev/sda1`

Con questo tool puoi vedere se ci sono dei messaggi di *pre-fail* nella riga **Current_Pending_Sector**   

`sudo smartctl -a /dev/sda1`
	