---
id: 2903
title: Importare un file .csv in un database MySQL da command line
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2903
permalink: /importare-un-file-csv-in-un-database-mysql-da-command-line/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2835013958
categories:
  - Linux
  - Windows
tags:
  - command line
  - csv
  - import
  - mysql
---
Se avete un file .csv molto grande e magari non riuscite ad importarlo attraverso PhpMyAdmin, potete importare i dati da command line.

Se si tratta di un mysql su Windows, la sintassi sarà questa:

`load data local infile 'd:/temp/file.csv' into table nome_tabella fields terminated by ';';`