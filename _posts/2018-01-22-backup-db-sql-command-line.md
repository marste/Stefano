---
title: Backup SQL da command line
date: 2018-01-22 11:45:00 +0200
published: true
image: http://www.oracle.com/technetwork/developer-tools/sql-developer/sqldev-128x128x32-2372774.png
share-img: http://www.oracle.com/technetwork/developer-tools/sql-developer/sqldev-128x128x32-2372774.png
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