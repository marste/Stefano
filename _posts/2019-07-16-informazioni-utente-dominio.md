---
title: Informazioni utente di Dominio
date: 2019-07-16 08:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
layout: post
categories:
  - Windows
tags:
  - password
  - scadenza
  - accesso
  - account
  - commandline
  - gruppo
---
Per visualizzare le seguenti informazioni legate ad un account di dominio Windows utilizzata il comando sottostante:   

 - Nome utente
 - Nome completo
 - Account attivo
 - Scadenza account
 - Ultima impostazione password
 - Scadenza password
 - Password cambiabile
 - Password richiesta
 - L'utente può cambiare la password
 - Ultimo accesso
 - Ore di accesso consentito
 - Appartenenze al gruppo locale
 - Appartenenze al gruppo globale

	NET USER m.rossi /DOMAIN   
