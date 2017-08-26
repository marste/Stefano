---
id: 2021
title: Percentuale di memoria usata per un processo
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2021
permalink: /percentuale-memoria-usata-processo/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2102145278
categories:
  - Linux
tags:
  - memoria
  - memory
  - percentage
  - percentuale
  - process
  - used
---
Esempio per l&#8217;httpd:  
``TOTAL_RAM=`free | head -n 2 | tail -n 1 | awk '{ print $2 }'`; PROC_RSS=`ps axo rss,comm | grep [h]ttpd | awk '{ TOTAL += $1 } END { print TOTAL }'`; PROC_PCT=`echo "scale=4; ( $PROC_RSS/$TOTAL_RAM ) * 100" | bc`; echo "RAM Used by HTTP: $PROC_PCT%"``

Esempio per mysqld:  
``TOTAL_RAM=`free | head -n 2 | tail -n 1 | awk '{ print $2 }'`; PROC_RSS=`ps axo rss,comm | grep [m]ysqld | awk '{ TOTAL += $1 } END { print TOTAL }'`; PROC_PCT=`echo "scale=4; ( $PROC_RSS/$TOTAL_RAM ) * 100" | bc`; echo "RAM Used by MYSQL: $PROC_PCT%"``

<div id="dc_vk_code" style="display: none;">
</div>