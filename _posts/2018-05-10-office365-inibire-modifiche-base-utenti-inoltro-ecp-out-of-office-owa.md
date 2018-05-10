---
title: Office 365 - Inibire visualizzazione e modifiche della configurazione di base agli utenti
date: 2018-05-10 09:40:00 +0200
author: Stefano Marzorati
image: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
share-img: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
layout: post
categories:
  - Office365
tags:
  - mybaseoptions
  - base
  - inibire
  - office365
  - configurazione
  - inoltro
  - ecp
  - out of office
---
Se volete inibire la possibilità via OWA all'utente finale di poter visualizzare e modificare delle opzioni di base della propria casella di posta (esempio: inoltro delle email, out of office...), basterà andare sul portale di Office365 nella sezione:   

	Autorizzazioni - Ruoli utente - Default Role Assignment Policy

Togliere il flag a **MyBaseOptions**   

Questo ruolo consente ai singoli utenti di visualizzare e modificare la configurazione di base delle loro cassette postali e le impostazioni associate.   

N.B.   
Questo flag disabiliterà anche la possibilità di utilizzare l'ecp (esempio: http://outlook.office365.com/ecp/utente@email.com)
