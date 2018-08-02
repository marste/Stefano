---
layout: post
title: Formula Excel per anteporre degli zero ad una stringa alfanumerica con una lunghezza fissa
date: '2018-08-02 14:00:00 +0200'
published: true
author: Stefano Marzorati
image: 'https://marzorati.co/img/excel.png'
share-img: 'https://marzorati.co/img/excel.png'
categories:
  - Excel
tags:
  - formula
  - zero
  - digit
  - excel
  - concatena
  - ripeti
  - lunghezza
---
Se dovete ottenere una stringa di 6 digit totali e avete delle stringhe più corte e per portarle ad avere 6 digit dovete anteporre degli zero davanti, ecco la formula che fa per voi:   

<code>=CONCATENA(RIPETI(0;6-LUNGHEZZA(A1));A1)</code>

Otterrete un risultato del genere:   

	1234	001234
	12345	012345
	123456	123456
