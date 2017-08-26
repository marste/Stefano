---
id: 2884
title: 'Aggiungere un mime-types -gpx- su Apache'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2884
permalink: /aggiungere-un-mime-types-gpx-su-apache/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2824455435
categories:
  - Linux
  - Windows
tags:
  - apache
  - gpx
  - mime.types
---
Se il vostro server Apache non vi permette di scaricare, in questo caso, un file **.gpx**, ma ve lo apre facendo vedere il contenuto xml, occorre verificare i mime.types.

Se la vostra è una macchina Linux, accedete al file:

`/etc/mime.types`

e aggiungete la seguente riga:

`application/gpx+xml	gpx`

**Riavviate Apache** e il problema è risolto.

Se state usando xampp, il file **mime.types** si trova in:

`C:\xampp\apache\conf`