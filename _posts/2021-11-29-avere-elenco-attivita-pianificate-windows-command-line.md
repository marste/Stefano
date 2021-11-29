---
title: Avere un elenco delle attività pianificate di Windows da command line
date: 2021-11-29 08:11:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
layout: post
categories: [Windows]
tags: [elenco, csv, attività, schedulate, pianificate, windows, commandline, remoto, tasks, list]
---
Se vuoi ottenere la lista completa con tutte le informazioni di tutti i tasks che girano su un PC locale, digita:   
~~~batch
schtasks /query /v /fo CSV > tasks.csv
~~~

Se vuoi ottenere la lista di tutti i tasks che girano su un PC remoto, digita:   
~~~batch
schtasks /s <Nome_PC> /query
~~~