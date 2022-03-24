---
title: Visualizzare l'indice di prestazioni di un PC con Windows 10
date: 2022-03-24 17:15:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories: [Windows]
tags: [windows10, indice, prestazioni, powershell, rating, valutazione]
---
Il comando da digitare in PowerShell come amministratore, è il seguente:   

<code>Get-CimInstance Win32_WinSat</code> oppure   
<code>Get-WmiObject -Class Win32_WinSAT</code>   

L'indice di prestazioni Windows valuta i componenti chiave del sistema, in base ad una **scala da 1,0 a 7,9**   

* CPUScore = prestazioni del processore in calcoli al secondo
* D3DScore = prestazioni grafiche aziendali e di gioco 3D
* DiskScore = velocità di trasferimento dati del disco rigido primario
* Graphicsscore = Prestazioni grafiche grafiche per Windows (Aero)
* MemoryScore = Memoria (RAM) – Operazioni di memoria al secondo
* WinSPRLevel = punteggio totale (risultante dal punteggio più basso)

I numeri rappresentano le prestazioni del rispettivo componente hardware: il punteggio va da **1,0 (scarso) a 9,9 (ottimo)**

Se il punteggio totale è:   

- 2.0 = Computer adatto alle  attività informatiche di base.
- 3.0 = Funzionano gli effetti Aero di base su Windows 7.
- 4.0 = Windows Vista o Windows 7 sono assolutamente compatibili col computer e funzionano senza intoppi in ogni caratteristica.
- 5.0 = Si possono usare le nuove funzionalità di Windows 7 ed il multi-tasking.
- 6.0 = Il computer fa tutto quello che è possibile fare, in modo scattante e senza soffrire.
- 7.0 = Computer di fascia alta su cui possono girare anche programmi di grafica ad alta intensità come anche i videogiochi più moderni.
