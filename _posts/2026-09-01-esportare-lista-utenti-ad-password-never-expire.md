---
title: "Esportare in un file .csv la lista degli utenti AD con Password Never Expire"
subtitle: Script Powershell
date: 2026-08-31 07:30:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
layout: post
published: true
categories: [Windows]
tags: [password, never, expire, powershell, script, export, list]
---
Ecco uno script PowerShell che usa il modulo Active Directory per estrarre tutti gli utenti con l'opzione "Password Never Expires" attiva:   

```
# Richiede il modulo RSAT-AD-PowerShell installato
Import-Module ActiveDirectory

# Estrae gli utenti con PasswordNeverExpires = True
$utenti = Get-ADUser -Filter {PasswordNeverExpires -eq $true} -Properties Name, SamAccountName, PasswordNeverExpires, Enabled, LastLogonDate, PasswordLastSet, DistinguishedName |
    Select-Object Name, SamAccountName, Enabled, PasswordLastSet, LastLogonDate, DistinguishedName

# Mostra a video
$utenti | Format-Table -AutoSize

# Esporta in CSV
$utenti | Export-Csv -Path "C:\Temp\Utenti_PasswordNeverExpire.csv" -NoTypeInformation -Encoding UTF8

Write-Host "Trovati $($utenti.Count) utenti con password impostata su 'non scade mai'." -ForegroundColor Cyan
```

Va eseguito su un DC o su una macchina con RSAT installato (**Install-WindowsFeature RSAT-AD-PowerShell** su Windows Server, oppure tramite **Funzionalità facoltative** su client).