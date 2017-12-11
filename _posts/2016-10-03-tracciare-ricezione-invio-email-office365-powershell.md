---
title: Tracciare ricezione invio di email su Office365 tramite PowerShell
date: 2016-10-03 15:00:00 +0200
author: Stefano Marzorati
image: 'http://www.fullerton.edu/it/_resources/images/faculty_software_logo/office365_logo.png'
share-img: 'http://www.fullerton.edu/it/_resources/images/faculty_software_logo/office365_logo.png'
layout: post
permalink: /tracciare-ricezione-invio-email-office365-powershell/
categories:
  - Office365
tags:
  - track
  - message
  - tracciare
  - office365
  - powershell
  - invio
  - ricezione
---
**Connettersi tramite PowerShell a Office365:**   

* <code>$UserCredential = Get-Credential</code>

* <code>$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/powershell-liveid/ -Credential $UserCredential -Authentication Basic -AllowRedirection</code>

* <code>Import-PSSession $Session</code>

**Comando da eseguire per effettuare un trace:**   

* <code>Get-MessageTrace -SenderAddress stefano@marzorati.co -StartDate "09/22/2016 00:00:01" -EndDate "10/03/2016 23:59:59"</code>   

oppure

* <code>Get-MessageTrace -RecipientAddress stefano@marzorati.co -StartDate "09/22/2016 00:00:01" -EndDate "10/03/2016 23:59:59"</code>   

Attenzione: all'orario visualizzato nel risultato dovrete aggiungere +2 per questioni di Time Zone.

**Chudere la sessione:**   

* <code>Remove-PSSession $Session</code>