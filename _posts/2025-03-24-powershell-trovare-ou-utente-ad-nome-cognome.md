---
title: "PowerShell: Come trovare la OU di un utente in Active Directory (con nome e cognome)"
date: 2025-03-24 10:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Active Directory]
tags: [powershell, AD, OU, nome, cognome, trovare, find]
---
Se avete bisogno di sapere in quale OU è presente un utente di Active Directory sapendo solo il suo nome e cognome, potete utilizzare PowerShell con il seguente comando di esempio:

~~~powershell
Get-ADUser -Filter "GivenName -like '*Mario*' -and Surname -like '*Rossi*'" -Properties DistinguishedName | Select-Object Name, SamAccountName, DistinguishedName
~~~