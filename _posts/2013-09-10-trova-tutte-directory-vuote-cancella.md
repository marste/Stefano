---
id: 1973
title: Trova tutte le directory vuote e le cancella
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1973
permalink: /trova-tutte-directory-vuote-cancella/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:26;}s:2:"wp";a:1:{i:0;i:2;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:26;}s:2:"wp";a:1:{i:0;i:2;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2824341969
categories:
  - Linux
tags:
  - cartelle
  - directory
  - elimina
  - vuote
---
Esempio:  
`find /var/www/html/cache/ -type d -empty -exec rmdir {} ;`