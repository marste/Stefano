---
title: Ottenere la lista di files con la data di ultimo accesso
subtitle: Usando Powershell
date: 2022-04-15 09:05:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Windows]
tags: [Windows, get, LastAccessTime, export, powershell, Get-ChildItem, Recurse]
---
{% highlight powershell %}
Get-ChildItem -Path "D:\Cartella" -Recurse | Sort-Object -Property LastAccessTime | Select-Object LastAccessTime,FullName |export-csv "C:\TEMP\Last.csv" -NoTypeInformation
{% endhighlight %}
