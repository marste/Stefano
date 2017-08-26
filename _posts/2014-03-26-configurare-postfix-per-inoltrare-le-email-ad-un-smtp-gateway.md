---
id: 2786
title: Configurare Postfix per inoltrare le email ad un smtp gateway
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2786
permalink: /configurare-postfix-per-inoltrare-le-email-ad-un-smtp-gateway/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2515161129
categories:
  - Linux
tags:
  - email
  - forward
  - postfix
  - relay
  - smtp
---
Aggiungi al file di configurazione di postfix **/etc/postfix/main.cf** le seguenti righe:

<code>
transport_maps = hash:/etc/postfix/transport
</code>

Se vuoi ad esempio che tutte le email che hanno dominio gmail.com, vengano spedite con l&#8217;smtp **192.168.101.71**, edita il file **/etc/postfix/transport** aggiungendo la regola:

<code>gmail.com          smtp:192.168.101.71:25</code>

oppure se voglio che tutte le email vengano inoltrate verso un certo smtp:   

<code>*          smtp:192.168.101.71:25</code>

Lancia questi comandi:   

<code>postmap hash:/etc/postfix/transport</code>  
<code>postfix reload</code>

Se cambi le regole nel file transport, occorre rilanciare questi due ultimi comandi in modo da rigenerare il file transport.db