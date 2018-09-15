---
layout: post
title: Backup della configurazione di uno switch Cisco
date: '2017-11-06 14:00:00 +0200'
author: Stefano Marzorati
image: 'https://marzorati.co/img/cisco.png'
share-img: 'https://marzorati.co/img/cisco.png'
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
	
Inserire l'indirizzo del server tftp remoto (esempio: 192.168.20.12)   

	Destination filename [nome dello switch]?
	
Si può mantenere come nome file, il nome host dello switch, oppure scrivere il nome che si desidera   
Premi ENTER
