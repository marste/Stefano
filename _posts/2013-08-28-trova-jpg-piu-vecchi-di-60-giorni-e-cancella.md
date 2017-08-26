---
id: 1923
title: Trova tutti i files jpg più vecchi di 60 giorni e li cancella
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1923
permalink: /trova-jpg-piu-vecchi-di-60-giorni-e-cancella/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 3314111347
categories:
  - Linux
tags:
  - cancella
  - delete
  - find
  - giorni
  - old
  - trova
  - vecchi
---
Esempio:  
`find /mnt/autofs/nfs/netapp-vol3/cluster/var/www/html/cms-*/cache/gallery/ -name "*.jpg" -type f -mtime +60 -exec rm -f {} ;`