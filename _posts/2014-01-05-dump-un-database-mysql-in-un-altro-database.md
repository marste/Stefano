---
id: 2671
title: Dump un database MySQL in un altro database
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2671
permalink: /dump-un-database-mysql-in-un-altro-database/
authorsure_include_css:
  - 
dsq_thread_id:
  - 
categories:
  - Linux
  - Windows
tags:
  - database
  - dump
  - mysql
---
`mysqldump --force -uUSER -pPASS PRODUCTION_DB | mysql -uUSER -pPASS COPY_DB`