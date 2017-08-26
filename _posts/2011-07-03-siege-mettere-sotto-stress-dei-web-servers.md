---
id: 914
title: 'Siege: mettere sotto stress dei web servers'
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=914
permalink: /siege-mettere-sotto-stress-dei-web-servers/
authorsure_include_css:
  - 
categories:
  - Linux
tags:
  - server
  - siege
  - stress
  - tool
  - web
---
`sudo apt-get install siege`  
Eseguire il benchmark del sito http://yourwebsite.com, lanciando 10 connessioni contemporanee al sito, ed eseguendo il test in un ciclo di 3 volte.  
`siege -b -c 10 -r 3 http://yoursite.com`  
Questo simula 30 utenti simultanei, tutti richiedono pagine casuali da un elenco di URL (tratte dal file sitemap.txt ), con un ritardo di 5 secondi dopo ogni pagina (per simulare la lettura della pagina da parte dell’utente). Questo è stato impostato per essere eseguito per 10 minuti.  
`siege -c 30 -i -t 10m -d 5 -f sitemap.txt`  
E’ possibile impostare le opzioni nel file di configurazione /$HOME/.siegerc come ad esempio:  
`/root/.siegercerbose = true   
show-logfile = true   
logging = true   
protocol = HTTP/1.1   
chunked = true   
cache = false   
connection = close   
concurrent = 15   
delay = 1   
accept-encoding = gzip   
spinner = true   
internet = true   
benchmark = true`

<a href="http://linuxaria.com/article/put-your-site-under-siege?lang=it" target="_blank">Fonte</a>