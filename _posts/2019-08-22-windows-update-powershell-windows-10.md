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

{% highlight powershell %} Import-Module PSWindowsUpdate {% endhighlight %}

{% highlight powershell %}	Get-WUList –MicrosoftUpdate {% endhighlight %}

{% highlight powershell %}	Get-WUInstall –MicrosoftUpdate –AcceptAll –AutoReboot -Verbose {% endhighlight %}

{% highlight powershell %}	Get-WindowsUpdate -MicrosoftUpdate -KBArticleID KB4503308 -Verbose {% endhighlight %}

Esempio:   

{% highlight powershell %}	Help Get-WUInstall -full {% endhighlight %}
