---
title: Script di Backup per MySQL Server compresso
date: 2019-01-07 09:00:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/mysql.png'
share-img: 'https://marzorati.co/img/mysql.png'
categories:
  - Windows
tags:
  - windows
  - mysql
  - backup
  - mysqldump
  - cmd
  - command
  - line
  - 7zip
---
Vai in command prompt:   

	"C:\Program Files\MySQL\MySQL Server 5.7\bin\mysqldump.exe" -u user --password=password nome_database > C:\Backup_DB\backup.sql
	c:\batch\7z.exe a -tzip C:\Backup_DB\NomeDatabase.zip C:\Backup_DB\backup.sql
	del C:\Backup_DB\backup.sql

Potete creare un file .cmd e schedularlo in Windows.