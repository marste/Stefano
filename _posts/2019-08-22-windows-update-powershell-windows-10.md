---
title: Windows Update da Powershell in Windows 10
subtitle: 'usare command line per aggiornare Windows 10'
date: 2019-08-22 23:30:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories:
  - Windows
tags:
  - windowsupdate
  - wuinstall
  - powershell
  - update
  - windowsupdate
---
1)

	Esegui PowerShell *come Administrator*   
2)

	Install-Module PSWindowsUpdate
3)

	Set-ExecutionPolicy RemoteSigned
4)

	Import-Module PSWindowsUpdate
5)

	Get-WUList –MicrosoftUpdate
6)

	Get-WUInstall –MicrosoftUpdate –AcceptAll –AutoReboot -Verbose
7)

	Get-WindowsUpdate -MicrosoftUpdate -KBArticleID KB4503308 -Verbose
	
Lista Esempi:

	Help Get-WUInstall -full
