---
title: Ottenere la lista di files con la data di ultima modifica
subtitle: Usando Powershell
date: 2022-04-15 09:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Windows]
tags: [Windows, get, LastWriteTime, export, powershell, Get-ChildItem, Recurse]
---
{% highlight powershell %}
Get-ChildItem -Path "D:\Cartella" -Recurse | Sort-Object -Property LastWriteTime | Select-Object LastWriteTime,FullName |export-csv "C:\TEMP\Last.csv" -NoTypeInformation
{% endhighlight %}
