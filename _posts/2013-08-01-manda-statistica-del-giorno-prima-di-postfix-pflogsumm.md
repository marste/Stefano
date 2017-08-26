---
id: 1895
title: Manda statistica del giorno prima di postfix (pflogsumm)
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1895
permalink: /manda-statistica-del-giorno-prima-di-postfix-pflogsumm/
geo_public:
  - 0
  - 0
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2213436966
categories:
  - Linux
tags:
  - log
  - mail
  - pflogsumm
  - postfix
---
`pflogsumm -d yesterday --problems_first /var/log/mail.log | mail -s "yesterday's mail activity" utente@dominio.com`