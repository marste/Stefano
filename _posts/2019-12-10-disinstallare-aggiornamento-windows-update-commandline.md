---
title: Disinstallare un aggiornamento Windows da command line
date: 2019-12-10 11:51:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
layout: post
categories:
  - Windows
tags:
  - uninstall
  - windows
  - update
  - aggiornamento
  - kb
  - database
  - reset
---
Ecco un esempio:   

	wusa /uninstall /kb:4493435 /quiet /norestart
	wusa /uninstall /kb:4493450 /quiet /norestart
	wusa /uninstall /kb:4493451 /quiet /norestart
	wusa /uninstall /kb:4493446 /quiet /norestart
	wusa /uninstall /kb:4493448 /quiet /norestart
	wusa /uninstall /kb:4493472 /quiet /norestart

e infine riavviare il sistema.

Ovviamente questo comando è possibile lanciarlo anche per disinstallare degli aggiornamento su PC remoti, utilizzando psexec.   
