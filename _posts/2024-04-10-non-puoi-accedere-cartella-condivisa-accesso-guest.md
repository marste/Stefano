---
title: "Non puoi accedere a questa cartella condivisa perchè i criteri di sicurezza dell'organizzazione bloccano l'accesso guest non autenticato"
subtitle: Questi criteri garantiscono la protezione del PC da dispositivi non sicuri o dannosi nella rete
date: 2024-04-10 14:35:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
layout: post
categories: [Windows]
tags: [accesso, cartella, guest, condivisa, sicurezza, criteri, autenticazione]
---
Se non riesci più ad accedere ad una cartella condivisa, magari di una NAS, dal tuo PC Windows con il seguente messaggio:   

*Non puoi accedere a questa cartella condivisa perchè i criteri di sicurezza dell'organizzazione bloccano l'accesso guest non autenticato.*   
*Questi criteri garantiscono la protezione del PC da dispositivi non sicuri o dannosi nella rete.*

è perchè sono state introdotte delle patch di sicurezza che bloccano questo tipo di accesso.   

Se per qualsiasi motivo, tu voglia bypassare questo controllo e poterci accedere nuovamente, è aggiungere la seguente riga nei registri di Windows:   

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanWorkstation\Parameters
```
aggiungere un Valore REG_DWORD (32) **AllowInsecureGuestAuth** e impostarlo sul valore **1**.   

Non serve riavviare il PC e riprovando potrai nuovamente accedere alla share condivisa.   

<span style="background-color:yellow">!!! Attenzione, l’applicazione di bypass impedisce la protezione contro la vulnerabilità !!!</span>