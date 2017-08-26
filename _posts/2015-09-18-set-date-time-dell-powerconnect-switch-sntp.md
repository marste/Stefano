---
title: Set date and time in DELL PowerConnect Switch with SNTP
author: Stefano Marzorati
date: 2015-09-18 15:30:00 -07:00
layout: post
permalink: /set-date-time-dell-powerconnect-switch-sntp/
categories:
  - Network
tags:
  - DELL
  - PowerConnect
  - NTP
  - server
  - date
  - time
  - sntp
---
La configurazione è stata effettuata su questo modello:   

**PowerConnect 3548**   

Da telnet digitate i seguenti comandi:   

	conf
	sntp unicast client enable
	sntp unicast client poll
	sntp anycast client enable
	sntp broadcast client enable
	sntp server 192.168.20.12 poll
	clock source sntp
	exit
	copy ru st