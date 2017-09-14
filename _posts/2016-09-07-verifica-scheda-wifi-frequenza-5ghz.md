---
title: Verificare se la scheda WiFi supporta la frequenza di 5GHz
date: 2016-09-07 11:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'http://www.capalbio.it/images/wifi.png'
share-img: 'http://www.capalbio.it/images/wifi.png'
permalink: /verifica-scheda-wifi-frequenza-5ghz/
categories:
  - Rete
tags:
  - check
  - compatibility
  - wifi
  - scheda
  - frequenza
  - 5GHz
  - netsh
  - psexec
---
Digita da command prompt:   

	netsh wlan show drivers
	
Controlla la riga *Radio types supported* o *Tipi frequenza radio supportati*   
Se nella lista compare **802.11a** o **802.11ac**  il tuo computer supporta le reti wireless a 5GHz.   

Ad esempio, su questo PC, il risultato è:   
**Tipi frequenza radio supportati  : 802.11b 802.11a 802.11g 802.11n**   
Quindi questo PC supporta il WiFi a 5GHz.   

Se non avete il PC sotto mano e volete controllare un PC remoto, potete digitare il seguente comando:   

	psexec \\nome_pc -u domain\user -p password netsh wlan show drivers
