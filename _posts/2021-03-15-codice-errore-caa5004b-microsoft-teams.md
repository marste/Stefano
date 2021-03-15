---
title: '(Solved) Microsoft Teams - Codice di errore: caa5004b'
author: Stefano Marzorati
layout: post
date: 2021-03-15 08:29:00 +0200
image: 'https://marzorati.co/img/teams.png'
share-img: 'https://marzorati.co/img/teams.png'
categories: [Teams]
tags: [error, caa5004b, code, errore, microsoft, teams]
published: true
---

Il problema è legato all'autenticazione che non avviene più.   
Si arriva alla finestra di login, ma la password non viene più chiesta.

Per risolvere velocemente il problema, io ho risolto così:

* Disinstalla Microsoft Teams
* Elimina le due cartelle:

	C:\Users\Utente\appdata\Roaming\Microsoft\Teams

	C:\Users\Utente\appdata\Local\Microsoft\Teams

* Reinstalla Microsoft Teams