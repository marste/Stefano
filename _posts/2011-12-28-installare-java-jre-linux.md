---
id: 1079
title: Installare Java jre su linux
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/linux.png'
share-img: 'https://marzorati.co/img/linux.png'
permalink: /installare-java-jre-linux/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"152035859284238337";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"152035859284238337";}}}'
authorsure_include_css:
  - 
categories:
  - Linux
tags:
  - fedora
  - firefox
  - java
  - Linux
  - ubuntu
---
Scaricare l&#8217;ultima versione di Java presente sul sito:  
<a title="Java" href="http://www.java.com/en/download/linux_manual.jsp?locale=en" target="_blank">http://www.java.com/en/download/linux_manual.jsp?locale=en</a>

Cambiare i permessi al file appena scaricato:  
`chmod a+x jre-6u30-linux-i586.bin`  
Spostare il file nella directory:  
`/usr/java/`  
Installare:  
`./jre-6u30-linux-i586.bin`  
Una volta installato abilitiamo il plugin in Firefox

Spsostarsi nella direcory:  
`cd /usr/lib/mozilla/plugins/`  
Creare il collegamento al plugin:  
`ln -s /usr/java/jre1.6.0_30/lib/i386/libnpjp2.so`