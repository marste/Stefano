---
title: 'Outlook si blocca quando si clicca su Firma'
date: 2019-06-17 16:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/office.png'
share-img: 'https://marzorati.co/img/office.png'
layout: post
categories:
  - Office365
tags:
  - outlook
  - office
  - Windows 10
  - office365
  - freeze
  - signature
  - blocca
---
Se vi è successo in **Windows 10** che Outlook si blocchi e non apra la finestra delle **firme**, è sufficiente andare in:   
**Installazione Applicazioni** - **App e funzionalità** e rimuovere **Microsoft Office Desktop Apps**   

Per magia tornerà tutto a funzionare!

In alternativa:   

Apri **regedit**

Premi CTRL + F e cerca questa stringa **0006F03A-0000-0000-C000-000000000046** nel search box, poi clicca su **Find Next**.   

Eliminare la chiave trovata.   

Premere **F3** per ripetere la ricerca fino a quando non vengono trovate più chiavi di registro.   
