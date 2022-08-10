---
title: "Verificare se un PC remoto supporta TPM"
author: Stefano Marzorati
date: 2022-08-10 08:30:00 +0200
layout: post
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Windows]
tags: [TPM, powershell, remoto, protezione, attivo, versione]
---
Per vedere se un PC remoto supporta il TPM per attivare il BitLocker, digita questo comando PowerShell:   

~~~powershell
Get-WmiObject -class Win32_Tpm -namespace root\CIMV2\Security\MicrosoftTpm  -computername  nome_computer
~~~
Se vi ritornerà un messaggio contenente le informazioni sulla versione, ad esempio **SpecVersion: 2.0, 0, 1.38**, la risposta è che quel PC lo supporta.   
Se non vi tornerà alcun messaggio, il PC non lo supporta.   

Per vedere se un PC remoto ha già la protezione Bitlocker attiva sul disco C:, potete digitare questo comando:   

~~~powershell
Get-WMIObject -Namespace "root/CIMV2/Security/MicrosoftVolumeEncryption" -query "SELECT * FROM Win32_EncryptableVolume WHERE DriveLetter='C:'" -ComputerName Nome_Computer | Select-Object ProtectionStatus
~~~
Se avrete come risposta **1**, la protezione è attiva, se è **0** è disattiva.   