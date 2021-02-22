---
title: 'Visualizzare i programmi installati su un PC locale o remoto'
author: Stefano Marzorati
layout: post
date: 2021-02-22 08:20:00 +0200
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Windows]
tags: [programmi, installati, pc, remoto, windows, wmi]
---
Per visualizzare una lista di tutti i programmi installati su un PC locale, basta digitare:   

~~~batch
Get-WmiObject Win32_Product -ComputerName localhost | select Name,Version
~~~

Se vuoi salvare il risultato su un file, ad esempio in C:\TMP\Lista.txt 

~~~batch
Get-WmiObject Win32_Product -ComputerName localhost | select Name,Version > c:\TMP\Lista.txt
~~~

Per visualizzare i programmi installati su un PC remoto, basterà sostituire localhost con il nome del PC remoto:   

~~~batch
Get-WmiObject Win32_Product -ComputerName vigmar | select Name,Version
~~~