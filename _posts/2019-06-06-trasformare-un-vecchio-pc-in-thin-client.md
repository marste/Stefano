---
title: Trasformare un vecchio PC in Thin Client
date: 2019-06-66 13:00:00 +0200
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
Io ti consiglio **Linux Mint**, in questo periodo è scaricabile la versione **Linux Mint 19.1 Tessa - Cinnamon (32-bit)**.   
Una volta installata, elimina tutti i menù che puoi e tutte le icone dal desktop e crea un nuovo launcher per avviare il **Remote Desktop** con i parametri per collegarsi al terminal server.   

Ad esempio:   

	rdesktop -u nome_utente -d dominio -f nome_server:3389
