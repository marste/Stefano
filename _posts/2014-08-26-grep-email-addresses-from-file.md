---
id: 3004
title: Grep email addresses from file
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3004
permalink: /grep-email-addresses-from-file/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2959908043
categories:
  - Linux
tags:
  - address
  - email
  - grep
---
Se avete la necessità di trovare tutti gli indirizzi email all&#8217;interno di un file di testo, potete usare il comando grep su linux.

Esempio:  
`grep -E -o "\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,6}\b" /var/tmp/indirizzi.csv > /var/tmp/indirizzi_estratti.csv`

Se avete un messaggio del genere, vuol dire che si tratta di un file binario.

`Binary file /var/tmp/indirizzi.csv matches`

Quindi il comando da digitare diventerà:

`grep -E -o --binary-files=text "\b[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9.-]+\b" /var/tmp/indirizzi.csv > /var/tmp/indirizzi_estratti.csv`