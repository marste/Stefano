---
title: Robocopy Esempio
date: 2020-06-10 11:20:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories: [Script]
tags: [copia, command line, robocopy, backup, server]
---
Ecco un esempio semplice di utilizzo di Robocopy:   
~~~batch
robocopy "C:\Shared Folders\Home" "\\192.168.1.1\Backup\Giugno_2020\Home" /e /z /r:3 /w:5 /FFT /MT:10  /log+:c:\backup_log.txt
~~~