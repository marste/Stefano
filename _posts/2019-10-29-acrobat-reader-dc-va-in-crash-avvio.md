---
title: Acrobat Reader DC va in crash all'avvio
subtitle: Problema sui recent files
date: 2019-10-29 10:50:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/acrobat.png'
share-img: 'https://marzorati.co/img/acrobat.png'
layout: post
categories:
  - Acrobat
tags:
  - acrobat
  - reader
  - crash
  - avvio
  - recenti
  - files
  - regedit
---
Se Acrobat Reader va in crash all'avvio è molto probabile che la causa siano i files aperti di recente che non esistono più nel percorso che si è memorizzato Acrobat nei suoi registri.   

Quindi vi basterebbe eliminare i files recenti di Acrobat, ma se va subito in crash dovete agire nei registri di Windows.   

Aprire **regedit**   

Andare in:   

	HKEY_CURRENT_USER\Software\Adobe\Acrobat Reader\DC\AVGeneral\cRecentFiles

ed eliminare tutte le sottocartelle, esempio c1, c2, c3...   

Una volta fatto questo, potete aprire Acrobat Reader e vedrete che non andrà più in crash.   
Vi consiglio di andare in **Modifica - Preferenze - Documenti** e modificare il *Numero massimo di documenti nell'elenco dei documenti usati di recente*, magari mettendolo a 1.   

