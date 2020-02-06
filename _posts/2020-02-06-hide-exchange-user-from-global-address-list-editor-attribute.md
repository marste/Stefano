---
title: Nascondere utente dalla Global Address List
subtitle: Usando l'attribute editor da DC a Exchange Online
author: Stefano Marzorati
date: 2020-02-06 09:15:00 +0200
image: 'https://marzorati.co/img/office.png'
share-img: 'https://marzorati.co/img/office.png'
layout: post
categories:
  - windows
tags:
  - hide
  - exchange
  - gal
  - editor
  - attribute
  - adsync
  - addresslist
---
* Dal Domain Controller, **selezionare l'utente** che non si vuol far comparire nella GAL e andare in **Properties**.   
* Vai nel tab **Attribute Editor**
* Vai nell'attributo **msExchHideFromAddressLists** e metti il valore **TRUE**
* Vai nell'attributo **mailNickname** e scrivi il nome utente prima della @ (Se la mail è **mario.rossi@acme.com**, scrivere **mario.rossi**)
* Avviare la sincronizzazione con il **Synchronization Service** o da PowerShell {% highlight powershell %}Start-ADSyncSyncCycle -PolicyType Delta{% endhighlight %}