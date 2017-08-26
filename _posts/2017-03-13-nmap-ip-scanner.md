---
title: NMap, IP Scanner
date: 2017-03-13 17:00:00 +0200
author: Stefano Marzorati
layout: post
permalink: /nmap-ip-scanner/
categories:
  - Windows
tags:
  - nmap
  - ip
  - scanner
  - port
  - packet
  - scan
---
Ecco alcuni **comandi utili**.   

Per eseguire un ping scan per un indirizzo o una classe:   

<code>nmap -sn 10.10.50.0/24</code>

Esegue un ping scan più verifica le porte, più comuni, attive:   

<code>nmap -T4 -F 10.10.50.1</code>

Quick Scan Plus:   

<code>nmap -sV -T4 -O -F --version-light 10.10.50.1</code>

Mostra tutti i pacchetti inviati e ricevuti:   

<code>nmap --packet-trace 192.168.1.1</code>