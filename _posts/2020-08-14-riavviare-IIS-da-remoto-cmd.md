---
title: "Riavviare IIS da remoto"
subtitle: "Restart da command line"
date: 2020-08-14 16:20:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories: [Windows]
tags: [IIS, restart, cmd, remote, commandline]
---
Per visualizzare lo stato di IIS su un server remoto, digitare:    
~~~batch
iisreset nome_server /status
~~~
Il risultato sarà del tipo:
~~~batch
Stato di Windows Process Activation Service ( WAS ) : In esecuzione
Stato di World Wide Web Publishing Service ( W3SVC ) : In esecuzione
~~~

Per riavviare tutti i servizi di IIS, digitare:   
~~~batch
iisreset nome_server /noforce
~~~

oppure:
~~~batch
iisreset nome_server /stop
iisreset nome_server /start
~~~
