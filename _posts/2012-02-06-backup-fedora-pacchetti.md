---
id: 1098
title: Backup e restore dei pacchetti installati su Fedora
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1098
permalink: /backup-fedora-pacchetti/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"166607320753778689";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"166607320753778689";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 2085109910
categories:
  - Linux
tags:
  - backup
  - dpkg
  - fedora
  - pacchetti
  - yum
---
`rpm -qa > /backup/installed-software.txt`  
`yum -y install $(cat /backup/installed-software.txt)`