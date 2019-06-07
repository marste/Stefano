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

<iframe style="width:728px;height:90px;" marginwidth="0" marginheight="0" scrolling="no" frameborder="0" src="https://rcm-eu.amazon-adsystem.com/e/cm?ref=qf_sp_asin_til&t=marzoratiamaz-21&m=amazon&o=29&p=8&l=as1&IS2=1&asins=B075RZT2PW&linkId=0672027579fc5b5628b8991ba88231f9&bc1=ffffff&lt1=_blank&fc1=333333&lc1=0066c0&bg1=ffffff&f=ifr">
    </iframe>
