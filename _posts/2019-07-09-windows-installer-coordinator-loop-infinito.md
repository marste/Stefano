---
title: Windows installer Coordinator
subtitle: Attendere. Preparazione dell'applicazione per il primo utilizzo
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
  - wait
  - first
  - use
  - application
---
Se mentre state installando un'applicazione su Terminal Server e vi appare una finestra con il messaggio:   

**Windows installer Coordinator** - **(Attendere. Preparazione dell'applicazione per il primo utilizzo)** o in inglese **(Please wait while the application is preparing for the first use)**   

e attendendo un tempo infinito la situazione non cambia, occorre fare la seguente modifica.   

Aprire ***local group policy editor*** sul server (**gpedit.msc**) e modificare:   

	Computer Configuration\Administrative Templates\Windows Components\Remote Desktop Services\Remote Desktop Session Host\Application Compatibility\

**Turn off Windows Installer RDS Compatibility** e Settarlo a **Enabled**   

<span style="background-color:colore_testo">Turn off Windows Installer RDS Compatibility</span>
<span style="background-color:yellow">Turn off Windows Installer RDS Compatibility</span>  e Settarlo a **Enabled**   
