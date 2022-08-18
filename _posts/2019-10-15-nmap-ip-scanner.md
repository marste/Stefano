---
title: NMap, IP Scanner, Port Scanner
date: 2019-10-15 12:40:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories:
  - Windows
tags:
  - nmap
  - ip
  - scanner
  - port
  - packet
  - scan
  - commandline
  - search
  - ricerca
---
Ecco alcuni **comandi utili**.   

Per eseguire un ping scan per un indirizzo o una classe:   

	nmap -sn 10.10.50.0/24

Esegue un ping scan più verifica le porte, più comuni, attive:   

	nmap -T4 -F 10.10.50.1

Quick Scan Plus:   

	nmap -sV -T4 -O -F --version-light 10.10.50.1

Mostra tutti i pacchetti inviati e ricevuti:   

	nmap --packet-trace 192.168.1.1

Per fare la scansione solo sulla porta 25 di un indirizzo IP:   

	nmap -p25 192.168.20.25 -o c:\temp\log.txt

Per fare la scansione solo sulla porta 25 di un range di indirizzi IP:   

	nmap -p25 192.168.5.0/24 -o c:\temp\log.txt