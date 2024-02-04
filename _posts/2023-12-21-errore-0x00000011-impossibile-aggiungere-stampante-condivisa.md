---
title: "Errore 0x00000011b"
subtitle: Impossibile aggiungere una stampante condivisa
date: 2023-12-21 14:35:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
layout: post
categories: [Windows]
tags: [0x00000011b, shared, printer, stampante, condivisa, sicurezza, errore]
---
Dopo l’aggiornamento della KB5005573 si può riscontrare questo errore quando si tenta di aggiungere una stampante condivisa in rete.   
L’aggiornamento KB5005573 rilasciato giorno 17 Settembre 2021 tramite Windows Update risolve un importante rischio chiamato "PrintNightmare", ma causa anche questo errore errore 0x00000011b su Windows.   
Una soluzione rapida per risolvere il problema consiste nell’aggiungere la seguente chiave di registro:

```
KEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Print\
```
aggiungere un Valore REG_DWORD (32) **RpcAuthnLevelPrivacyEnabled** e impostarlo sul valore **0**.

Riavvia il PC e non avrai più l'errore.

<span style="background-color:yellow">!!! Attenzione, l’applicazione di bypass impedisce la protezione contro la vulnerabilità RPC !!!</span>