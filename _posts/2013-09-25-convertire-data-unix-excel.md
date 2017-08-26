---
id: 2008
title: Convertire data unix in un formato leggibile in excel
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2008
permalink: /convertire-data-unix-excel/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1906913741
categories:
  - Linux
  - Windows
tags:
  - convert
  - data
  - date
  - excel
  - time
  - unix
---
Supponiamo di avere una colonna che riporti delle date in formato Unix, tipo:  
`1380109216`

Mettiamo questo valore nella cella A1, aggiungiamo una colonna e mettiamo questa formula:  
`=(((A1/60)/60)/24)+DATA(1970;1;0,1)`

Il risultato che otterremo sarà:  
`41541,4863`

Ora clicchiamo sulle proprietà di questa cella e gli diciamo che sarà una data, scegliendo il formato  
personalizzato g/m/aa h.mm.ss;@

Il risultato sarà:  
`24/9/13 11.40.00`