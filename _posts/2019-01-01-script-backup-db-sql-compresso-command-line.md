---
title: Script di Backup per SQL Server compresso
date: 2019-01-01 08:00:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/sql.png'
share-img: 'https://marzorati.co/img/sql.png'
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
  - 7zip
---
Vai in command prompt:   

	sqlcmd -U sa -P password -S localhost\session -Q "BACKUP DATABASE NomeDatabase to DISK='C:\Backup_DB\Backup.BAK' WITH INIT"
	c:\batch\7z.exe a -tzip C:\Backup_DB\NomeDatabase.zip C:\Backup_DB\NomeDatabase.BAK
	del C:\Backup_DB\NomeDatabase.BAK

Potete creare un file .cmd e schedularlo in Windows.