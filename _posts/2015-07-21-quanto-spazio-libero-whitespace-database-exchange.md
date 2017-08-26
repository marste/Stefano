---
title: Quanto spazio libero (whitespace) c'è su ogni mio database Exchange?
date: 2015-07-21 10:45:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /quanto-spazio-libero-whitespace-database-exchange/
categories:
  - Software
tags:
  - whitespace
  - spazio
  - libero
  - database
  - exchange
  - defrag
  - shell
---
Cancellando dei contenuti dalle caselle di posta, questi non liberano spazio sul disco e non fanno diminuire la dimensione dei files dei databases.      
Per vedere quanto spazio andremmo a recuperare su ogni singolo database qualora facessimo un defrag dei db, occorre digitare questo comando:   

	Get-MailboxDatabase -Status | ft name,databasesize,availablenewmailboxspace