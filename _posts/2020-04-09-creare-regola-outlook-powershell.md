---
title: "Creare una regola su Outlook via Powershell su Office365"
date: 2020-04-09 12:30:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Powershell]
tags: [rule, office365, powershell, regola, outlook, mail, spostare, move]
---
**Connettersi tramite PowerShell a Office365:**   
~~~powershell
Install-Module -Name ExchangeOnlineManagement
Import-Module ExchangeOnlineManagement
Connect-ExchangeOnline -UserPrincipalName  mioindirizzoemail
~~~

**Creare ad esempio la regola per spostare delle email con un certo mittente (pippo@acme.com) in una cartella specifica (Cartella di Destinazione):**   
~~~powershell
New-InboxRule -Mailbox clienti@acme.com -Name "Move to folder" -From pippo@acme.com -MoveToFolder clienti@acme.com:\Inbox\"Cartella di Destinazione"
~~~

**Chudere la sessione:**   
~~~powershell
Remove-PSSession $Session
~~~