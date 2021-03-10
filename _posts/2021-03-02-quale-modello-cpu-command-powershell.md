---
title: 'Visualizzare il modello di CPU da Powershell'
author: Stefano Marzorati
layout: post
date: 2021-03-02 08:20:00 +0200
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Windows]
tags: [modello, cpu, processore, remoto, windows, wmi]
---
Per visualizzare il modello di CPU su un PC locale, basta digitare:   

~~~batch
Get-WmiObject Win32_Processor
~~~

Per visualizzare il modello di CPU su un PC remoto, basta digitare:      

~~~batch
Get-WmiObject Win32_Processor -ComputerName nome_pc_remoto
~~~