---
title: 'Trova i files a cui non si accede da tempo da PowerShell'
author: Stefano Marzorati
layout: post
date: 2021-04-07 12:59:00 +0200
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Windows]
tags: [find, time, accesso, access, giorni, windows, mesi, powershell, anni]
---

Se devi trovare tutti i files nel percorso **"C:\Shared Folders\Utenti"** a cui non si accede da più di 5 anni (1825 giorni) salvando su un file il nome, l'ultima volta che qualcuno ci ha acceduto e la sua dimensione, digita questa riga:   

~~~powershell
Get-ChildItem -Path "C:\Shared Folders\Utenti" -Recurse -Force  | Where-Object {$_.LastAccessTime -lt (Get-Date).AddDays(-1825)} | select fullname,lastaccesstime,Length |export-csv "C:\TMP\Last.csv" -NoTypeInformation
~~~

La dimensione è in **Byte**, se la vuoi in **Gigabyte** dividi per 1073741824.