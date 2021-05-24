---
title: 'Installare Remote Desktop Services Manager su Windows Server 2016 e Windows 10'
author: Stefano Marzorati
layout: post
date: 2021-05-24 12:45:00 +0200
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories: [Windows]
tags: [find, trova, product, key, windows, wmic]
---
Ti manca il buon vecchio Remote Desktop Services Manager che era presente in Windows Server 2008 R2?   

Il tool che funzionava su Windows 2008 R2 funziona anche su Windows 2012, 2012 R2, 2016 e Windows 10!   

Quindi tutto ciò che devi fare è copiare il file <a href="https://marzorati.co/download/tsadmin.zip" target="_blank">tsadmin.zip</a> ed eseguire i seguenti passaggi:   

Il file zip è composto da 4 files: **tsadmin.msc**, **wts.dll**, **tsadmin.dll** e **tsadmin.reg**   

* Estrai i files in **C:\Windows\System32\**
* Doppio click su **tsadmin.reg** per aggiungere al registro le informazioni richieste per il gestore dei servizi terminal al fine di caricare lo snap-in MMC
* Doppio click su **tsadmin.exe**
