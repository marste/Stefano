---
id: 3164
title: Cosa fare per prevenire un attacco POODLE sul tuo server Apache SSLv3
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3164
permalink: /cosa-fare-per-prevenire-un-attacco-poodle-sul-tuo-server-apache-sslv3/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3258166664
categories:
  - Linux
  - Windows
tags:
  - apache
  - POODLE
  - sslv3
---
Aggiungi nel tuo vhost:  
`SSLProtocol All -SSLv2 -SSLv3`  
Questo ti darà supporto per: TLSv1.0, TLSv1.1 and TLSv1.2 e sono espressamente rimosse le versioni SSLv2 and SSLv3.

Riavvia Apache