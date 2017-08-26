---
id: 2038
title: Esportare una tabella mysql
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2034
permalink: /esportare-una-tabella-mysql/
publicize_linkedin_url:
  - 'http://www.linkedin.com/updates?discuss=&scope=114372254&stype=M&topic=5795519925325926400&type=U&a=NuSh'
  - 'http://www.linkedin.com/updates?discuss=&scope=114372254&stype=M&topic=5795519925325926400&type=U&a=NuSh'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
publicize_twitter_url:
  - http://t.co/FFCmjTW78h
  - http://t.co/FFCmjTW78h
authorsure_include_css:
  - 
dsq_thread_id:
  - 1899928990
dsq_needs_sync:
  - 1
categories:
  - Linux
  - Windows
tags:
  - bzip2
  - database
  - dump
  - export
  - mysql
  - tabella
  - table
  - zip
---
`mysqldump -u utente -p database tabella > /tmp/tabella.sql`

Se vogliamo anche comprimere la tabella:  
`mysqldump -u utente -p database tabella | bzip2 > /tmp/tabella.sql.bz2`

<div id="dc_vk_code" style="display: none;">
</div>