---
title: "Controllare lo stato di salute di un disco SSD o NVMe con Powershell"
author: Stefano Marzorati
date: 2023-01-27 17:30:00 +0200
layout: post
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Powershell]
tags: [disk, powershell, NVMe, health, check, disco, ssd]
---
I miei comandi preferiti per vedere lo stato del mio disco sono:   
~~~powershell
Get-PhysicalDisk | Sort Size | FT FriendlyName, Size, MediaType, SpindleSpeed, HealthStatus, OperationalStatus -AutoSize
~~~
oppure
~~~powershell
Get-PhysicalDisk | Get-StorageReliabilityCounter | ft deviceid, temperature, wear -AutoSize
~~~
**wear** = 0 è ottimo   
**wear** = 100 è il peggio   

Poi scopri il nome del disco con:
~~~powershell
Get-PhysicalDisk | Sort Size | FT FriendlyName
~~~
e digita questo comando sostituendo il nome del disco:   
~~~powershell
Get-PhysicalDisk -FriendlyName 'Nome_del_disco' | Get-StorageReliabilityCounter | Select *
~~~
Poiché si tratta di un disco SSD, i due numeri a cui dovremmo prestare attenzione qui sono **ReadErrorsTotal** e **Wear**.   
<u>Se vedi numeri diversi da 0 visualizzati nelle colonne ReadErrors e wear è meglio sostituirlo.</u>