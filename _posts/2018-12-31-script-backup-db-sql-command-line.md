---
title: Script di Backup per SQL Server
date: 2018-12-31 12:00:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories:
  - Windows
tags:
  - windows
  - sql
  - backup
  - sqlcmd
  - cmd
  - command
  - line
---
Vai in command prompt:   

	sqlcmd -U sa -P password -S localhost\session -Q "BACKUP DATABASE ERWEKAMC to DISK='C:\Backup_DB\Backup.BAK' WITH INIT"
	
Potete creare un file .cmd e schedularlo in Windows.