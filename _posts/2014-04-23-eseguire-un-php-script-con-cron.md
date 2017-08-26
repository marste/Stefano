---
id: 2838
title: Eseguire un PHP script con cron
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2838
permalink: /eseguire-un-php-script-con-cron/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2633098184
categories:
  - Linux
tags:
  - cron
  - crontab
  - php
---
Esempio:

\# Ogni 5 minuti esegui questo file .php  
`*/5 * * * * php -q /var/www/html/scheduled.php >/dev/null 2>&#038;1`