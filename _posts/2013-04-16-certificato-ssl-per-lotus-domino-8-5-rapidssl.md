---
id: 1514
title: 'Certificato SSL per Lotus Domino 8.5 &#8211; RapidSSL'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1514
permalink: /certificato-ssl-per-lotus-domino-8-5-rapidssl/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:31;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:31;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2171797875
categories:
  - Windows
---
- Dal client Notes aprire il database &#8220;**Server Certificate Admin**&#8221;  
&#8211; Selezionare &#8220;**Create key ring**&#8221;  
&#8211; Selezionare &#8220;**Create Certificate Request**&#8221;

&#8211; Inviare il certificato creato nel nostro caso a RapidSSL (acquistandolo)  
&#8211; Vi verrà inviato via mail il vostro nuovo certificato.

&#8211; Dal client Notes aprire nuovamente il database &#8220;**Server Certificate Admin**&#8221;  
&#8211; Selezionare &#8220;**Install Trusted Root Certificate into Key Ring**&#8221; (il certificato TrustedRoot lo trovate sul sito http://www.rapidssl.com)  
&#8211; Selezionare &#8220;**Install Certificate Into Key Ring**&#8221; (prendendo il certificato che vi è stato inviato)

Al contrario di come riporta la documentazione sul sito di RapidSSL, non occorre installare il CrossRoot certificate nè l&#8217;Intermediate certificate.

&#8211; Copiare i file **keyfile.kyr** e **keyfile.sth** in LotusDominoData  
&#8211; Riavviare il task HTTP di Domino (**restart task http**)