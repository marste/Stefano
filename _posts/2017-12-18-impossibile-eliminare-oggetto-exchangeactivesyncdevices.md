---
title: Impossibile eliminare l'oggetto ExchangeActiveSyncDevices
date: 2017-12-18 11:00:00 +0200
author: Stefano Marzorati
image: 'http://www.fullerton.edu/it/_resources/images/faculty_software_logo/office365_logo.png'
share-img: 'http://www.fullerton.edu/it/_resources/images/faculty_software_logo/office365_logo.png'
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

  - <code>$UserCredential = Get-Credential</code>

  - <code>$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/powershell-liveid/ -Credential $UserCredential -Authentication Basic -AllowRedirection</code>

  - <code>Import-PSSession $Session</code>

**Verificare gli attuali permessi:**   

  - <code>Get-Mailbox NomeUtente</code>

**Rimuovere i devices sincronizzati:**   

  - <code>Get-ActiveSyncDevice -Mailbox "indirizzo.email@dominio.com" | Remove-ActiveSyncDevice</code>

**Chudere la sessione:**   

  - <code>Remove-PSSession $Session</code>