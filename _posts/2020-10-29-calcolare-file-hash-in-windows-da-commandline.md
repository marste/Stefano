---
layout: post
title: Calcolare file hash in Windows da command line
date: '2020-10-29 12:40:00 +0200'
author: Stefano Marzorati
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories: [Windows]
tags: [hash, file, powershell, algoritmo, commandline, cmd]
published: true
---
Da cmd potete utilizzare il comando **certutil** con la seguente sintassi:
~~~batch
certutil -hashfile c:\Temp\aaa.txt SHA256
~~~
Da PowerShell utilizzare il comando **Get-FileHash** con la seguente sintassi:
~~~powershell
Get-FileHash C:\Temp\aaa.txt -Algorithm SHA256
~~~

L'algoritmo più utilizzato al momento è lo **SHA256**, ma ce ne sono di vari tipi:   

- SHA1
- SHA256
- SHA384
- SHA512
- MACTripleDES
- MD5
- RIPEMD160
