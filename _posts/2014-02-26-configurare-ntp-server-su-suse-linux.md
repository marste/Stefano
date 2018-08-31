---
id: 2745
title: Configurare NTP Server su SUSE Linux
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/linux.png'
share-img: 'https://marzorati.co/img/linux.png'
permalink: /configurare-ntp-server-su-suse-linux/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2324757684
categories:
  - Linux
tags:
  - data
  - ntp
  - opensuse
  - ora
  - server
  - suse
  - yast
---
Da Terminal:  
`yast`

Seleziona:  
`Network Services`  
`NTP Configuration`

Seleziona:  
`Automatically Start NTP Daemon`  
`During Boot`

Aggiungi:  
`Server`

Inserisci come indirizzo:  
`0.pool.ntp.org`

Fai il test, se è tutto ok, esci da yast.

Per verificare che sia tutto corretto, digita:  
`ntpq -p`