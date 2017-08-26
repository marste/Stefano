---
id: 1208
title: Impostare IP statico su Ubuntu Server
date: 2016-01-12 11:44:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /impostare-ip-statico-su-ubuntu-server/
categories:
  - Linux
---
`sudo nano /etc/network/interfaces`   

e dentro modificare come segue:   
	auto lo
	iface lo inet loopback

	auto lo eth0
	iface eth0 inet static
	address 192.168.1.2 #mettere qui l’IP desiderato
	netmask 255.255.255.0 #la netmask della rete
	gateway 192.168.1.1 #il gateway della rete

poi configuri il DNS Server
(se la versione è < 14.04)   

`sudo nano /etc/resolv.conf`   

e dentro modificare come segue:   

	nameserver 212.216.112.112 #dns primario della rete
	nameserver 212.216.172.62 #dns secondario della rete

Riavviare la rete:   
`sudo ifdown eth0 && sudo ifup eth0`

(se la versione è > 14.04)   

`sudo nano /etc/network/interfaces`   

	auto lo eth0
	iface eth0 inet static
	address 192.168.1.2 #mettere qui l’IP desiderato
	netmask 255.255.255.0 #la netmask della rete
	gateway 192.168.1.1 #il gateway della rete
	dns-nameservers 8.8.8.8 #imposti il server dns