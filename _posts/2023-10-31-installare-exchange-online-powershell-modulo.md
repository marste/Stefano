---
title: "Installare l'Exchange Online Powershell module"
author: Stefano Marzorati
layout: post
date: 2023-10-31 16:00:00 +0200
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Exchange]
tags: [installare, exchange, online, powershell, module, accedere]
---
~~~powershell
Get-Module -ListAvailable -Name ExchangeOnlineManagement
Install-Module -Name ExchangeOnlineManagement -Force
Update-Module ExchangeOnlineManagement
Connect-ExchangeOnline
~~~