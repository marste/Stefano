---
title: "Eliminare tutti i files e cartelle più vecchie di x giorni da cmd"
date: 2020-04-10 09:30:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories: [Script]
tags: [delete, old, files, folder, subfolder, vecchi, giorni, cmd, commandline]
---
Esempio per eliminare files e subfolder più vecchi di 14 giorni:   

~~~batch
@echo off
:: set folder path
set dump_path=C:\Temp\Sessioni

:: set min age of files and folders to delete
set max_days=14

:: remove files from %dump_path%
forfiles -p %dump_path% -m *.* -d -%max_days% -c "cmd  /c del /q @path"

:: remove sub directories from %dump_path%
forfiles -p %dump_path% -d -%max_days% -c "cmd /c IF @isdir == TRUE rd /S /Q @path"
~~~