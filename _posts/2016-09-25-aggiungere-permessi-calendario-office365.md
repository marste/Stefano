---
title: Dare permessi a leggere calendario su Office365
date: 2016-09-25 16:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/office.png'
share-img: 'https://marzorati.co/img/office.png'
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
  - rimuovere
---
**Connettersi tramite PowerShell a Office365:**   

	Install-Module -Name ExchangeOnlineManagement   

	Import-Module ExchangeOnlineManagement   

	Connect-ExchangeOnline -UserPrincipalName  mioindirizzoemail

**Verificare gli attuali permessi sul Calendario:**   

	Get-MailboxFolderPermission g.verdi@acme.com:\Calendario

**Aggiungere i permessi in sola lettura all'utente m.rossi@acme.com**   

	Add-MailboxFolderPermission g.verdi@acme.com:\Calendario -User m.rossi@acme.com -AccessRights Reviewer

**Verificare se l'operazione ha avuto esito positivo:**   

	Get-MailboxFolderPermission g.verdi@acme.com:\Calendario

**Chudere la sessione:**   

	Remove-PSSession $Session

**Per rimuovere invece un utente:**

	Remove-MailboxFolderPermission -Identity g.verdi@acme.com:\Calendario -User "Mario Rossi"