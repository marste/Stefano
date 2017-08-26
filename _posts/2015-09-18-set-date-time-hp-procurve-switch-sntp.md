---
title: Set date and time in HP ProCurve Switch with SNTP
author: Stefano Marzorati
date: 2015-09-18 15:15:00 -07:00
layout: post
permalink: /set-date-time-hp-procurve-switch-sntp/
categories:
  - Network
tags:
  - HP
  - ProCurve
  - NTP
  - server
  - date
  - time
  - sntp
---
La configurazione è stata effettuata su questi modelli:   

**ProCurve Switch 2510G-48 (J9280A)**   
**ProCurve Switch 2610-48-PWR (J9089A)**   

Da telnet digitate i seguenti comandi:   

	config
	timesync sntp
	sntp server 192.168.20.12
	sntp unicast
	time timezone 60
	time daylight-time-rule western-europe
	end
	show time

La configurazione è stata effettuata su questi modelli:   
	
**ProCurve Switch 2520-8-PoE (J9137A)**   
**HP Switch E2620-24-PPoEP (J9624A)**   

	config
	timesync sntp
	sntp server priority 1 192.168.20.12
	sntp unicast
	time timezone 60
	time daylight-time-rule western-europe
	end
	show time	
