---
id: 22
title: 'IRSSI &#8211; Client IRC'
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/irssi-client-irc
permalink: /irssi-client-irc/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 753029143388612196
  - 753029143388612196
  - 753029143388612196
dsq_thread_id:
  - 1913634399
categories:
  - Linux
  - Windows
tags:
  - add
  - client
  - download
  - irc
  - list
  - remove
---
`sudo apt-get install irssi`  
`/SET dcc_autoget ON` (abilita ricezione automatica dei files)  
`/SET dcc_autoresume ON` (abilita il resume di un file che si è iniziato a scaricare)  
`/SET dcc_download_path /home/marste/Videos` (dove salvare i files scaricati)  
`/DCC LIST` (mostra l&#8217;avanzamento dei download in corso)  
`/SERVER ADD -auto irc.oltreirc.com` (aggiunge un server alla lista dei preferiti e si autoconnette all&#8217;avvio)  
`/SERVER REMOVE irc.oltreirc.com` (rimuove un server dalla lista dei preferiti)  
`/SERVER LIST` (mostra la lista dei canali)  
`/SET autolog ON` (abilita i logs)  
`/SET autolog_path c:\IRSSI\log\$0.log` (percorso dove salvare i logs in Windows)  
`/SET autolog_path /home/marste/log/$0.log` (percorso dove salvare i logs in Linux)  
`xdcc cancel` (interrompe il trasferimento di un download)