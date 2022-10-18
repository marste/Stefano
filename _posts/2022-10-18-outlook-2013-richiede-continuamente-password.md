---
title: "Outlook 2013 richiede continuamente la password"
author: Stefano Marzorati
date: 2022-10-18 10:30:00 +0200
layout: post
image: 'https://marzorati.co/img/outlook.png'
share-img: 'https://marzorati.co/img/outlook.png'
categories: [Office]
tags: [microsoft, office, outlook, richiede, password, continuamente, autenticazione, moderna, ]
---
Se avete Office 2013 e oggi vi accorgete che Outlook continua a chiedervi la password nonostante sia esatta, è tutto normale.   
Office 2013 non è più ufficialmente supportato e tra i vari aggiornamenti ci sono metodologie di autenticazioni più moderne nelle nuove versioni di Office 365.   
Per risolvere il problema occorre passare all'autenticazione moderna facendo delle modifiche nel registro di Windows.   

Andare in:
  
```
HKCU\SOFTWARE\Microsoft\Office\15.0\Common\Identity\
```

Creare una chiave **REG_DWORD** con il nome **EnableADAL** e dargli valore **1**   

Chiudere e riaprire Outlook.