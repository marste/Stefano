---
id: 2469
title: Ottimizzare MySQL
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2469
permalink: /ottimizzare-mysql/
layout_key:
  - 
post_slider_check_key:
  - 0
dsq_thread_id:
  - 1910582528
authorsure_include_css:
  - 
categories:
  - Linux
  - Windows
tags:
  - my.cnf
  - mysql
  - optimize
  - ottimizzare
---
Nel mio file /etc/my.cnf ho inserito queste righe:

La lunghezza minima della parola da includere in un FULLTEXT index.  
`ft_min_word_len = 2`

Il numero massimo consentito di connessioni client simultanee.  
`max_connections=500`

Quanti threads il server deve memorizzare nella cache per il riutilizzo.  
`thread_cache_size = 16K`

Se è settato a 1, tutte le istruzioni INSERT, UPDATE, DELETE, e LOCK TABLE WRITE attendono fino a quando non ci sono più dei SELECT o LOCK TABLE READ pendenti sulla tabella interessata.  
`low_priority_updates = 1`

La quantità di memoria allocata per la memorizzazione nella cache dei risultati delle query.  
`query_cache_size = 128M`

Non memorizzare nella cache i risultati che sono più grandi di 4M  
`query_cache_limit = 4M`

Il numero di tabelle aperte per tutti i threads.  
`table_cache = 1K`

Il numero di definizioni di tabella (da file .FRM) che possono essere memorizzati nella cache definita. Se si utilizza un gran numero di tabelle, è possibile creare una cache di grandi dimensioni definizione della tabella per accelerarne l&#8217;apertura.  
`table_definition_cache = 4K`

Il numero di files che il sistema operativo permette a mysqld di aprire.  
`open_files_limit = 3K`

La dimensione del buffer utilizzato per i blocchi di indice.  
`key_buffer = 64M`

Se una query impiega più di questo numero di secondo, il server aumenta le variabili di stato &#8220;slow_queries&#8221;  
`long_query_time = 5`