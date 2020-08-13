---
title: "Come mostrare i secondi nell'orologio della taskbar di Windows 10"
date: 2020-08-13 11:20:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories: [Windows]
tags: [orologio, secondi, taskbar, windows, regedit]
---
 - Vai in:   
~~~batch
HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced
~~~
 - Crea una nuova **DWORD (32-bit) Value** con nome **ShowSecondsInSystemClock** e come valore imposta **1** esadecimale.
 - Disconnettiti e riconnettiti