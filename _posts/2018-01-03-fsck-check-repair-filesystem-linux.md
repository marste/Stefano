---
title: "Controlla e ripara il filesystem linux corrotto"
date: 2022-08-12 08:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/linux.png'
share-img: 'https://marzorati.co/img/linux.png'
categories: [Linux]
tags: [check, controllare, repair, riparare, fsck, corrotto, filesystem, badblock, blocchi, danneggiati]
---
Esempio:   

Verifica che partizione del disco controllare con:   

`sudo fdisk -l`

Poi lancia uno di questi comandi per verificare se hai dei settori danneggiati.   

`sudo fsck -yvfM /dev/sda1`
	
`sudo fsck -y /dev/sda1`  
		
`sudo fsck -tyfc /dev/sda1`

Con questo tool puoi vedere se ci sono dei messaggi di *pre-fail* nella riga **Current_Pending_Sector**   

`sudo smartctl -a /dev/sda1`
	