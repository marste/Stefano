---
id: 3291
title: 'phpMyAdmin &#8211; Cannot start session without errors'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3291
permalink: /phpmyadmin-cannot-start-session-without-errors/
authorsure_include_css:
  - 
video_url:
  - 
quote_content:
  - 
quote_attribution:
  - 
categories:
  - Linux
tags:
  - error
  - php
  - phpmyadmin
  - save_path
  - session
---
Se riscontrate questo errore con phpMyAdmin:

<u>In italiano</u>  
*Non posso far partire la sessione senza errori, controlla gli errori nel log di PHP e/o del tuo server web e configura correttamente la tua installazione di PHP.*

<u>In inglese</u>  
*Cannot start session without errors, please check errors given in your PHP and/or webserver log file and configure your PHP installation properly.*

Le soluzioni sono le seguenti:

&#8211; verificare che nel file **php.ini**, ci sia la riga: `session.save_path = "/var/lib/php/session"`  
&#8211; che il percorso sia esistente  
&#8211; che la directory session abbia almeno permessi 0770  
&#8211; eliminare la cache del browser

Se modificate il file php.ini, ricordatevi di riavviare il servizio httpd di Apache.
