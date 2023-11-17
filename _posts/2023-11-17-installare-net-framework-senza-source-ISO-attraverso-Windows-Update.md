---
title: "Installare .NET Framework 3.5 senza Source ISO attraverso Windows Update"
author: Stefano Marzorati
layout: post
date: 2023-11-17 12:00:00 +0200
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories: [Windows Servers]
tags: [installare, .net, online, ISO, update, windows]
---
Se hai questo messaggio di errore:   

***The source files could not be found. Try installing the roles, role services, or features again in a new Add Roles and Features Wizard session, and on the Confirmation page of the wizard, click “Specify an alternate source path” to specify a valid location of the source files that are required for the installation. The location must be accessible by the computer account of the destination server.***   

mentre stai installando una feature di Windows Server, è perchè non hai a disposizione i file di origine.   

<span style="background-color:yellow">Ma c'è un'altra possibilità per installare .NET Framework 3.5.</span>   
 
È possibile attivare il download delle funzionalità opzionali direttamente da Windows Update anziché da Windows Server Update Services (WSUS).   

- Esegui gpedit.msc (Local Group Policy Editor)
- Vai in: Computer Configuration > Administrative Templates > System
- Sulla destra cerca: **Specify settings for optional component installation and component repair**
- Impostalo su **Enabled** e seleziona l'opzione **Download repair Content and optional features features directly from Windows Update instead of Windows Server Update Services (WSUS)**
- Ora è possibile avviare nuovamente l'installazione della funzione tramite Server Manager.