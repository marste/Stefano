---
title: PC connesso a internet, ma non naviga
author: Stefano Marzorati
layout: post
date: 2019-05-03 09:00:00 +0200
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
permalink: /pc-connesso-a-internet-ma-non-naviga/
categories:
  - Windows
tags:
  - connesso
  - dns
  - firewall
  - internet
  - naviga
  - reset
  - winsock
---
Il problema è quasi sicuramente legato al DNS.  
Verificate di avere impostato il server DNS corretto, o in alternativa provate a mettere il **DNS di Google** che ha indirizzo **8.8.8.8** e **8.8.4.4**.  
Potrebbe essere che il problema sia proprio legato ad un down del server di Telecom o di altri provider.

In alternativa potete effettuare un reset delle impostazioni e dei parametri di rete, lo svuotamento della cache DNS di Windows ed il ripristino di Windows Firewall.  
**ATTENZIONE** che questa operazione eliminerà le impostazioni relative alle eccezioni impostate in Windows Firewall e quelle relative ad un’eventuale configurazione ad IP statico.

`netsh winsock reset`  
`netsh int ip reset`  
`netsh advfirewall reset`   
`ipconfig /flushdns`   
`ipconfig /release`   
`ipconfig /renew`   