---
title: 'Avrai bisogno di una nuova app per aprire questo collegamento ms-calculator'
author: Stefano Marzorati
layout: post
date: 2021-03-25 13:20:00 +0200
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Windows]
tags: [aprire, calcolatrice, app, store, microsoft, ms-calculator]
---
Se avete un nuovo PC con Windows 10 e vi rendete conto che vi mancano le solite applicazioni base che trovate solitamente (calcolatrice, cattura e annota, foto, solitario, editor video, film e tv, etc... etc...) è perchè non è presente nemmeno il **Microsoft Store**.   

Quindi per installare quest'ultimo più tutte le app di default di Windows 10, è sufficiente premere:   

* <i class="fa fa-windows" aria-hidden="true"></i> + x
* Cliccare su **Windows PowerShell (amministratore)**
* Al command prompt, digitare il seguente comando e dare **Invio**:

~~~powershell
Get-AppXPackage -allusers | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}
~~~