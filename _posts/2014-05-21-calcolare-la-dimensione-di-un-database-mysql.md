---
id: 2857
title: Calcolare la dimensione di un database MySQL
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2857
permalink: /calcolare-la-dimensione-di-un-database-mysql/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2701803283
categories:
  - Linux
  - Windows
tags:
  - database
  - dimensione
  - mysql
---
`SELECT COUNT(table_name) AS NumeroTabelle, SUM(data_length + index_length) AS Dimensione FROM information_schema.TABLES WHERE table_schema = 'nome_database';`

Il valore ottenuto sarà in **byte**

Esempio:  
12145033216 byte

Se vuoi sapere in Gb, occorre dividere per:  
1073741824 che equivale a (1024\*1024\*1024)

**12145033216/1073741824 = 11,31 Gb**