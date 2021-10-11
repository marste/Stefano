---
title: Impossibile eliminare l'oggetto ExchangeActiveSyncDevices
date: 2017-12-18 11:00:00 +0200
author: Stefano Marzorati
image: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
share-img: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
layout: post
permalink: /impossibile-eliminare-oggetto-exchangeactivesyncdevices/
categories:
  - Office365
tags:
  - impossibile
  - eliminare
  - oggetto
  - office365
  - powershell
  - exchange
  - activesync
  - devices
---
**Connettersi tramite PowerShell a Office365:**   

  - <code>Install-Module -Name ExchangeOnlineManagement</code>

  - <code>Import-Module ExchangeOnlineManagement</code>

  - <code>Connect-ExchangeOnline -UserPrincipalName  mioindirizzoemail</code>

**Verificare gli attuali permessi:**   

  - <code>Get-Mailbox NomeUtente</code>

**Rimuovere i devices sincronizzati:**   

  - <code>Get-ActiveSyncDevice -Mailbox "indirizzo.email@dominio.com" | Remove-ActiveSyncDevice</code>

**Chudere la sessione:**   

  - <code>Remove-PSSession $Session</code>