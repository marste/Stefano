---
title: Visualizzare la dimensione e lo stato della quota di una cassetta postale su Office 365
date: 2016-10-17 15:00:00 +0200
author: Stefano Marzorati
layout: post
permalink: /visualizzare-dimensione-quota-cassetta-postale-office365-powershell/
categories:
  - Office365
tags:
  - dimensione
  - quota
  - mailbox
  - office365
  - powershell
  - cassetta
  - visualizzare
---
**Connettersi tramite PowerShell a Office365:**   

* <code>$UserCredential = Get-Credential</code>

* <code>$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/powershell-liveid/ -Credential $UserCredential -Authentication Basic -AllowRedirection</code>

* <code>Import-PSSession $Session</code>

**Comando da eseguire per visualizzare le informazioni che cerchiamo:**   

* <code>Get-MailboxStatistics "Stefano Marzorati" | Format-List StorageLimitStatus,TotalItemSize,TotalDeletedItemSize,ItemCount,DeletedItemCount</code>   

**Chudere la sessione:**   

* <code>Remove-PSSession $Session</code>