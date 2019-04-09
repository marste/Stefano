---
title: Error 0x800F0954 installing .NET Framework 3.5
date: 2019-04-09 16:10:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/microsoft.png'
share-img: 'https://marzorati.co/img/microsoft.png'
categories:
  - Windows
tags:
  - errore
  - 0x800F0954
  - windows
  - .net
  - framework
  - immagine
  - ISO
  - dism
---
Se state cercando di abilitare .NET Framework 3.5 e cliccando OK vi compare questo errore:   

**Windows couldn’t complete the requested changes.**   
**The changes couldn’t be completed. Please reboot your computer and try again.**   
**Error code: 0x800F0954**   

Fate così:

- **Monta l'immagine ISO** di Windows 10
- L'immagine verrà montata come disco, ad esempio H:\
- Apri **cmd** con privilegi di administrator

Lancia questo comando:   

	dism /online /enable-feature /featurename:NetFX3 /Source:H:\sources\sxs /LimitAccess