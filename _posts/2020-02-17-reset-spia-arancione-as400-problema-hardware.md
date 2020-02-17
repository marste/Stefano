---
title: Reset spia arancione dell'AS/400 quando si è verificato un problema hardware
author: Stefano Marzorati
layout: post
image: https://marzorati.co/img/ibm.png
share-img: https://marzorati.co/img/ibm.png
categories: [AS400]
tags: [spia, gialla, as400, problema, hardware, reset]
---
Il led va spento solo dopo che il problema è risolto mettendo il sistema in condizione di risegnale un eventuale successivo guasto.   

 * Entrare dalla riga comandi in **STRSST** dopo aver recuperato la password dei DST
 * Selezionare il punto **1** (START SERVICE TOOL) e premere invio
 * Selezionare il punto **7** (HARDWARE SERVICE) e premere invio
 * Selezionare il punto **6** (WORK WITH SERVICE ACTION LOG)
 * Si presenterà una videata con delle date. Converrà anticipare di un periodo significativo la data di inizio registrazioni da visualizzare così da avere visualizzati tutte le registrazioni possibili avvenute anche in precedenza poi premere invio.
 * Chiudere tutte le segnalazioni