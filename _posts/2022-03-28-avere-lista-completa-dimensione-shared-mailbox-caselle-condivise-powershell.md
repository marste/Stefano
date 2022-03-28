---
title: "Ottenere la lista completa e lo spazio utilizzato da tutte le shared mailbox via powershell"
date: 2022-03-28 07:53:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
layout: post
categories: [Office365]
tags: [lista, dimensione, spazio, size, mailbox, shared, condivisa]
---
Collegati via PowerShell ad Exchange Online:   

	Connect-ExchangeOnline -UserPrincipalName tuo@utente.com

Digita questo comando per avere la lista completa:   

	Get-EXOMailbox -RecipientTypeDetails SharedMailbox -ResultSize Unlimited | Get-EXOMailboxStatistics | Sort-Object -Property TotalItemSize -Descending | Select-Object DisplayName,ItemCount,TotalItemSize
