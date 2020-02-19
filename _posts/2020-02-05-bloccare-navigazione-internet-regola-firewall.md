---
title: Bloccare la navigazione internet su Windows 10
subtitle: Attraverso una regola sul Firewall Windows
author: Stefano Marzorati
date: 2020-02-05 13:51:00 +0200
image: 'https://marzorati.co/img/firewall.png'
share-img: 'https://marzorati.co/img/firewall.png'
layout: post
categories:
  - windows
tags:
  - firewall
  - bloccare
  - navigazione
  - internet
  - regola
  - rule
---
Per bloccare la possibilità di navigare in Internet da un PC, magari non facente parte di un dominio, è possibile creare una regola sul firewall di Windows.   

Andate in:   
* Windows Firewall con sicurezza avanzata (accedere come amministratore)
* Regole connessioni in uscita
* Nuova Regola
* Porta
* TCP
* Porte Remote 80, 443
* Blocca la connessione
* Dominio - Privato - Pubblico
* Dare un nome alla regola

Se invece avete bisogno che qualche eseguibile si colleghi ad Internet (esempio antivirus per aggiornarsi), potete decidere di bloccare i browser.

Andate in:   
* Windows Firewall con sicurezza avanzata (accedere come amministratore)
* Regole connessioni in uscita
* Nuova Regola
* Programma
* Percorso del browser (IE, Edge, Chrome, Firefox)
* Blocca la connessione
* Dominio - Privato - Pubblico
* Dare un nome alla regola