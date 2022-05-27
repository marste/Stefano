---
layout: post
title: Disabilitare o disinstallare Windows Defender da Windows Server 2016 via Powershell
date: '2021-05-27 12:30:00 +0200'
author: Stefano Marzorati
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Server]
tags: [Msmpeng.exe, Server, defender, antivirus, installa, disinstalla, powershell]
published: true
---
Se volete disabilitare il monitor realtime, fai così:

* Apri Windows Powershell come administrator
* Digita: 
~~~powershell
Set-MpPreference -DisableRealtimeMonitoring $true
~~~   
e **riavvia il server**

Se vuoi disinstallarlo, fai così:   

* Apri Windows Powershell come administrator
* Digita: 
~~~powershell 
Uninstall-WindowsFeature -Name Windows-Defender
~~~
* Riavvia il server

Se vorrai reinstallarlo Windows Defender, fai così:   

* Apri Windows Powershell come administrator
* Digita:
~~~powershell 
Install-WindowsFeature -Name Windows-Defender
~~~
* Riavvia il server