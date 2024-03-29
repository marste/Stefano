---
title: Vedere e modificare i giorni per conservare email eliminate in Office 365
date: 2017-03-09 11:00:00 +0200
author: Stefano Marzorati
image: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
share-img: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
layout: post
permalink: /vedere-modificare-giorni-conservare-email-eliminate-cestino-office365/
categories:
  - Office365
tags:
  - vedere
  - modificare
  - giorni
  - office365
  - powershell
  - posta
  - eliminata
  - cestino
  - conservare
  - retaindeleteditemsfor
---
**Connettersi tramite PowerShell a Office365:**   

  - <code>Install-Module -Name ExchangeOnlineManagement</code>

  - <code>Import-Module ExchangeOnlineManagement</code>

  - <code>Connect-ExchangeOnline -UserPrincipalName  mioindirizzoemail</code>

**Verificare il Retain Delete sui vari piani di Exchange:**   

  - <code>Get-MailboxPlan |ft Name,RetainDeletedItemsFor</code>

**Avrete un risultato simile:**   

|                              Name                             | RetainDeletedItemsFor |
|:-------------------------------------------------------------:|:---------------------:|
|  ExchangeOnlineDeskless-c0efa76b-66f6-479e-963c-3e30a808e010  |      14.00:00:00      |
|      ExchangeOnline-2ac40b2e-678a6-4484-a387-b3956b787eee     |      14.00:00:00      |
| ExchangeOnlineEnterprise-bdc01d94-3892-4936-b107-8a0509fae1fd |      14.00:00:00      |
| ExchangeOnlineEssentials-a5fef2a5-49d0-562f-9688-ca797def08ec |      14.00:00:00      |   


**Per modificare il valore dei giorni, ad esempio 30 giorni:**   

  - <code>Get-MailboxPlan | Set-MailboxPlan -RetainDeletedItemsFor 30</code>
  
**Per vedere invece la singola casella postale di un utente:**   

  - <code>Get-Mailbox "Stefano Marzorati" | FL RetainDeletedItemsFor</code>
  
**Per modificare invece la singola casella postale di un utente:**   

  - <code>Set-Mailbox "Stefano Marzorati" -RetainDeletedItemsFor 30.00:00:00</code>
  
**Per invece volete modificare tutte le caselle della vostra orgazizzazione:**     

  - <code>Get-Mailbox -ResultSize unlimited -Filter {(RecipientTypeDetails -eq 'UserMailbox')} | Set-Mailbox -RetainDeletedItemsFor 30</code>
  
**Chudere la sessione:**   

  - <code>Remove-PSSession $Session</code>