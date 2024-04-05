---
title: Trovare modello e serial number o service tag di un PC remoto
date: 2017-12-29 12:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories:
  - Windows
tags:
  - Windows
  - version
  - wmic
  - command
  - cmd
  - remote
  - computersystem
  - csproduct
  - identifyingnumber
  - serialnumber
  - systemtype
  - vendor
---
Local PC:
	
`wmic csproduct get vendor, name, identifyingnumber`
	
Remote PC:   
	
`psexec \\nome_pc wmic csproduct get vendor, name, identifyingnumber`
	
**Oppure**   

Local PC:   

`wmic bios get serialnumber`
	
Remote PC:   

`psexec \\nome_pc wmic bios get serialnumber`
	
**Se vuoi sapere anche se è a 32 bit o 64 bit, il produttore e il modello**

Local PC:   

`wmic computersystem get model, name, manufacturer, systemtype`
	
Remote PC:   

`psexec \\nome_pc wmic computersystem get model, name, manufacturer, systemtype`