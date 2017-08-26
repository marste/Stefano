---
title: Esporta lista delle dimensioni delle cassette postali in Exchange 2007/2010
date: 2015-07-21 10:21:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /esporta-lista-dimensioni-cassette-postali-exchange-2007-2010/
categories:
  - Software
tags:
  - esporta
  - dimensioni
  - cassette
  - postali
  - exchange
  - shell
  - email
---
Questo è un esempio di esportazione in un file txt, della lista di tutte le caselle di posta presenti sul database mbx01, ordinato per dimensione.   

	Get-Mailbox -Database mbx01 | Get-MailboxStatistics | Sort TotalItemSize -descending | Ft Displayname,TotalItemSize,ItemCount,TotalDeletedItemSize,LastLogonTime > c:\mbx01.txt