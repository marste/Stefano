---
id: 3128
title: 'Grep Apache access_log and list IP&#8217;s by hits and date sorted'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3128
permalink: /grep-apache-access_log-and-list-ips-by-hits-and-date-sorted/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3127971848
categories:
  - Linux
tags:
  - acces_log
  - apache
  - grep
  - ip
  - sort
---
Esempio:

`grep Oct/2014 /var/log/httpd/access_log |  awk '{ print $1 }' | sort -n | uniq -c | sort -rn | head`