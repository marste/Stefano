---
id: 3138
title: 'vnStat: how to monitor and log network traffic on CentOS'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3138
permalink: /vnstat-how-to-monitor-and-log-network-traffic-on-centos/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3140131553
categories:
  - Linux
tags:
  - centos
  - log
  - monitor
  - network
  - traffic
  - vnstat
---
Installa il servizio:  
`yum install vnstat`

Avvia il servizio al boot:  
`chkconfig vnstat on`

Avvia ora il servizio:  
`/etc/init.d/vnstat start`

Esempi di utilizzo:  
`vnstat -i eth0`  
`vnstat -h -i eth0`  
`vnstat -l -i eth0`  
`vnstati -vs -i eth0 -o /tmp/vnstat.png`

Se volete avere anche un&#8217;interfaccia web, installata sul vostro webserver <a href="http://www.sqweek.com/sqweek/index.php?p=1" target="_blank">vnStat PHP frontend</a>