---
title: "Come ottenere l'elenco di tutte le applicazioni installate in Windows"
date: 2021-12-21 12:35:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
layout: post
categories: [Windows]
tags: [elenco, applicazioni, installati, wmic, product, get, name]
---
Se si desidera ottenere l'elenco di tutte le applicazioni installate nel sistema Windows, è necessario utilizzare il comando:

	wmic product get name
	
Per vedere la lista dei programmi di un PC remoto:

	psexec \\nome_pc wmic product get name