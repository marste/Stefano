---
title: "Eseguire GPResult come amministratore"
date: 2022-04-07 17:33:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
layout: post
categories: [Windows]
tags: [gpresult, runas, admin, commandline, policy]
---
Se devi eseguire un **GPResult** per verificare se il PC ha preso delle **Group Policy** a livello Computer e l'utente non è **Administrator**.   
Digita:   

	cmd runas admin
	
Da questo momento potrai digitare il comando come se fossi amministratore locale del PC, e quindi ti basterà digitare:   

	gpresult /H C:\Temp\result.html