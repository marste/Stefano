---
title: Cronologia aggiornamenti installati da Windows Update usando Powershell
date: 2020-01-22 16:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories:
  - Windows
tags:
  - Windows
  - hotfix
  - list
  - security
  - update
  - cmd
  - remote
  - powershell
---
Local PC:   
{% highlight powershell %}
Get-HotFix | Sort-Object installedon
{% endhighlight %}

Remote PC:   
{% highlight powershell %}
Get-HotFix -Description Security* -ComputerName Nome_PC1, Nome_PC2 -Credential Dominio\Admin | Sort-Object installedon
{% endhighlight %}

Se vuoi tutti gli update installati e senza dover passare le credenziali del domnio, puoi anche semplicemente scrivere:   
{% highlight powershell %}
Get-HotFix -CN Nome_PC1 | Sort-Object installedon
{% endhighlight %}
