---
title: "I comandi NSLOOKUP più utilizzati"
date: 2022-03-14 07:53:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
layout: post
categories: [Windows]
tags: [NSLOOKUP, record, NS, MX, SOA, reverse, command]
---
Puoi usare questo comando per vedere quanti record A ci sono e vedere gli indirizzi IP di ciascuno:   

	nslookup example.com

Controllando i record NS, puoi vedere qual è il server autorevole per un dominio specifico:   

	nslookup -type=ns example.com
	
Con questo, puoi vedere l'inizio dell'autorità e ottenere informazioni sulla zona:   

	nslookup -type=soa example.com
	
Con questo puoi controllare gli record MX dei server di posta:   

	nslookup -query=mx example.com
	
Qui vogliamo vedere tutti i record DNS disponibili. Dopo averli visti tutti, possiamo eseguire ricerche specifiche per diversi tipi di record DNS:   

	nslookup -type=any example.com
	
Molte volte controlli i record A per vedere gli IP di un dominio, ma a volte devi verificare se un indirizzo IP è correlato a un dominio specifico. A tale scopo, abbiamo bisogno di una ricerca DNS inversa:   

	nslookup 10.20.30.40

