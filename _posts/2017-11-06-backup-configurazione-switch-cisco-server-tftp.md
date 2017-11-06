---
layout: post
title: Backup della configurazione di uno switch Cisco
date: '2017-11-06 14:00:00 +0200'
author: Stefano Marzorati
image: 'https://farm5.staticflickr.com/4383/36390662603_aa17d0fa81_o.png'
share-img: 'https://farm5.staticflickr.com/4383/36390662603_aa17d0fa81_o.png'
categories:
  - Network
tags:
  - tftp
  - server
  - cisco
  - template
  - commandline
  - backup
published: true
---
Collegarsi allo switch di cui si vuol salvare la configurazione.   

	copy running-config tftp:
	Address or name of remote host []?    
	
Inserire l'indirizzo del server tftp remoto   

	Destination filename [nome dello switch]?   
	
Si può mantenere come nome file, il nome host dello switch, oppure scrivere il nome che si desidera   
Premi ENTER
