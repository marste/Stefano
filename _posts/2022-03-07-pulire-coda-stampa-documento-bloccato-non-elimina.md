---
title: "Pulire la coda di stampa quando rimane bloccato un documento"
date: 2022-03-07 08:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/konica.jpeg'
share-img: 'https://marzorati.co/img/konica.jpeg'
categories: [Stampanti]
tags: [spool, stampa, coda, eliminare]
---
Se nella coda di stampa rimane un documento che non viene stampato e non è possibile eliminare, occorre procedere in questo modo:   
Riavviare il servizio **Printer Spooler**

	net stop spooler
	net start spooler

Se non dovesse bastare, una volta stoppato il servizio, elimina il contenuto della seguente cartella:   
	
	del /Q /F /S "%windir%\System32\spool\PRINTERS\*.*"

e poi rifai partire il servizio.