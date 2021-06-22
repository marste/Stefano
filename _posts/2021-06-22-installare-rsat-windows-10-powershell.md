---
title: "Installare RSAT (Remote Server Administration Tools) su Windows 10 con PowerShell"
author: Stefano Marzorati
layout: post
redirect_url: https://www.youtube.com/watch?v=TDuXjHDaqeY
date: 2021-06-09 11:05:00 +0200
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Windows]
tags: [installare, rsat, powershell, WindowsCapability]
---
Installare i **Remote Server Administration Tools (RSAT)** sulle ultime versioni di Windows 10.

Mostra la lista dei componenti RSAT che sono disponibili:
~~~powershell
Get-WindowsCapability -Name RSAT* -Online
~~~

Mostra la lista dei componenti RSAT che sono installati o non installati:   
~~~powershell
Get-WindowsCapability -Name RSAT* -Online | Select-Object -Property DisplayName, State
~~~

Installa tutti i componenti RSAT a disposizione:   
~~~powershell
Get-WindowsCapability -Name RSAT* -Online | Add-WindowsCapability -Online
~~~

Mostra la lista dei componenti RSAT che sono installati o non installati:   
~~~powershell
Get-WindowsCapability -Name RSAT* -Online | Select-Object -Property DisplayName, State
~~~