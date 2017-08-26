---
title: Set default username in Windows 7 with regedit
author: Stefano Marzorati
date: 2015-11-05 11:59:00 -07:00
layout: post
permalink: /set-default-username-windows7-regedit/
categories:
  - windows
tags:
  - default
  - username
  - winlogon
  - logon
  - windows7
  - regedit
---
Se vi siete loggati come "Administrator" su un PC dell'utente per fare manutenzione e poi volete ripristinare l'utente originario con cui si dovrà loggare il proprietario del PC, basta che prima di scollegarvi, cambiate questa chiave di registro:   
	
	HKLM\Software\Microsoft\Windows\CurrentVersion\Authentication\LogonUI\LastLoggedOnUser