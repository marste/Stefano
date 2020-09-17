---
title: Cambia l'ultimo utente loggato su Windows 10 con regedit
author: Stefano Marzorati
date: 2020-09-17 11:59:00 +0200
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
layout: post
categories:
  - windows
tags:
  - default
  - username
  - winlogon
  - logon
  - windows7
  - cambiare
  - utente
  - windows10
  - regedit
---
**In Windows 7**:   

Se vi siete loggati come **Administrator** su un PC dell'utente per fare manutenzione e poi volete ripristinare l'utente originario con cui si dovrà loggare il proprietario del PC, basta che prima di scollegarvi, cambiate questa chiave di registro:   
	
	HKLM\Software\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\LastLoggedOnUser
	
**In Windows 10**:   

	HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI

Devi cambiare tutte e 4 le entries   

	LastLoggedOnDisplayName

Inserisci il nome completo dell'utente, ad esempio **Stefano Marzorati**

    LastLoggedOnSAMUser

Inserisci lo username, ad esempio **DOMAIN\stefano.marzorati**

    LastLoggedOnUser
	
Inserisci ancora lo username, ad esempio **DOMAIN\stefano.marzorati**

    LastLoggedOnUserSID
	
Inserisci il SID dell'utente, ad esempio **S-1-5-21-112783954-3472839473-6329827380-1437**   
Puoi trovare l'esatto SID dell'utente digitando: <code>wmic useraccount where name='stefano.marzorati'</code>

Poi sarà sufficiente fare un logout per verificare di aver cambiato l'ultimo utente loggato.   

