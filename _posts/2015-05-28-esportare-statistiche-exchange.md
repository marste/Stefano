---
title: Get-LogonStatistics - Esportare statistiche da Exchange da shell
date: 2015-05-28 11:15:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /get-logonstatistics-esportare-statistiche-exchange-shell/
categories:
  - Software
tags:
  - get-logonstatistics
  - esportare
  - statistiche
  - exchange
  - shell
  - server
---
Se avete la necessità di sapere quante persone sono attive su un server Exchange, compreso di nome utente e nome del pc, il comando da shell da lanciare è il seguente:   

	Get-LogonStatistics -Server NomedelServer | select-object UserName,ClientName  | export-csv c:\export.csv   

Se avete bisogno di sapere la versione di Outlook in usodai vostri utenti, potete lanciare il seguente comando, che vi fornirà anche il nome dell'utente, l'ultima volta che eseguito l'accesso e il nome del server sul quale è configurato:   

	Get-MailboxServer | Get-LogonStatistics | Select UserName,ClientVersion,LastAccessTime,ServerName   

Se avete bisogno di avere altre informazioni, potete usare anche le seguenti opzioni:   

	AdapterSpeed   
	ClientIPAddress   
	ClientMode   
	ClientName   
	ClientVersion   
	CodePage   
	CurrentOpenAttachments   
	CurrentOpenFolders   
	CurrentOpenMessages   
	FolderOperationCount   
	FullMailboxDirectoryName   
	FullUserDirectoryName   
	HostAddress   
	LastAccessTime   
	Latency   
	LocaleID   
	LogonTime   
	MACAddress   
	MessagingOperationCount   
	OtherOperationCount   
	ProgressOperationCount   
	RPCCallsSucceeded   
	StreamOperationCount   
	TableOperationCount   
	TotalOperationCount   
	TransferOperationCount   
	UserName   
	Windows2000Account   
	ServerName   
	StorageGroupName   
	DatabaseName   
	Identity