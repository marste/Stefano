---
title: Ricevere allegati XML su Exchange Online di Office 365
date: 2015-04-29 16:30:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /ricevere-allegati-xml-exchange-online/
categories:
  - Software
tags:
  - ricevere
  - allegati
  - xml
  - powershell
  - exchange
  - office365
---
Da PowerShell digitare:   

  - <code>$LiveCred = Get-Credential</code>   

  - <code>$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://ps.outlook.com/powershell/ -Credential $LiveCred -Authentication Basic -AllowRedirection</code>   

  - <code>Import-PSSession $Session</code>   

  - <code>Get-OwaMailboxPolicy | Set-OwaMailboxPolicy -BlockedFileTypes @{Remove = ".xml"}</code>   
  - <code>Get-OwaMailboxPolicy | Set-OwaMailboxPolicy -AllowedFileTypes @{Add = ".xml"}</code>   
  - <code>Get-OwaMailboxPolicy | Set-OwaMailboxPolicy -BlockedMimeTypes @{Remove = "text/xml", "application/xml"}</code>   
  - <code>Get-OwaMailboxPolicy | Set-OwaMailboxPolicy -AllowedMimeTypes @{Add = "text/xml", "application/xml"}</code>   

Le modifiche potranno anche metterci 24 ore prima di essere effettive.   
