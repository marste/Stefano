---
title: Backup SQL da command line
date: 2018-01-22 11:45:00 +0200
published: true
image: https://marzorati.co/img/sql.png
share-img: https://marzorati.co/img/sql.png
categories:
  - Windows
tags:
  - SQL
  - commandline
  - backup
  - express
  - sqlcmd
  - script
  - batch
  - erweka
---
Esempio:   

<code>sqlcmd -U sa -P password -S localhost\erwekamc -Q "BACKUP DATABASE ERWEKAMC to DISK='C:\Backup_DB\ERWEKAMC.BAK'"</code>