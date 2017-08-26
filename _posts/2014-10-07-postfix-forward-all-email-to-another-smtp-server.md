---
id: 3120
title: 'Postfix &#8211; Forward all email to another smtp server'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3120
permalink: /postfix-forward-all-email-to-another-smtp-server/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3091526089
categories:
  - Linux
tags:
  - postfix
  - relay
  - smtp
---
Se hai bisogno di inoltrare tutte le mail di postfix, verso un altro server SMTP, serve solo una piccola modifica al file di configurazione:

`/etc/postfix/main.cf`

Basta aggiungere la seguente riga, ad esempio:

`relayhost = 192.168.101.7:25`

Poi riavvia Postfix:

`/etc/init.d/postfix restart`