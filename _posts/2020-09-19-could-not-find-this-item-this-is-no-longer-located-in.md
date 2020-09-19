---
layout: post
title: "Could not find this item. This is no longer located in path. Verify the item’s location and try again"
date: '2020-09-19 08:30:00 +0200'
author: Stefano Marzorati
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories: [Windows]
tags: [eliminare, cartella, percorso, disponibile, commandline, cmd]
published: true
---

Se non riuscite ad eliminare una cartella di Windows e avete come errore questo:   
***"Could not find this item. This is no longer located in path. Verify the item’s location and try again"***

<center><img src="https://marzorati.co/img/post/could_not_find_this_item.webp" alt="could_not_find_this_item"></center>

Basta digitare da command line questo comando:   

	rd /s \\?\C:\bad\folder\path
	
La cartella verrà eliminata.