---
title: Disabilitare i messaggi secondari in Outlook su Office365 da PowerShell
date: 2019-05-09 09:00:00 +0200
author: Stefano Marzorati
image: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
share-img: 'https://images.sftcdn.net/images/t_optimized,f_auto/p/9625aa54-96d0-11e6-aca8-00163ec9f5fa/3338717603/office-online-logo.png'
layout: post
categories:
  - Office365
tags:
  - disabilitare
  - messaggi
  - secondari
  - office365
  - powershell
  - clutter
---
**Connettersi tramite PowerShell a Office365:**   

	$UserCredential = Get-Credential
	$Session = New-PSSession -ConfigurationName Microsoft.Exchange -ConnectionUri https://outlook.office365.com/powershell-liveid/ -Credential $UserCredential -Authentication Basic -AllowRedirection
	Import-PSSession $Session

**Verificare gli attuali permessi(se IsEnabled è True i messaggi secondari sono attivi):**   

	Get-Clutter -Identity mario.rossi@acme.com
	
**Disabilitare i messaggi secondari su una casella di posta:**   

	Set-Clutter -Identity mario.rossi@acme.com -Enable $false

**Disabilitare i messaggi secondari su tutte le caselle di posta:**   

	Get-Mailbox -ResultSize Unlimited | ?{-not (Get-Clutter -Identity $_.Alias).IsEnabled} | %{Set-Clutter -Identity $_.Alias -Enable $false}
	
Questo comando vi permetterà di raccogliere tutte le caselle di posta (Get-Mailbox -ResultSize Unlimited), verificarne lo stato di Clutter (Get-Clutter … .isEnabled) e quindi disattivarlo nel caso questo sia attivato (Set-Clutter … $false)   

**Chudere la sessione:**   

	Remove-PSSession $Session

