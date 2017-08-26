---
id: 1854
title: 'pflogsumm: produce Postfix MTA logfile summary'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1854
permalink: /postfix-mta-log-summary/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
geo_public:
  - 0
  - 0
authorsure_include_css:
  - 
dsq_thread_id:
  - 2572496922
categories:
  - Linux
tags:
  - log
  - mta
  - pflogsumm
  - postfix
  - summary
---
`apt-get install pflogsumm`

Esempio:  
`pflogsumm -d today /var/log/mail.log > /tmp/23.07.13.txt`