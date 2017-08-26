---
id: 1087
title: Verificare se esiste un indirizzo email
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1087
permalink: /verificare-se-esiste-un-indirizzo-email/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"159291393590837248";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"159291393590837248";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1941833474
categories:
  - Linux
  - Windows
tags:
  - address
  - email
  - esiste
  - indirizzo
  - verificare
  - verify
---
**nslookup**  
**set type=mx**  
**dominio.it**

ti annoti l&#8217;mx principale (in questo caso facciamo che sia il seguente)  
**out.mail.it**

**telnet out.mail.it 25**  
**helo caro**  
**MAIL FROM: <test@test.org>**  
**RCPT TO: <rossi@mail.it>**

Se l&#8217;utente esiste **&#8220;Recipient ok&#8221;**  
Se l&#8217;utente non esiste **&#8220;No such user&#8221;**