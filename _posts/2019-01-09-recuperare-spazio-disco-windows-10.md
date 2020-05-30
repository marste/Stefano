---
title: Recuperare spazio disco su Windows 10
date: 2019-01-09 15:40:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories: [Windows]
tags: [spazio, disco, compact, query, always, never, compattare]
---
Per verificare se la modalità Compact OS è attiva:   

	Compact.exe /CompactOS:query
	
Se esce il messaggio: *Il sistema non è nello stato compatto perché Windows ha determinato che non è utile per questo sistema.*   

Vuol dire che non è attiva e può essere attivata con il seguente comando:
	
	Compact.exe /CompactOS:always

Per disabilitarlo:   
	
	Compact.exe /CompactOS:never