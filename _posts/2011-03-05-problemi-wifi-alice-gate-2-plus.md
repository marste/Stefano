---
id: 94
title: Problemi wifi ALICE GATE 2 Plus
author: Stefano Marzorati
layout: post
image: 'http://marzorati.co/img/wifi.png'
share-img: 'http://marzorati.co/img/wifi.png'
permalink: /problemi-wifi-alice-gate-2-plus/
categories:
  - Linux
---
ALICE GATE 2 Plus Wi-Fi (bianco, bordatura nera, smart card sulla sinistra)  
Funziona con MAC e con Windows ma con Linux si blocca la ricezione dei  
pacchetti dopo pochi kappa&#8230;dopo molti smadonnamenti ho trovato questo:

In pratica basta eseguire uno script al boot (per es. il /etc/rc.local)

	echo 1 > /proc/sys/net/ipv4/tcp_syncookies  
	echo 0 > /proc/sys/net/ipv4/tcp\_window\_scaling  
	echo 0 > /proc/sys/net/ipv4/tcp_ecn

oppure basta aggiungere nel file /etc/sysctl.conf le righe seguenti:

	net.ipv4.tcp_syncookies = 1  
	net.ipv4.tcp\_window\_scaling = 0  
	net.ipv4.tcp_ecn = 0