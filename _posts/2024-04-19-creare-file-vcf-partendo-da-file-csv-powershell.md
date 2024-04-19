---
title: "Come creare con PowerShell un file .VCF importabile in un cellulare, partendo da un file .CSV"
date: 2024-04-19 10:35:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
layout: post
categories: [Powershell]
tags: [vcf, csv, import, powershell, chatgpt]
---
~~~powershell
# Definire la funzione per creare il file VCF
function Create-VCF {
    param (
        [Parameter(Mandatory=$true)]
        [string]$CsvFile,
        [string]$OutputFile = "contacts.vcf"
    )

    # Leggere i dati dal file CSV
    $Contacts = Import-Csv -Path $CsvFile -Delimiter ";" 

    $VcfLines = @()

    foreach ($entry in $Contacts) {
        $Name = $entry.Name
        $GivenName = $entry.GivenName
        $Surname = $entry.Surname
        $OfficePhone = $entry.OfficePhone

        $VcfLines += "BEGIN:VCARD"
        $VcfLines += "VERSION:3.0"
        $VcfLines += "N:$Surname;$GivenName"
        $VcfLines += "FN:$Name"
        $VcfLines += "TEL;TYPE=WORK,VOICE:$OfficePhone"
        $VcfLines += "END:VCARD"
    }

    $VcfContent = $VcfLines -join "`r`n"
    $VcfContent | Set-Content -Path $OutputFile

    Write-Host "VCF file created successfully: $OutputFile"
}

# Creare il file VCF
Create-VCF -CsvFile "C:\Users\phone.19.04.24.csv"
~~~
Il file .csv dovrà avere queste colonne: **Name;GivenName;Surname;OfficePhone**

Potrai esportare tutti i contatti da ActiveDirectory con questo comando powershell:   

~~~powershell
Get-ADUser -Filter * -SearchBase 'OU=Operativi,OU=Utenti,DC=Azienda,DC=IT' -Properties * | Select-Object Name, GivenName, Surname, OfficePhone | export-csv -path c:\tmp\phonexport.csv
~~~