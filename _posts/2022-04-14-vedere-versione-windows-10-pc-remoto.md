---
title: Vedere la versione di Windows 10 di un PC remoto
subtitle: Usando Powershell
date: 2022-04-14 09:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Windows]
tags: [Windows, versione, os, command, line, cmd, remote, version]
---
Local PC:   
{% highlight powershell %}
(Get-WmiObject Win32_OperatingSystem).Version
{% endhighlight %}

Remote PC:   
{% highlight powershell %}
Get-WmiObject Win32_OperatingSystem -ComputerName "Nome_PC" |
Select PSComputerName, Caption, OSArchitecture, Version, BuildNumber | FL
{% endhighlight %}

Oppure potete utilizzare il seguente comando:   

Local PC:   

	systeminfo | findstr /B /C:"Nome SO" /C:"Versione SO"

Remote PC:   

	psexec  \\Nome_PC systeminfo | findstr /B /C:"Nome SO" /C:"Versione SO"
