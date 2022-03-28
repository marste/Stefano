---
title: "Come collegarsi a Teams via PowerShell"
date: 2022-03-28 08:23:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
layout: post
categories: [Office365]
tags: [collegarsi, teams, powershell, commandline, connect]
---
Installa il modulo PowerShell di Microsoft Teams:   

	Install-Module -Name MicrosoftTeams

Importa il modulo:   

	Import-Module –Name MicrosoftTeams

Collegati con le tue credenziali:   

	Connect-MicrosoftTeams

Ottieni, ad esempio, la lista dei Teams a cui una persona appartiene:   

	Get-Team -User utente@azienda.com

Scollegati:   

	Disconnect-MicrosoftTeams