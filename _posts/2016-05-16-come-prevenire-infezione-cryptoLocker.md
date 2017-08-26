---
title: Come prevenire l'infezione di CryptoLocker
date: 2016-05-16 15:00:00 +0200
author: Stefano Marzorati
layout: post
permalink: /come-prevenire-infezione-cryptolocker/
categories:
  - Windows
tags:
  - ransomware
  - cryptolocker
  - virus
  - criptare
  - infezione
  - prevenire
  - prevention
---
Questo accorgimento non coprirà tutti i casi degli attuali ransomware, ma almeno il 60%.   
Molte, ma non tutte, versioni di Cryptolocker sfruttano i servizi di crittografia del sistema operativo.   
Infatti coloro che infettano le macchine, sarebbero troppo lenti se criptassero loro i files e in più non avrebbero i privilegi corretti.   

**A livello di domain c'è la possibilità di impedire a chiunque di utilizzare i servizi di crittografia.**   

*To access this configuration in the Default Domain Policy, follow this path once you are editing the GPO in the Group Policy Editor:*   

**Computer Configuration\Windows Settings\Security Settings\Public Key Policies\Encrypting File System**

Clicca su **Proprietà** e seleziona **Don't allow** come da screenshot:   

<p align="center">
  <img src="https://farm8.staticflickr.com/7200/26775798780_813750025c_o.jpg">
</p>   

Per maggiori info:   
<a href="http://www.windowsecurity.com/articles-tutorials/authentication_and_encryption/Controlling-Encrypting-File-System-EFS-Group-Policy.html" target="_blank">http://www.windowsecurity.com/articles-tutorials/authentication_and_encryption/Controlling-Encrypting-File-System-EFS-Group-Policy.html</a>