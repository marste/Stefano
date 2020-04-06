---
title: "Vedere il Name e il DisplayName di un servizio Windows usando PowerShell"
date: 2020-04-06 10:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [PowerShell]
tags: [Windows, Name, DisplayName, PowerShell, services, servizio, nome, visualizzato]
---
Da PowerShell digitare **Get-Service** per avere la lista completa di tutti i servizi con il proprio nome.   

Esempio per cercare tutti i servizi con display name che iniziano con ***conne...***
{% highlight powershell %}
Get-Service | where {($_.DisplayName -like "conne*")}
{% endhighlight %}

Esempio per cercare tutti i servizi con name che iniziano con ***Spooler...***
{% highlight powershell %}
Get-Service | where {($_.Name -like "Spooler*")}
{% endhighlight %}
