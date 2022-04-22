---
title: Trasformare un vecchio PC in Thin Client
date: 2022-04-22 13:00:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/linux.png'
share-img: 'https://marzorati.co/img/linux.png'
categories: [Linux]
tags: [trasformare, freerdp, recuperare, PC, thinclient, thin, client, linux, mint, lmde, rdesktop, terminal, server]
---
Installa una distribuzione Linux che non ti farà impazzire con driver e che è di semplice installazione e configurazione anche per i meno esperti.   
Io ti consiglio **Linux Mint**, in questo periodo è scaricabile la versione **Linux Mint LMDE 5**.   
Una volta installata, crea un utente con diritti non amministrativi, <u>elimina tutte le icone dal desktop</u> e <u>crea un launcher</u> per avviare il **Remote Desktop** con i parametri per collegarsi al terminal server.   
Ti consiglio di **disattivare lo screensaver** o almeno eliminare la richiesta di password dopo il suo sblocco.   
Installa: **sudo apt-get install freerdp2-x11**   

**Crea uno script eseguibile .sh** da salvare in un percorso che non sia il dekstop, con questi comandi:   

~~~batch
xfreerdp /v:tuo_server /u:$(zenity --entry --title="Utente di Dominio" --text="Inserisci il tuo utente") /p:$(zenity --entry --title="Password di Dominio" --text="Inserisci la tua password" --hide-text) /d:tuo_dominio /f /cert-ignore +clipboard
~~~

A questo punto crea uno shortcut sul desktop che punti a questo script.   

In più se volete non far eliminare l'icona launcher, modificate i permessi, con l'utenza di root, su quello shortcut con il comando **sudo chattr +i**   
