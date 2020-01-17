---
title: 'Error [00000524]: L'account specificato esiste già'
subtitle: L'esecuzione del codice non può proseguire perchè psregapi.dll non è stato trovato
date: 2020-01-17 10:47:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/intel.png'
share-img: 'https://marzorati.co/img/intel.png'
categories:
  - Windows
tags:
  - error
  - 00000524
  - specificato
  - account
  - psregapi.dll
  - intel
  - PROSet
  - Wireless
  - uninstall
---
Se dopo un upgrade a Windows 10, all'avvio vi si presenta l'errore:   
> **ifrmewrk.exe**   
> L'esecuzione del codice non può proseguire perchè psregapi.dll non è stato trovato.
> Per risolvere il problema, prova a reinstallare il programma.

Il problema è legato al **Software Intel PROSet/Wireless** che andrebbe disinstallato e reinstallato.   
Peccato che nella maggioranza delle volte, provando a disinstallarlo si ha un altro errore:   

> Error [00000524]: L'account specificato esiste già.

Per risolvere questo altro problema, occorre scaricare e installare l'ultima versione di <a href="https://www.intel.com/content/www/us/en/support/network-and-i-o/wireless-networking/000005634.html?eu-cookie-notice" target="_blank">Intel® PROSet/Wireless Software and Wi-Fi Drivers</a> dal sito Intel (WiFi_21.60.2_Driver64_Win10.exe).   

A questo punto sarà possibile rimuovere il vecchio **Software Intel PROSet/Wireless** e poi reinstallarlo con il driver scaricato dal sito DELL che in alcuni casi potrebbe essere il file **Intel-8260-7265-3165-7260-WiFi-Driver_8K8HC_WIN_20.120.1.970_A28.EXE**
