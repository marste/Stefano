---
title: Tracciare invio e ricezione di email fallite su Office365
date: 2016-10-18 15:00:00 +0200
author: Stefano Marzorati
image: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
share-img: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
layout: post
permalink: /tracciare-ricezione-invio-email-email-fallite-office365-powershell/
categories:
  - Office365
tags:
  - tracciare
  - ricezione
  - mailbox
  - office365
  - powershell
  - failed
  - invio
  - track
---
**Connettersi tramite PowerShell a Office365:**   

* <code>$UserCredential = Get-Credential</code>

* <code>$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/powershell-liveid/ -Credential $UserCredential -Authentication Basic -AllowRedirection</code>

* <code>Import-PSSession $Session</code>

**Comando da eseguire per visualizzare le informazioni che cerchiamo:**   

* <code>Get-MessageTrace -SenderAddress stefano@marzorati.co -StartDate "10/17/2016 00:00:01" -EndDate "10/18/2016 23:59:59" | Select-Object Received, SenderAddress, RecipientAddress, Subject, Status, ToIP, FromIP, Size, MessageID, MessageTraceID | Where {$_.Status -eq "Failed"} | Out-GridView</code>   

**Chudere la sessione:**   

* <code>Remove-PSSession $Session</code>