---
title: Non funziona MFA (autenticazione a più fattori) con Office 2013
subtitle: Richiesta continua della password di Outlook
date: 2022-04-20 09:05:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories: [Windows]
tags: [Windows, get, LastAccessTime, export, powershell, Get-ChildItem, Recurse]
---
Microsoft Office 2013 supporta l'autenticazione moderna, ma ha bisogno che vengano aggiunte le seguenti chiavi di registro:   

~~~regedit
Windows Registry Editor Version 5.00

[HKEY_CURRENT_USER\Software\Microsoft\Exchange]
"AlwaysUseMSOAuthForAutoDiscover"=dword:00000001

[HKEY_CURRENT_USER\Software\Microsoft\Office\15.0\Common]

[HKEY_CURRENT_USER\Software\Microsoft\Office\15.0\Common\Identity]
"EnableADAL"=dword:00000001
"Version"=dword:00000001
~~~

- Salva il file con l'estensione .reg invece di .txt in una posizione facile da trovare. Ad esempio, C:\Temp\Office2013_Enable_ModernAuth.reg
- Aprire Esplora file, individuare il percorso del file .reg appena salvato, quindi fare doppio clic su di esso.
- Dopo aver impostato le chiavi del Registro di sistema, è possibile impostare le app di Office 2013 per l'uso dell'autenticazione a più fattori (MFA) con Microsoft 365.