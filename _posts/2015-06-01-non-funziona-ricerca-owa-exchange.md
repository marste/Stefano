---
title: Non funziona la ricerca in OWA - Exchange 2010
date: 2015-06-01 09:35:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /non-funziona-ricerca-owa-exchange/
categories:
  - Software
tags:
  - search
  - fulltext
  - owa
  - exchange
  - shell
  - corrupt
---
Se vi siete accorti che su molte caselle di posta non si riesce più ad effettuare la ricerca, occorre verificare se il full-text index catalog è in buono stato o è corrotto.   

Potete eseguire questo test, mettendo l'indirizzo email di una delle persone che ha il problema:   

	Test-ExchangeSearch -Identity john@contoso.com

Se il risultato sarà:   

	ResultFound : False
	SearchTime : -1

Vuol dire che il **full-text index catalog è corrotto**

Per verificare che i database siano indicizzabili:   

	Get-MailBoxDatabase | select name, indexenabled

Per abilitare la ricerca:   

	Set-MailboxDatabase <name> -indexenabled:$true

Per resettare l'indice su un database (il file ResetSearchIndex.ps1 si trova in `C:\Program Files\Microsoft\Exchange Server\V14\Scripts`):   

	ResetSearchIndex.ps1 "Mailbox Database"   

Per resettare l'indice su tutti i database:   

	ResetSearchIndex.ps1 –all