---
id: 3153
title: "Couldn&#8217;t execute &#8216;show create table `tabella`': Table &#8216;./database/tabella&#8217; is marked as crashed and last (automatic?) repair failed"
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3153
permalink: /couldnt-execute-show-create-table-tabella-table-databasetabella-is-marked-as-crashed-and-last-automatic-repair-failed/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3233056932
categories:
  - Linux
  - Windows
tags:
  - crashed
  - mysql
  - repair
  - table
---
Da riga comando ti sposti nella directory di mysql:

`cd /var/lib/mysql/database/`

e lanci il comando:

`myisamchk -r tabella.MYI`