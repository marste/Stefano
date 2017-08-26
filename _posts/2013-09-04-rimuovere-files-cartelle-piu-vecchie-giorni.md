---
id: 1951
title: Rimuovere i files e le cartelle piu vecchie di 30 giorni
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1951
permalink: /rimuovere-files-cartelle-piu-vecchie-giorni/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1935521899
categories:
  - Linux
tags:
  - cartelle
  - directory
  - file
  - giorni
  - old
  - rimuovere
  - vecchie
---
Esempio:

`find /home/backup/mysql/* -ctime +30 -delete ;`

Ovviamente se la cartella è più vecchia di 30 giorni, ma il file che è contenuto all&#8217;interno non lo è, la cartella non verrà cancellata.