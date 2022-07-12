---
title: "Esportare gli utenti dell'active directory in .csv con PowerShell"
author: Stefano Marzorati
date: 2022-07-12 11:30:00 +0200
layout: post
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Powershell]
tags: [export, esportare, lista, utenti, powershell, Get-ADUser]
---
Se avete bisogno di esportare la lista di tutti gli utenti di AD, potete usare questa riga in powershell:
~~~powershell
Get-ADUser -Filter * -Properties * | Select-Object GivenName, Surname, UserPrincipalName, Department | export-csv -path c:\temp\userexport.csv
~~~

Se avete bisogno di esportare altri oggetti o campi, potete vedere i nomi facendo una query di esempio su un utente:   
~~~powershell
Get-ADUser nome_utente -Properties *
~~~