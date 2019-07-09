---
title: Windows installer Coordinator in loop infinito
date: 2019-07-09 10:30:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories:
  - Windows
tags:
  - Windows
  - RDP
  - remote
  - desktop
  - coordinator
  - installer
  - loop
---
Se mentre state installando un'applicazione su Terminal Server e vi appare una finestra con il messaggio:   

**Windows installer Coordinator** - **(Attendere. Preparazione dell'applicazione per il primo utilizzo)**   

e attendendo un tempo infinito la situazione non cambia, occorre fare la seguente modifica.   

Aprire *"local group policy editor"* sul server (**gpedit.msc**) e modificare:   

	Computer Configuration\Administrative Templates\Windows Components\Remote Desktop Services\Remote Desktop Session Host\Application Compatibility\

**Turn off Windows Installer RDS Compatibility** e Settarlo a **Enabled**   
