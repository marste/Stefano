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
  - logon
---
Per visualizzare le seguenti informazioni legate ad un account di dominio Windows utilizzata il comando sottostante:   

	NET USER m.rossi /DOMAIN

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

Se vuoi solo sapere quando scadrà la password di un utente, basta digitare:   

	NET USER m.rossi /DOMAIN | FIND /I "Scadenza password"

Se vuoi solo sapere quando è stata cambiata la password di un utente l'ultima volta, basta digitare:   

	NET USER m.rossi /DOMAIN | FIND /I "Ultima impostazione password"

Se vuoi cambiare la password ad un utente, basta digitare:   

	NET USER m.rossi newpassword /DOMAIN

Se vuoi sapere l'ultima volta che l'utente ha fatto logon:   

	NET USER m.rossi /DOMAIN | FIND /I "Ultimo accesso"

-[] punto
-[] punto
-[] punto
