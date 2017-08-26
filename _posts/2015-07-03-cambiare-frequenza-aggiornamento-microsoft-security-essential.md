---
title: Cambiare la frequenza di aggiornamento di Microsoft Security Essential
date: 2015-07-03 10:15:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /cambiare-frequenza-aggiornamento-microsoft-security-essential/
categories:
  - software
tags:
  - cambiare
  - frequenza
  - aggiornamento
  - microsoft
  - antivirus
  - security
  - essential
---
Di default, l'antivirus Microsoft Security Essential si aggiorna automaticamente ogni 24 ore.   
Se volete cambiare la frequenza con cui si dovrà aggiornare il vostro antivirus, seguite questi passi:   

  - Apri il Registry Editor con regedit.exe   
  - Vai in: `HKEY_LOCAL_MACHINE/SOFTWARE/Microsoft/Microsoft Antimalware/Signature Updates`   
  - Tasto destro su **Signature Updates** - Autorizzazioni - darsi i permessi di **Controllo completo** per poter modificare la chiave di registro   
  (by default SYSTEM has ownership over that key and won't let any changes be made, to prevent malware from overriding the security settings under a given credential.   
  You have to set the Administrators group as owner, then make the change to allow Administrators Full Control.)   
  - Fai doppio click sulla chiave **SignatureUpdateInterval** e cambia il numero da 1 a 24 in base a ogni quante ore si vuole cambiare la frequenza.   
