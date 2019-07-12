---
title: Trasformare un vecchio PC in Thin Client
date: 2019-06-06 13:00:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/linux.png'
share-img: 'https://marzorati.co/img/linux.png'
categories:
  - Linux
tags:
  - trasformare
  - recuperare
  - PC
  - thinclient
  - thin
  - client
  - linux
  - mint
  - rdesktop
  - terminal
  - server
---
Installa una distribuzione Linux che non ti farà impazzire con driver e che è di semplice installazione e configurazione anche per i meno esperti.   
Io ti consiglio **Linux Mint**, in questo periodo è scaricabile la versione **Linux Mint 19.1 "Tessa" - Cinnamon (32-bit)**.   
Una volta installata, crea un utente con diritti non amministrativi, <u>elimina tutte le icone dal desktop</u> e <u>crea un launcher</u> per avviare il **Remote Desktop** con i parametri per collegarsi al terminal server.   
Ti consiglio di **disattivare lo screensaver** o almeno eliminare la richiesta di password dopo il suo sblocco.   

Ad esempio:   

	rdesktop -u nome_utente -d dominio -f nome_server:3389

In più se volete non far eliminare l'icona launcher, modificate i permessi, con l'utenza di root, su quello shortcut con il comando **sudo chattr +i**   
