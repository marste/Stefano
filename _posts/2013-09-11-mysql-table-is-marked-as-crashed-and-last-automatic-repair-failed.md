---
id: 1975
title: mysql table is marked as crashed and last (automatic?) repair failed
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1975
permalink: /mysql-table-is-marked-as-crashed-and-last-automatic-repair-failed/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2010852512
categories:
  - Linux
  - Windows
tags:
  - crashed
  - myisamchk
  - mysql
  - repair
  - table
---
`service mysqld stop`  
`cd /var/lib/mysql/nome_database`  
`myisamchk -r nome_tabella`  
`service mysqld start`

Se la tabella è stata riparata, avrete un messaggio simile:

Data records: 184  
&#8211; Fixing index 1  
&#8211; Fixing index 2  
Data records: 179