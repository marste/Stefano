---
id: 924
title: Trasferire files compressi usando netcat e tar
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=924
permalink: /trasferire-files-compressi-usando-netcat-e-tar/
authorsure_include_css:
  - 
dsq_thread_id:
  - 1916246906
categories:
  - Linux
tags:
  - compressi
  - comprimere
  - netcat
  - tar
  - trasferire
---
Copiare i file di una directory da un server ad un altro eseguendo una compressione prima dell&#8217;invio e una decompressione subito dopo la ricezione.

Per prima cosa si deve predisporre il server di destinazione in ascolto:

`nc -l 8888 | tar xzvf -`

Il server mittente deve invece fare il lavoro inverso e deve conoscere anche l&#8217;IP della macchina di destinazione:

`tar czvf -  | nc  8888`