---
title: Remotely Terminate a Remote Desktop Session from the Command Line
author: Stefano Marzorati
date: 2015-12-01 17:20:00 -07:00
layout: post
permalink: /remotely-terminate-remote-desktop-session-command-line/
categories:
  - Windows
tags:
  - command-line
  - terminal
  - server
  - remote
  - desktop
  - session
  - remotely
---
Digita il comando:   
	
	qwinsta /server:REMOTESERVER
	
e vedrai la lista degli utenti collegati a questo server con il proprio ID   

Per terminare la sessione dell'utente xxxx che ha ad esempio l'ID numero 4, basterà digitare:   

	rwinsta 4 /server:REMOTESERVER
