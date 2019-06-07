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
Una volta installata, crea un utente con diritti non amministrativi, elimina tutti i menù che puoi e tutte le icone dal desktop e crea un nuovo launcher per avviare il **Remote Desktop** con i parametri per collegarsi al terminal server.   

Ad esempio:   

	rdesktop -u nome_utente -d dominio -f nome_server:3389

In più se volete non far eliminare l'icona launcher, modificate i permessi su quello shortcut con il comando **sudo chattr +i**

<a target="_blank" href="https://www.amazon.it/gp/search/ref=as_li_qf_sp_sr_tl?ie=UTF8&tag=marzoratiamaz-21&keywords=thin client&index=aps&camp=3414&creative=21718&linkCode=ur2&linkId=8f21ccd1ec63dbdfb8abc4c72368774e">thin client</a><img src="//ir-it.amazon-adsystem.com/e/ir?t=marzoratiamaz-21&l=ur2&o=29&camp=3414" width="1" height="1" border="0" alt="" style="border:none !important; margin:0px !important;" />
