---
title: Tracciare email su Exchange da shell
date: 2015-05-29 10:53:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /tracciare-email-excahnge-shell-cmdlet/
categories:
  - Software
tags:
  - get-messagetrackinglog
  - $msgs
  - tracciare
  - exchange
  - shell
  - email
---
Questo è un esempio di tracciamento di tutte le email spedite da stefano@marzorati.co tra le 08.00 del 28/05/2015 alle 23.00 del 28/05/2015 e il risultato sarà salvato in un file html.   

	Get-MessageTrackingLog -Server NomeDelServer -Start "05/28/2015 08:00:00" -End "05/28/2015 23:00:00" -Sender "stefano@marzorati.co" | ConvertTo-Html > "C:\track.html"

Oppure potete usare questo comando:   
	
	$msgs = Get-ExchangeServer | Get-MessageTrackingLog -Sender stefano@marzorati.co -Start "05/28/2015 08:00:00" -End "05/28/2015 23:00:00"   

seguito da questo comando che mostrerà il risultato ordinato per data:   

	$msgs | sort timestamp