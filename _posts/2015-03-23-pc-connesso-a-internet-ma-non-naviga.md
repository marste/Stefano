---
id: 3278
title: PC connesso a internet, ma non naviga
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3278
permalink: /pc-connesso-a-internet-ma-non-naviga/
authorsure_include_css:
  - 
video_url:
  - 
quote_content:
  - 
quote_attribution:
  - 
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
