---
id: 1959
title: 'Trovare una parola all&#8217;interno di files'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1959
permalink: /trovare-una-parola-allinterno-di-files/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1899886437
categories:
  - Linux
tags:
  - cercare
  - find
  - parola
  - string
  - trovare
  - word
---
Esempio:

`find /var/www/html/ -name "*.php" -type f -print | xargs grep -i "parola_da_trovare"`

`find /var/www/html/ -type f | xargs grep "parola_da_trovare"`