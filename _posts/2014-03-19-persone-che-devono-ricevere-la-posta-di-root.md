---
id: 2776
title: Persone che devono ricevere la posta di root
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2776
permalink: /persone-che-devono-ricevere-la-posta-di-root/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2462529647
categories:
  - Linux
tags:
  - aggiungere
  - email
  - indirizzo
  - mail
  - root
---
Modificare il file:   

<code>/etc/aliases</code>   

e aggiungere alla seguente riga, gli indirizzi email delle persone che dovranno leggere la posta inviata all&#8217;utente root


  `# Person who should get root's mail`   
  `root:		support@email.com, user@marzorati.co`   

Poi digitare il comando seguente per aggiornare il db:   
`newaliases`

Per effettuare un test, digita:  
`echo "Testing message" | mail -s "Testing from server" root@localhost`