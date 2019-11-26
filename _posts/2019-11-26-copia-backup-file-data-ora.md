---
title: Creare copia di backup rinominando il file con data e ora
subtitle: Schedulando un file batch
date: 2019-11-26 17:30:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
layout: post
categories:
  - Windows
tags:
  - batch
  - script
  - rename
  - move
  - backup
  - data
  - ora
---
Ecco un esempio di batch che ha come scopo quello di fare una copia di backup di un file, rinominado la copia con la data e l'ora corrente.   

	set data=%date:~6,4%-%date:~3,2%-%date:~0,2%
	set ora=%time:~0,2%.%time:~3,2%
	copy "D:\tmp\test.xlsx" "D:\tmp\Copia_Test.xlsx"
	move "D:\tmp\Copia_Test.xlsx" "D:\tmp\Storico\test_%data%_%ora%.xlsx"

