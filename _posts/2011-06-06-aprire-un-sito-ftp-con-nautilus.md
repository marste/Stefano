---
id: 896
title: Aprire un sito FTP con Nautilus
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=896
permalink: /aprire-un-sito-ftp-con-nautilus/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2164187618
categories:
  - Linux
tags:
  - ftp
  - gnome
  - nautilus
---
`sudo gedit /etc/gnome/defaults.list`

Aggiungi la seguente linea :  
`x-scheme-handler/ftp=nautilus-folder-handler.desktop`

Salva, chiudi e riavvia