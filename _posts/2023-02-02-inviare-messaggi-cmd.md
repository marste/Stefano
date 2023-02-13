---
title: "Inviare un messaggio ad un PC sulla rete locale da cmd"
author: Stefano Marzorati
date: 2023-02-02 07:30:00 +0200
layout: post
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories: [Windows]
tags: [net send, msg, messaggio, lan, check, inviare, cmd]
---
Microsoft Windows fornisce un metodo semplice per inviare messaggi ad altri computer sulla rete locale, chiamato Net Send.   
Ecco un esempio:   

	msg /SERVER:Nome_PC * /TIME:60 "Questo è il messaggio da inviare a Nome_PC che si chiuderà in automatico tra 60 secondi"
