---
title: Configurazione Linksys ATA SPA-2102 per spedire Fax
date: 2016-06-01 11:00:00 +0200
author: Stefano Marzorati
layout: post
permalink: /configurare-linksys-ata-spa2102-fax/
categories:
  - Hardware
tags:
  - configurazione
  - linksys
  - ata
  - spa2102
  - fax
  - codec
  - spedire
---
Per resettare l'ATA hai bisogno di un vecchio telefono a tastiera:   

* Plug in power adapter
* Plug in a phone to *Phone 1* port of the SPA-2102
* Dial * * * *
* You should hear *Configuration Option Menu*
* Dial 73738# (RESET#)
* Press 1 to confirm the reset

Oppure   

* Please pick up the phone that is connected to the voip adapter. 
* Then, regardless of if there is a dial tone, dial: * * * * (star 4 times) 
* Then, dial 877778# 
* Then hang up 
* This will reset the adapter back to the default configuration of DHCP 

Qua quasi tutti gli screenshots di una configurazione standard per poter inviare dei fax:   

<p align="center">
<img src="https://c2.staticflickr.com/8/7296/27293057432_0cb747bb80_o.png">
<img src="https://c2.staticflickr.com/8/7053/26784291933_d46033a553_o.png">
<img src="https://c2.staticflickr.com/8/7087/26784291943_f585280e88_o.png">
<img src="https://c2.staticflickr.com/8/7054/26783520454_9711d7706f_o.png">
</p>

**Dial Tone:** 425@-12;10(.6/1/1,.2/.2/1)   
**Busy Tone:** 425@-20;10(.5/.5/1)   
**FXS Port Impedance:** 270+750||150nF   

<p align="center">
<img src="https://c2.staticflickr.com/8/7445/26784291783_6b2322dff9_o.png">
<img src="https://c2.staticflickr.com/8/7075/26783520314_9e33409ed0_o.png">
</p>

**Network Jitter Level:** very high   
**Jitter Buffer Adjustment:** Disable   

<p align="center">
<img src="https://c2.staticflickr.com/8/7063/26784291803_28ff73c0fb_o.png">
<img src="https://c2.staticflickr.com/8/7793/27293057182_15f34fc742_o.png">
<img src="https://c2.staticflickr.com/8/7074/27293057112_aa6ec0bac8_o.png">
</p>   


*Ecco una lista di comandi che potrebbero tornare utili:*   

**Enter Interactive Voice Response Menu**:	* * * *   
**Check net connection type**:	100#   
**Check internet IP address**:	110#   
**Check Network Mask or Subnet Mask**:	120#   
**Check Gateway IP address**:	130#   
**Check MAC Address**:	140#   
**Check Firmware Version**:	150#   
**Check Primary DNS server IP address**:	160#   
**Check web server port**:	170#   
**Check local IP address**:	210#   
**Set internet connection type**:	101#   
**Set static IP address**:	111#   
**Set Network (or Subnet) Mask**:	121#   
**Set Gateway IP Address**:	161#   
**Set the Mode**:	201#   
**Enable/Disable WAN Access to the Web-based Utility**:	7932#   
**Manual Reboot**:	732668   
**Factory Reset**:	73738   
**User Factory Reset**:	877778   


