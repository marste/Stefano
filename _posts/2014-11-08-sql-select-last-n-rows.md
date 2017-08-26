---
id: 3146
title: SQL SELECT LAST N Rows
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3146
permalink: /sql-select-last-n-rows/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3205718151
categories:
  - Linux
  - Windows
tags:
  - mysql
  - order
  - righe
  - sql
  - top
  - ultimi
---
Esempio:   
<code>
SELECT TOP 100 *   
FROM "database"."tabella"."tabella"   
ORDER BY colonnachevuoi DESC
</code>