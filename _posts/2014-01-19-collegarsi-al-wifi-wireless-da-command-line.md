---
id: 2704
title: Collegarsi al WiFi Wireless da command line
author: Stefano Marzorati
layout: post
image: 'http://www.capalbio.it/images/wifi.png'
share-img: 'http://www.capalbio.it/images/wifi.png'
permalink: /collegarsi-al-wifi-wireless-da-command-line/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2144235341
categories:
  - Windows
tags:
  - command line
  - netsh
  - wifi
  - wireless
---
Per vedere le reti wifi visibili:  
`netsh wlan show networks`

Per collegarsi ad una rete wifi:  
`netsh wlan connect name=NomeRete `

Per vedere i profili salvati sul pc:  
`netsh wlan show profiles`

Per vedere l&#8217;eventuale password in chiaro salvata sul pc:  
`netsh wlan show profile name=NomeRete key=clear`

Per disconnetterti:  
`netsh wlan disconnect`