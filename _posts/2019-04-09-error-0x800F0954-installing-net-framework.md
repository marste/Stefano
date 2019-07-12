---
title: Error 0x800F0954 installing .NET Framework 3.5
date: 2019-07-12 14:10:00 +0200
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
  - 800F0954
  - regedit
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
	
Se però non disponete del file ISO corrispondente alla vostra versione installata, occorre procedere diversamente.   
Siccome il problema è causato da una difficoltà nel reperire i files dalla rete locale attraverso il WSUS, abbiamo due alternative.   

1. Riavviare il PC e loggarsi con un utente locale assicurandosi che non passi attraverso il server WSUS
2. <u>Risolutiva:</u> Digitare <code>regedit.exe</code> e andare nella seguente chiave di registro:   

	HKEY_LOCAL_MACHINE\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU

Modificare la chiave <code>UseWUServer</code> a <code>0</code>   
Riavviare il PC e poi riprovare   
