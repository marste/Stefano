---
title: "Download dig.exe per Windows"
subtitle: Comandi più usati
author: Stefano Marzorati
date: 2022-06-17 08:00:00 +0200
layout: post
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories: [Networking]
tags: [dig, esempio, comandi, usati, dns, query, record]
---
Scarica <a href="https://marzorati.co/download/dig_windows.zip" target="_blank">questo file ZIP</a> e estrai i files in ***C:\Windows\System32***   

Esempi di comandi più usati:   

**Record A**   

	dig marzorati.co

**Tutti i Record DNS**   

	dig marzorati.co ANY

**Record MX**   

	dig marzorati.co MX
	
**Record TXT**   

	dig marzorati.co TXT

**Reverse DNS Lookup**   

	dig +noall +answer -x 8.8.8.8
