---
title: 'IRSSI &#8211; Client IRC'
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/irc.png'
share-img: 'https://marzorati.co/img/irc.png'
permalink: /irssi-client-irc/
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