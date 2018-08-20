---
title: Vedere dimensione casella di posta in PowerShell su Office365
date: 2018-01-29 10:00:00 +0200
author: Stefano Marzorati
image: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
share-img: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
layout: post
categories:
  - Office365
tags:
  - mailbox
  - statistics
  - limit
  - office365
  - powershell
  - total
  - quota
---
**Connettersi tramite PowerShell a Office365:**   

	$UserCredential = Get-Credential
	$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/powershell-liveid/ -Credential $UserCredential -Authentication Basic -AllowRedirection
	Import-PSSession $Session

**Verificare gli attuali permessi:**   

	Get-MailboxStatistics [username] | Format-List StorageLimitStatus,TotalItemSize,TotalDeletedItemSize,ItemCount,DeletedItemCount

**Chudere la sessione:**   

	Remove-PSSession $Session