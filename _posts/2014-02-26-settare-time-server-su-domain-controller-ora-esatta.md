---
title: "Settare Time Server su Domain Controller Windows"
subtitle: Ora esatta
author: Stefano Marzorati
date: 2023-01-27 16:30:00 +0200
layout: post
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories: [Windows]
tags: [time, server, ntp, domain, controller, update, sync]
---
Digitare sul PDC questo comando per impostare una lista di server NTP:   

	w32tm /config /syncfromflags:manual /manualpeerlist:"0.pool.ntp.org 1.pool.ntp.org 2.pool.ntp.org 3.pool.ntp.org"

Per verificare che abbia preso tale lista, digitare:   

	w32tm /query /peers

Per sincronizzare l'ora:   

	w32tm /resync
