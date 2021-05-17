---
title: Controllo stato della batteria
date: 2021-05-17 07:41:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/battery.png'
share-img: 'https://marzorati.co/img/battery.png'
tags: [controllo, test, check, battery, powercfg, report]
---
Eseguire <code>powercfg -energy</code> come amministratore.   

Verrà generato un file nel percorso <code>C:\WINDOWS\system32\energy-report.html</code>

In questo report occorre trovare le righe **Capacità nominale** e **Ultima carica completa**, che nel mio caso si trova con questi valori:   

	Batteria:Informazioni batteria
	ID batteria 	26045SWD-ATL4.490DELL JG75F0A
	Produttore 	SWD-ATL4.490
	Numero di serie 	26045
	Composizione chimica 	LiP
	Lunga durata 	1
	Sealing eseguito 	0
	Capacità nominale 	68005
	Ultima carica completa 	65877

oppure se in inglese cerca: **Design Capacity** e **Last Full Charge**.   

Dividi l'ultima carica totale con la capacità nominale: 65877/68005=0,9687 moltiplica per 100 = **96,87% efficienza della batteria**
