---
title: Inviare una mail via cURL
author: Stefano Marzorati
layout: post
date: 2019-10-27 12:30:00 +0200
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories:
  - email
tags:
  - smtp
  - curl
  - telnet
  - email
  - test
---
Esempio:  

	curl smtp://mailserver.acme.it -v --mail-from "rossi@gmail.com" --mail-rcpt "verdi@gmail.com" -T "c:\test.txt"
	
Il contenuto del file test.txt, può essere scritto come questo esempio:   

	From: John Smith <john@example.com>
	To: Joe Smith <smith@example.com>
	Subject: an example.com example email
	Date: Mon, 7 Nov 2016 08:45:16
	
	Dear Joe,
	Welcome to this example email. What a lovely day.

