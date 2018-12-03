---
title: Switch Cisco non risponde al ping
date: 2018-12-03 16:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/cisco.png'
share-img: 'https://marzorati.co/img/cisco.png'
layout: post
categories:
  - Networks
tags:
  - switch
  - Cisco
  - comandi
  - utili
  - vlan
  - porte
  - access
  - trunk
  - ping
---
Accertati che indirizzo IP ha il tuo switch, digitando:   

	sh run

Se nella parte di configurazione dell'interfaccia trovi la riga in cui è scritto l'indirizzo IP con la scritta **shutdown**

	interface Vlan1
	description *** VLAN 1 ***
	ip address 10.10.25.33 255.255.255.0
	shutdown

occorrerà spegnere e riaccendere l'interfaccia vlan1

	conf t
	interface vlan1
	shutdown
	no shutdown

	Digitando nuovamente **sh run** vedrete che l'interfaccia sarà salita e la scritta **shutdown** sarà sparita.
	interface Vlan1
	description *** VLAN 1 ***
	ip address 192.168.25.33 255.255.0.0
	!

Riprovate a pingare ora il vostro switch.