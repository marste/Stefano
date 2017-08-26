---
id: 2743
title: 'Settare Time Server su Domain Controller &#8211; Ora esatta'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2743
permalink: /settare-time-server-su-domain-controller-ora-esatta/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2329896683
categories:
  - Windows
tags:
  - data
  - esatta
  - ntp
  - ora
  - server
---
`net time /setsntp:ntp2.ien.it`

oppure

`net time /setsntp:"0.pool.ntp.org 1.pool.ntp.org 2.pool.ntp.org"`  
`w32tm /config /syncfromflags:MANUAL /reliable:YES /update`