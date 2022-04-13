---
title: "Visualizzare gli aggiornamenti di Windows Update di un PC remoto"
subtitle: Da PowerShell e con un tool
date: 2022-04-08 08:23:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
layout: post
categories: [Windows]
tags: [update, aggiornamenti, remoto, cronologia, history]
---
**Da PowerShell:**   

Esegui PowerShell ed eseguilo come amministratore
Digitare il comando seguente per installare il modulo PowerShell per aggiornare Windows 10 e premere Invio:   

	Install-Module PSWindowsUpdate
	
Digita il seguente comando per visualizzare un elenco dei 20 aggiornamenti più recenti e premi Invio:

	Get-WUHistory -ComputerName "nome_del_PC_remoto" | Select-Object -First 20


**Con un tool:**   

Scarica questo programmino della <b><a href="https://www.nirsoft.net/articles/view-windows-10-update-history.html" target="_blank">NirSoft</a></b>, **premi F9**, scrivi il nome o l'IP del PC remoto e avrai la cronologia degli aggiornamenti installati.   

<a href="https://www.nirsoft.net/utils/winupdatesview-x64.zip" target="_blank">WinUpdatesView</a>
