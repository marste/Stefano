---
id: 3157
title: Check error in mysql
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3157
permalink: /check-error-in-mysql/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3236908610
categories:
  - Linux
  - Windows
tags:
  - check
  - error
  - mysql
  - mysqlcheck
---
Check all tables and all databases:  
`mysqlcheck -c  -u root -p --all-databases`

Check all tables in pippo and pluto databases:  
`mysqlcheck -c  -u root -p --databases pippo pluto`

Check, optimize, and repair tables all databases:  
`mysqlcheck -u root -p --auto-repair -c -o --all-databases`