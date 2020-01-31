---
title: Set default username in Windows 10 with regedit
author: Stefano Marzorati
date: 2020-01-31 11:59:00 +0200
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
  - windows10
  - regedit
---
Se vi siete loggati come **Administrator** su un PC dell'utente per fare manutenzione e poi volete ripristinare l'utente originario con cui si dovrà loggare il proprietario del PC, basta che prima di scollegarvi, cambiate questa chiave di registro:   
	
	HKLM\Software\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\LastLoggedOnUser