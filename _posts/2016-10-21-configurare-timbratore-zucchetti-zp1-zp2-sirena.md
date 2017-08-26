---
title: Configurare un timbratore Zucchetti ZP1 o ZP2 per gestire una sirena
date: 2016-10-21 23:00:00 +0200
author: Stefano Marzorati
layout: post
permalink: /configurare-timbratore-zucchetti-zp1-zp2-sirena/
categories:
  - Hardware
tags:
  - configurazione
  - lettore
  - timbratore
  - zucchetti
  - zp1
  - zp2
  - sirena
  - allarme
---
Se avete l'esigenza di far comandare una sirena o un'allarme da un lettore Zucchetti ZP1 o ZP2, ecco la procedura:

Preparate un file **ALARMS.TXT** con l'orario in cui dovrà suonare la sirena, per quanti secondi e in quali giorni, come nell'esempio sottostante:   

  > 0600,1,10,01111100   
  > 1200,1,10,01111100   
  > 1400,1,10,01111100   
  > 1730,1,10,01111100   
  > 2200,1,10,01111100   

Sintassi: HHMM,R,TT,DLMMGVSF   

**HHMM** = ore e minuti   
**R** = 1 è il relè interno, 2 e 3 sono per relè esterni opzionali   
**TT** = quanti secondi deve suonare la sirena (0 è disattivato - da 1 a 254 secondi disponibili - 255 sempre attiva)   
**DLMMGVSF** = giorni da domenica a sabato più festivi (1 è attivo, 0 disattivo)   

Caricare via FTP il file appena creato nella root del lettore.   
(user e password di default sono: admin)

Dall'interfaccia web del lettore occorrerà modificare il seguente parametro:   

<p align="center">
<img src="https://c1.staticflickr.com/9/8568/30383908911_fcd28cccac_o.png">
</p>   

Questo farà in modo che quando il badge verrà passato sul lettore non chiuderà il contatto del relè e quindi non farà suonare la sirena o non la interromperà quando sta suonando.   
Se invece dovrete usare il timbratore per aprire una porta elettrificata, allora dovrete lasciare il valore 1.   

Fatto questo basterà collegare i due fili della sirena al morsetto **M1** nei contatti **NO** e **COM**, vedi schema elettrico sottostante:   

<p align="center">
<img src="https://c6.staticflickr.com/6/5350/30470754125_1990ed3b08_o.jpg">
</p>   

Per ulteriori informazioni, <a href="http://marzorati.co/download/ZP1-ZP2-Manuale_utente.pdf" target="_blank">clicca qua</a> per il manuale.

