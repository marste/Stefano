---
title: "Attivare Windows e/o Office con uno scripts"
date: 2024-04-25 07:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
layout: post
categories: [Microsoft]
tags: [attivare, windows, versioni, tutte, script, github, massgravel]
---
Fare clic con il tasto destro del mouse sul menu di avvio di Windows e selezionare **PowerShell o Terminal** (non CMD).   
Copiare-incollare il codice sottostante e premere invio:   

~~~powershell
irm https://massgrave.dev/get | iex
~~~

Seguire le istruzioni del menù.