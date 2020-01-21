---
title: Find windows OS version from command line
subtitle: Using Powershell
date: 2020-01-21 09:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
permalink: /find-windows-os-version-command-line/
categories:
  - Windows
tags:
  - Windows
  - version
  - OS
  - command
  - cmd
  - remote
  - powershell
---
Local PC:
	
	(Get-WmiObject Win32_OperatingSystem).Version
	
Remote PC:   
	
	Get-WmiObject Win32_OperatingSystem -ComputerName "Nome_PC" |
	Select PSComputerName, Caption, OSArchitecture, Version, BuildNumber | FL

{% highlight powershell %}
Get-WmiObject Win32_OperatingSystem -ComputerName "Nome_PC" |
Select PSComputerName, Caption, OSArchitecture, Version, BuildNumber | FL
{% endhighlight %}