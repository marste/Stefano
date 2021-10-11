---
title: Dare permessi di Owner ad un utente su Office365
date: 2017-01-03 14:00:00 +0200
author: Stefano Marzorati
image: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
share-img: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
layout: post
permalink: /aggiungere-permessi-owner-office365-powershell/
categories:
  - Office365
tags:
  - aggiungere
  - permessi
  - owner
  - office365
  - powershell
  - fullaccess
---
**Connettersi tramite PowerShell a Office365:**   

  - <code>Install-Module -Name ExchangeOnlineManagement</code>

  - <code>Import-Module ExchangeOnlineManagement</code>

  - <code>Connect-ExchangeOnline -UserPrincipalName  mioindirizzoemail</code>

**Verificare gli attuali permessi:**   

  - <code>Get-MailboxPermission g.verdi@acme.com</code>

**Aggiungere i permessi di owner all'utente m.rossi@acme.com**   

  - <code>Add-MailboxPermission -Identity g.verdi@acme.com -User m.rossi@acme.com -AccessRights FullAccess</code>

**Verificare se l'operazione ha avuto esito positivo:**   

  - <code>Get-MailboxPermission g.verdi@acme.com</code>

**Chudere la sessione:**   

  - <code>Remove-PSSession $Session</code>