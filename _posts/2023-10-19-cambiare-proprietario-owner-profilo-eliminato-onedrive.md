---
title: "Cambiare l'owner di un profilo di OneDrive eliminato con PowerShell"
author: Stefano Marzorati
layout: post
date: 2023-10-19 12:00:00 +0200
image: 'https://marzorati.co/img/onedrive.png'
share-img: 'https://marzorati.co/img/onedrive.png'
categories: [OneDrive]
tags: [cambiare, proprietario, permessi, account, onedrive, eliminato, deleted, powershell]
---
Per prima cosa assicurarsi di aver installato sul PC la componente di <a href="https://www.microsoft.com/en-us/download/details.aspx?id=35588" target="_blank">SharePoint Online Management Shell</a>

Una volta installato, aprite PowerShell e digitate:   

~~~powershell
Connect-SPOService
~~~
Vi chiederà l'url di amministrazione di SharePoint della vostra organizzazione:   
Ad esempio: https://acme-admin.sharepoint.com/

A questo punto per avere la lista di tutti i **Site** di SharePoint eliminati digitate:   
~~~powershell
Get-SPODeletedSite -IncludePersonalSite | FT url
~~~

Se invece volete avere l'elenco di tutti i **Personal Site**, digitate:   
~~~powershell
Get-SPOSite -IncludePersonalSite $true -Limit all
~~~

Avrete una lista simile a questa:   

https://acme-my.sharepoint.com/personal/mario_rossi_acme_it

Per darvi i permessi su questo OneDrive, ora vi basterà digitare:    
~~~powershell
Set-SPOUser -Site https://acme-my.sharepoint.com/personal/mario_rossi_acme_it/_layouts/15/onedrive.aspx -LoginName mio_nome@acme.it -IsSiteCollectionAdmin $True -ErrorAction SilentlyContinue
~~~