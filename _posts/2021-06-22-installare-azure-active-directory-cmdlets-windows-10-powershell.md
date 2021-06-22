---
title: "Installare Azure Active Directory su Windows 10 con PowerShell"
author: Stefano Marzorati
layout: post
date: 2021-06-22 11:05:00 +0200
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Windows]
tags: [installare, azure, powershell, active, directory, cmdlets]
---
Installa il modulo Azure Active Directory Cmdlets:   

~~~powershell
Install-Module -Name MSOnline
~~~

Se ad esempio ti devi collegare sul portale Azure:   
~~~powershell
Connect-msolservice
~~~

Se ad esempio devi cambiare l'UPN (UserPrincipalName), digita:   

~~~powershell
Set-MsolUserPrincipalName -UserPrincipalName vecchioUPN -NewUserPrincipalName nuovoUPN
~~~
