---
title: Impossibile connettersi al servizio Servizio di notifica eventi di sistema
subtitle: Windows could not connect to the system event notification service
date: 2019-09-06 09:45:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
layout: post
categories:
  - Windows
tags:
  - impossibile
  - connettersi
  - servizio
  - notifica
  - eventi
  - sistema
---
- Aprire un prompt dei comandi (**cmd.exe**) *con privilegi amministrativi*   
- Digitare il comando: <code>netsh winsock reset</code>   
- Riavviare il computer
