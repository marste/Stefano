---
title: Lista di tutti gli utenti di dominio con scadenza password
date: 2019-07-17 16:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
layout: post
categories:
  - Windows
tags:
  - password
  - scadenza
  - commandline
  - powershell
  - utenti
  - dominio
---
Se utilizzi Windows 10 accertati di aver installato **RSAT (Remote Server Administration Tools)** qualora non lo avessi, lo puoi scaricare dal sito Microsoft:   

<a href="https://www.microsoft.com/it-IT/download/details.aspx?id=45520" target="_blank">Download RSAT (Remote Server Administration Tools)per Windows 10</a> scegliendo quello per Windows Server 2016 (WindowsTH-RSAT_WS2016-x64.msu)   

Una volta installato lanciate da **PowerShell** questo comando:   

	Import-Module ActiveDirectory

Una volta che avete importato i moduli di ActiveDirectory, potete lanciare questo comando:   

	Get-ADUser -filter {Enabled -eq $True -and PasswordNeverExpires -eq $False} –Properties "DisplayName", "msDS-UserPasswordExpiryTimeComputed" | Select-Object -Property "Displayname",@{Name="ExpiryDate";Expression={[datetime]::FromFileTime($_."msDS-UserPasswordExpiryTimeComputed")}} > c:\Temp\Lista.txt

Questa query salverà nel file **Lista.txt** la lista di tutti gli utenti di dominio e la loro scadenza della password.
