---
id: 1424
title: 'Script: installare Java JRE in modalità Silent'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1424
permalink: /java-jre-deploy/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:24;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:24;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1913999233
layout_key:
  - 
post_slider_check_key:
  - 0
categories:
  - Windows
tags:
  - deploy
  - install
  - java
  - remote
  - silent
---
Installa sul tuo pc l&#8217;ultima versione di Java  
e vai in:

`C:\Documents and Settings\User\Dati applicazioni\Sun\Java`

qui troverai la directory contenente il file .msi

Qui di seguito lo script per l&#8217;installazione da remoto:

`xcopy "\\Server\Java\JavaJRE\jre1.7.0_45\*" "\\%1\C$\Temp\jre1.7.0_45\*.*" /r/i/c/h/k/e   
sleep 3   
psexec \\%1 -s -d msiexec /i  "C:\Temp\jre1.7.0_45\jre1.7.0_45.msi" /qn /norestart`