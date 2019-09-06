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
Esegui PowerShell *come Administrator*

{% highlight powershell %} Install-Module PSWindowsUpdate {% endhighlight %}

{% highlight powershell %} Set-ExecutionPolicy RemoteSigned {% endhighlight %}

Poi

	Import-Module PSWindowsUpdate

Poi

	Get-WUList –MicrosoftUpdate

Poi

	Get-WUInstall –MicrosoftUpdate –AcceptAll –AutoReboot -Verbose

Poi

	Get-WindowsUpdate -MicrosoftUpdate -KBArticleID KB4503308 -Verbose

Esempio

	Help Get-WUInstall -full
