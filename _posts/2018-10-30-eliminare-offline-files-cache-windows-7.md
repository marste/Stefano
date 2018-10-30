---
title: Eliminare gli offline files cache di Windows 7
date: 2018-10-30 12:40:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories:
  - Windows
tags:
  - windows
  - offline
  - files
  - cache
  - eliminare
  - rimuovere
  - delete
---
Apri **REGEDIT** e vai in:   

	HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Csc\Parameters

Crea una nuova **DWORD** chiamata **FormatDatabase** e imposta il valore a *1*   

Questo cancellerà il database dei file offline e cancellerà la chiave di registro creata nel passaggio precedente.   
**Riavviare il PC**.   
