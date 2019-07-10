---
title: Liberare spazio pulendo la cartella WinSXS
subtitle: Da Windows Server 2012 R2 in poi
date: 2018-06-14 10:47:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories:
  - Windows
tags:
  - cleanup
  - folder
  - windows
  - winsxs
  - spazio
  - liberare
  - pulire
  - server
  - 2012 R2
---
Premi i tasti **Win+R** e scrivi: **taskschd.msc** per aprire **Task Scheduler**   
Vai in questo percorso:   

	Task Scheduler Library\Microsoft\Windows\Servicing

Seleziona il task **StartComponentCleanup** e clicca su **Run** per avviare la pulizia.   

