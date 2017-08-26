---
id: 2872
title: Riparare e ottimizzare tutte le tabelle in tutti i db MySQL
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2872
permalink: /riparare-e-ottimizzare-tutte-le-tabelle-in-tutti-i-db-mysql/
authorsure_include_css:
  - 
categories:
  - Linux
  - Windows
tags:
  - db
  - mysql
  - optimize
  - repair
  - table
---
`mysqlcheck -u root -p --auto-repair --check --optimize --all-databases`