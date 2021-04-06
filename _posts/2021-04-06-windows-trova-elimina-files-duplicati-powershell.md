---
title: 'Trova e sposta files duplicati in Windows con PowerShell'
author: Stefano Marzorati
layout: post
date: 2021-04-06 17:30:00 +0200
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Windows]
tags: [find, delete, trova, sposta, elimina, windows, files, powershell, script]
---

* Apri PowerShell come amministratore (<i class="fa fa-windows" aria-hidden="true"></i> + x + a)
* Esegui lo script che trovi qua sotto
* Scrivi il nome della cartella in cui vorrai trovare i files duplicati
* Al termine della ricerca, apparirà una finestra per selezionare i file duplicati in base al valore hash. Tutti i file selezionati verranno spostati in C: \ DuplicatesCurrentDate

Ecco lo <a href="https://marzorati.co/download/find_duplicate_files.zip" target="_blank">script</a>

~~~powershell
# .SYNOPSIS
# find_duplicate_files.ps1 finds duplicate files based on hash values.
############# Find Duplicate Files based on Hash Value ###############
''
$filepath = Read-Host 'Enter file path for searching duplicate files (e.g. C:\Temp, C:\)'

If (Test-Path $filepath) {
''
Write-Warning 'Searching for duplicates ... Please wait ...'

$duplicates = Get-ChildItem $filepath -File -Recurse `
-ErrorAction SilentlyContinue | 
Get-FileHash | 
Group-Object -Property Hash |
Where-Object Count -GT 1

If ($duplicates.count -lt 1)

{
    Write-Warning 'No duplicates found.'
    Break  ''
}

else {
    Write-Warning "Duplicates found."
    $result = foreach ($d in $duplicates) 
    { 
    $d.Group | Select-Object -Property Path, Hash   
    } 

$date = Get-Date -Format "MM/dd/yyy"
$itemstomove = $result | 
Out-GridView -Title `
"Select files (CTRL for multiple) and press OK. Selected files will be moved to C:\Duplicates_$date" `
-PassThru 

If ($itemstomove)

{
New-Item -ItemType Directory `
-Path $env:SystemDrive\Duplicates_$date -Force
Move-Item $itemstomove.Path `
-Destination $env:SystemDrive\Duplicates_$date -Force
''
Write-Warning `
"Mission accomplished. Selected files moved to C:\Duplicates_$date"

Start-Process "C:\Duplicates_$date"
}

else 
{
Write-Warning "Operation aborted. No files selected."
}
}
}
else 
{
    Write-Warning `
    "Folder not found. Use full path to directory e.g. C:\photos\patrick"
}
~~~