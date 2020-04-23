---
title: "7Zip comprimere un file con lo stesso nome"
subtitle: "Zip file with same originally name"
date: 2020-04-21 10:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories: [Script]
tags: [zip, 7zip, compress, stesso, nome, file, batch, script]
---
Nell'esempio qua di seguito, ci spostiamo nella cartella dove sono presenti dei file **.bak**, li zippiamo con lo stesso nome originale e poi eliminiamo il file .bak

~~~batch
cd D:\MSSQL\Backup\Giornaliero
d:
FOR %%I IN (*.bak) DO "D:\Script\7Z.exe" a %%~nI.zip %%~nI.*
del D:\MSSQL\Backup\Giornaliero\*.bak
~~~
