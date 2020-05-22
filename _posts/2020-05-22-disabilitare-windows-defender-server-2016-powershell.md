---
layout: post
title: Disabilitare Windows Defender da Windows Server 2016 via Powershell
date: '2020-05-22 12:30:00 +0200'
author: Stefano Marzorati
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Server]
tags: [Msmpeng.exe, Server, defender, antivirus, installa, disinstalla, powershell]
published: true
---
Per verificare che il servizio di Windows Defender è realmente attivo e in esecuzione, basta digitare:<code>sc query Windefend</code>   

Se vuoi disabilitarlo, fai così:   

* Apri Windows Powershell come administrator
* Digita <code>Uninstall-WindowsFeature -Name Windows-Defender</code>
* Riavvia il server

Se vorrai riabilitare Windows Defender, fai così:   

* Apri Windows Powershell come administrator
* Digita <code>Install-WindowsFeature -Name Windows-Defender</code>
* Riavvia il server