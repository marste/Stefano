---
id: 668
title: Stampare molti files da terminale
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=668
permalink: /stampare-molti-files-da-terminale/
dsq_thread_id:
  - 1941076442
categories:
  - Linux
tags:
  - files
  - pdf
  - terminal
---
Stampa (con la stampante predefinita) tutti i files .pdf presenti nella directory:

``for i in `ls *.pdf`; do lp $i;done``

Se invece vuoi dirgli il nome della stampante:

``for in in `ls *.pdf`; do lp -d nomestampante $i;done``