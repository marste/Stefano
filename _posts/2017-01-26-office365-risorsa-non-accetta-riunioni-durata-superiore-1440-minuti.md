---
title: Office 365 - La risorsa non accetta riunioni con durata superiore a 1440 minuti
date: 2017-01-26 17:40:00 +0200
author: Stefano Marzorati
image: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
share-img: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
layout: post
permalink: /office365-risorsa-non-accetta-riunioni-durata-superiore-1440-minuti/
categories:
  - Office365
tags:
  - convocazione
  - riunione
  - rifiutata
  - office365
  - powershell
  - calendario
  - outlook
---
Se state prenotando una meeting room per più giorni e la convocazione della riunione viene rifiutata con il seguente messaggio:   

*La risorsa non accetta riunioni con durata superiore a 1440 minuti.*   

Seguite i seguenti passaggi per estendere o rendere illimitata la durata di una riunione:   

**Connettersi tramite PowerShell a Office365:**   

  - <code>Install-Module -Name ExchangeOnlineManagement</code>

  - <code>Import-Module ExchangeOnlineManagement</code>

  - <code>Connect-ExchangeOnline -UserPrincipalName  mioindirizzoemail</code>

**Verificare gli attuali parametri sulla meeting room:**   

  - <code>Get-CalendarProcessing Sala_Riunioni | fl</code>

**Modificare la massima durata in minuti:**   

  - <code>Set-CalendarProcessing Sala_riunioni -MaximumDurationInMinutes 0</code>

I valori ammessi sono da 0 a 2147483647, se viene settato a 0 la durata massima di una riunione è illimitata.   

**Verificare se l'operazione ha avuto esito positivo:**   

  - <code>Get-CalendarProcessing Sala_Riunioni | fl</code>

**Chudere la sessione:**   

  - <code>Remove-PSSession $Session</code>