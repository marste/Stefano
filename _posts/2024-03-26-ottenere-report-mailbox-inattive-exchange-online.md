---
title: "Come ottenere un report sulle caselle di posta inattive di Exchange Online con PowerShell"
date: 2024-03-26 17:22:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
layout: post
categories: [Office365]
tags: [microsoft, 365, report, exchange, posta, inactive, powershell, inattive, mailbox]
---
~~~powershell
Connect-ExchangeOnline -UserPrincipalName indirizzo_email
~~~

~~~powershell
Get-Mailbox -ResultSize Unlimited | Foreach{Get-MailboxStatistics -Identity $_.UserPrincipalName | Select DisplayName,LastLogonTime,LastUserActionTime}
~~~