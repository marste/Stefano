---
title: Problema Acer con IP 192.168.0.10
author: Stefano Marzorati
date: 2015-09-08 14:50:00 -07:00
layout: post
permalink: /problema-acer-ip-192.168.0.10/
categories:
  - Networking
tags:
  - acer
  - arp
  - IP
  - 192.168.0.10
  - conflitto
---
Se monitorando la rete scoprite che c'è un device che ha come IP l'indirizzo 192.168.0.10, che magari va in conflitto con qualche altro PC o Server, il problema legato a dei PC Acer collegati alla vostra rete.   
I PC Acer di default hanno abilitato da BIOS l'ASF (Alert Standard Format) che è una tecnologia di gestione client remoto a cui viene associato di default questo IP.   

Per disabilitarlo, basta accedere al BIOS:

	Entra nel BIOS -> Advanced -> Integrated Peripherals
	Seleziona "ASF" per disabilitarlo
	Salva BIOS e riavvia il PC
