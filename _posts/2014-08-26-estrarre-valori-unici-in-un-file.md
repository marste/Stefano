---
id: 3007
title: Estrarre valori unici in un file
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3007
permalink: /estrarre-valori-unici-in-un-file/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2959983382
categories:
  - Linux
tags:
  - extract
  - file
  - sort
  - unique
  - value
---
Se hai un file con milioni di righe e vorresti estrarre in un altro file solamente i valori unici, potete usare questo comando:

`sort -u /var/tmp/ok_a.csv > /var/tmp/ok_a_unici.csv`

Se vuoi ignorare i case-sensitive, occorre aggiungere l&#8217;opzione -f (ci metterà molto di più)