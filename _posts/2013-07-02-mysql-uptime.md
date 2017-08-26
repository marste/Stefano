---
id: 1823
title: MySQL uptime
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1823
permalink: /mysql-uptime/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2099917247
categories:
  - Linux
tags:
  - commandline
  - mysql
  - uptime
---
`mysqladmin  --user=root --password=password status`

Guarda quanto hai di uptime, esempio:  
`Uptime: 2212155`

Dividi per 3600 e avrai le ore di uptime:  
`2212155/3600=614 ore`

Dividi per 24 e avrai i giorni di uptime:  
`614/24=25 giorni`