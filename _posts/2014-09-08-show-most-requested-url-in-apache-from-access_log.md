---
id: 3090
title: Show most requested URL in apache from access_log
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3090
permalink: /show-most-requested-url-in-apache-from-access_log/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2998179391
categories:
  - Linux
tags:
  - access_log
  - apache
  - more
  - request
  - url
---
Esempio:

`awk {'print $7'} /var/log/httpd/access_log-20140907 | sort | uniq -c > /tmp/more_request.txt`