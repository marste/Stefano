---
id: 2781
title: 'Too many connection errors &#8211; Unblock with &#8216;mysqladmin flush-hosts&#8217;'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2781
permalink: /too-many-connection-errors-unblock-with-mysqladmin-flush-hosts/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2505238871
categories:
  - Linux
  - Windows
tags:
  - flush
  - mysql
  - mysqladmin
  - too many
  - unblock
---
Collegati al mysql della tua macchina:

`mysql -u root -p`

Lancia il comando:

`flush hosts;`