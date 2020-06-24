---
title: Zippare e Unzippare da Powershell
date: 2020-06-24 15:40:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories: [Powershell]
tags: [zip, unzip, comprimere, espandere, powershell]
---
Esempio per zippare:   

~~~powershell
Compress-Archive -Path C:\Temp\test.doc -DestinationPath C:\Temp\test.zip
~~~

Esempio per unzippare:   

~~~powershell
Expand-Archive -LiteralPath C:\Temp\test.zip -DestinationPath C:\Temp\
~~~