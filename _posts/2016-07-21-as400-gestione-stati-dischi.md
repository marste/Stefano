---
title: AS/400 - Gestione stati dischi
date: 2016-07-21 11:50:00 +0200
author: Stefano Marzorati
layout: post
permalink: /as400-gestione-stati-dischi/
image: https://marzorati.co/img/ibm.png
share-img: https://marzorati.co/img/ibm.png
categories:
  - AS400
tags:
  - gestione
  - stato
  - disco
  - dischi
  - HDD
  - as400
  - comando
---
Per vedere lo stato dei dischi dell'AS/400, la percentuale in uso, la dimensione e i dati in tempo reale di lettura e scrittura, digita il seguente comando:   

	WRKDSKSTS

Per vedere la dimensione totale dei dischi e lo spazio occupato in percentuale:

	DSPSYSSTS

Per vedere lo spazio occupato da ogni singola libreria, puoi fare una query SQL, ad esempio:

	SELECT * FROM indsk80f ORDER BY IDSIZ desc 