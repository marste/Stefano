---
id: 3198
title: Trova files modificati negli ultimi giorni
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3198
permalink: /trova-files-modificati-negli-ultimi-giorni/
authorsure_include_css:
  - 
categories:
  - Linux
tags:
  - files
  - modificati
  - trova
---
Se ad esempio devi trovare dei file modificati fino a 4 giorni da adesso, modifica il 3 con il valore che desideri per la tua ricerca.

`find ./ -type f -mtime -3 -exec ls -al {} \;`