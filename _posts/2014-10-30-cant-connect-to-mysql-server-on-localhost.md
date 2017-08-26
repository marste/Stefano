---
id: 3144
title: 'Can&#8217;t connect to MySQL server on localhost'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3144
permalink: /cant-connect-to-mysql-server-on-localhost/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3173321204
categories:
  - Linux
  - Windows
tags:
  - connection
  - denied
  - localhost
  - mysql
---
Digita semplicemente questa stringa SQL (va bene ovviamente anche da PhpMyAdmin):  
`GRANT ALL PRIVILEGES ON *.* TO 'USERNAME'@'localhost' IDENTIFIED BY 'PASSWORD';`  
Poi  
`FLUSH PRIVILEGES;`  
O riavvia il mysql server