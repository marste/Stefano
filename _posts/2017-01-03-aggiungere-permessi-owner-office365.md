---
title: Dare permessi di Owner ad un utente su Office365
date: 2017-01-03 14:00:00 +0200
author: Stefano Marzorati
image: 'http://www.fullerton.edu/it/_resources/images/faculty_software_logo/office365_logo.png'
share-img: 'http://www.fullerton.edu/it/_resources/images/faculty_software_logo/office365_logo.png'
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

  - <code>$UserCredential = Get-Credential</code>

  - <code>$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/powershell-liveid/ -Credential $UserCredential -Authentication Basic -AllowRedirection</code>

  - <code>Import-PSSession $Session</code>

**Verificare gli attuali permessi:**   

  - <code>Get-MailboxPermission g.verdi@acme.com</code>

**Aggiungere i permessi di owner all'utente m.rossi@acme.com**   

  - <code>Add-MailboxPermission -Identity g.verdi@acme.com -User m.rossi@acme.com -AccessRights FullAccess</code>

**Verificare se l'operazione ha avuto esito positivo:**   

  - <code>Get-MailboxPermission g.verdi@acme.com</code>

**Chudere la sessione:**   

  - <code>Remove-PSSession $Session</code>