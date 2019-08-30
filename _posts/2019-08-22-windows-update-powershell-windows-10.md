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
<highlight>Esegui PowerShell *come Administrator*</highlight>
Install-Module PSWindowsUpdate
Set-ExecutionPolicy RemoteSigned
Import-Module PSWindowsUpdate
Get-WUList –MicrosoftUpdate
Get-WUInstall –MicrosoftUpdate –AcceptAll –AutoReboot -Verbose
Get-WindowsUpdate -MicrosoftUpdate -KBArticleID KB4503308 -Verbose
Help Get-WUInstall -full
