---
title: Dare permessi a leggere calendario su Office365
date: 2016-09-25 16:00:00 +0200
author: Stefano Marzorati
image: 'http://www.fullerton.edu/it/_resources/images/faculty_software_logo/office365_logo.png'
share-img: 'http://www.fullerton.edu/it/_resources/images/faculty_software_logo/office365_logo.png'
layout: post
permalink: /aggiungere-permessi-calendario-office365-powershell/
categories:
  - Office365
tags:
  - aggiungere
  - permessi
  - calendario
  - office365
  - powershell
---
**Connettersi tramite PowerShell a Office365:**   

  - <code>$UserCredential = Get-Credential</code>

  - <code>$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/powershell-liveid/ -Credential $UserCredential -Authentication Basic -AllowRedirection</code>

  - <code>Import-PSSession $Session</code>

**Verificare gli attuali permessi sul Calendario:**   

  - <code>Get-MailboxFolderPermission g.verdi@acme.com:\Calendario</code>

**Aggiungere i permessi in sola lettura all'utente m.rossi@acme.com**   

  - <code>Add-MailboxFolderPermission g.verdi@acme.com:\Calendario -User m.rossi@acme.com -AccessRights Reviewer</code>

**Verificare se l'operazione ha avuto esito positivo:**   

  - <code>Get-MailboxFolderPermission g.verdi@acme.com:\Calendario</code>

**Chudere la sessione:**   

  - <code>Remove-PSSession $Session</code>