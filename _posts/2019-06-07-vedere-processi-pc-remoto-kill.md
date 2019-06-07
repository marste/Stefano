---
title: Vedere e terminare i processi di un PC remoto
subtitle: usando TASKLIST e TASKKILL e metterli in un file batch
date: 2019-06-07 13:29:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories:
  - Windows
tags:
  - processes
  - process
  - processi
  - task
  - kill
  - remote
  - tasklist
  - taskkill
---

	TASKLIST /S Nome_PC_Remoto
	
Se lo vuoi mettere in un file .cmd o .bat, scrivi questo, considerando che **%1** è la variabile

	TASKLIST /S %1


	TASKKILL /S Nome_PC_Remoto /IM notepad.exe

Se lo vuoi mettere in un file .cmd o .bat, scrivi questo, considerando che **%1** è la prima variabile e **%2** è la seconda variabile

	TASKKILL /S %1 /IM %2
