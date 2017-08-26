---
id: 484
title: Rimuovere un repository da terminal
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=484
permalink: /rimuovere-un-repository-da-terminal/
dsq_thread_id:
  - 2041416756
categories:
  - Linux
tags:
  - ppa
  - repository
  - rimuovere
---
Facciamo l&#8217;esempio che vogliamo togliere il repository di chromium daily, ma non ci ricordiamo il suo nome.

Allora scrivo:

`cat /etc/apt/sources.list /etc/apt/sources.list.d/*`

Avrò una lista e tra questi intravedo:

deb http://ppa.launchpad.net/**chromium-daily/ppa**/ubuntu maverick main

Quindi per eliminarlo dovrò scrivere:

`sudo ppa-purge ppa:chromium-daily/ppa`