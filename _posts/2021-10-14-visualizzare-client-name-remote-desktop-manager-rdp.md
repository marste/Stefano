---
title: Visualizzare il nome client di un Remote Desktop Server da PowerShell
date: 2021-10-14 09:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
layout: post
categories: [Windows]
tags: [getting, client, name, remote desktop server, powershell, rdp, rds]
---
Per installare il modulo:   
~~~powershell
Install-Module -Name PSTerminalServices
~~~
Per avere la lista dei client collegati:   
~~~powershell
Get-TSSession -ComputerName <nome_server>
~~~
Per disconnettere un utente:   
~~~powershell
Stop-TSSession <numero_id> -ComputerName <nome_server>
~~~
Per inviare un messaggio popup:   
~~~powershell
Send-TSMessage <numero_id> -ComputerName <nome_server>
~~~

**Disconnect-TSSession** - Disconnects any attached user from the session.   
**Get-TSCurrentSession** - Provides information about the session in which the current process is running.   
**Get-TSServers** - Enumerates all terminal servers in a given domain.   
**Get-TSProcess** - Gets a list of processes running in a specific session or in all sessions.   
**Get-TSSession** - Lists the sessions on a given terminal server.   
**Send-TSMessage** - Displays a message box in the specified session ID.   
**Stop-TSProcess** - Terminates the process running in a specific session or in all sessions.   
**Stop-TSSession** - Logs the session off, disconnecting any user that might be connected.   