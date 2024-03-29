---
title: Visualizzare il nome client di un Remote Desktop Server da PowerShell
date: 2023-05-18 10:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
layout: post
categories: [Windows]
tags: [getting, client, name, remote desktop server, powershell, rdp, rds, idle, shadow]
---
Per installare il modulo:   
~~~powershell
Install-Module -Name PSTerminalServices
~~~
Per abilitare l'esecuzione:   
~~~powershell
Set-ExecutionPolicy RemoteSigned
~~~
Per importare il modulo:   
~~~powershell
Import-Module PSTerminalServices
~~~
Per avere la **lista dei client** collegati:   
~~~powershell
Get-TSSession -ComputerName <nome_server>
~~~
Per **disconnettere** un utente:   
~~~powershell
Stop-TSSession <numero_id> -ComputerName <nome_server>
~~~
Per inviare un **messaggio popup**:   
~~~powershell
Send-TSMessage <numero_id> -ComputerName <nome_server>
~~~

Se volete prendere il **controllo remoto** di una sessione di un utente:   

	mstsc.exe /shadow:<id_sessione> /v:<nome_server> /control /noConsentPrompt

Se volete vedere da quanto tempo un certo utente è **idle**, basta digitare:   

	quser /SERVER:<nome_server>
	
Un altro modo più semplice per disconnettere un utente da una sessione RDS è il seguente:   

	logoff <id_sessione> /server:<nome_server>
	
Altri comandi li trovate qua di seguito:   

**Disconnect-TSSession** - Disconnects any attached user from the session.   
**Get-TSCurrentSession** - Provides information about the session in which the current process is running.   
**Get-TSServers** - Enumerates all terminal servers in a given domain.   
**Get-TSProcess** - Gets a list of processes running in a specific session or in all sessions.   
**Get-TSSession** - Lists the sessions on a given terminal server.   
**Send-TSMessage** - Displays a message box in the specified session ID.   
**Stop-TSProcess** - Terminates the process running in a specific session or in all sessions.   
**Stop-TSSession** - Logs the session off, disconnecting any user that might be connected.   