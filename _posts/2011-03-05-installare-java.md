---
id: 67
title: Installare Java
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/installare-java
permalink: /installare-java/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 248159035604131993
  - 248159035604131993
  - 248159035604131993
categories:
  - Linux
tags:
  - java
  - ppa
---
<span style="font-size:130%;">Prima rimuovere:</span>  
`sudo apt-get remove openjdk-6-jre-headless`  
`sudo apt-get remove openjdk-6-jre`  
Se vuoi tenerli tutti e 2:  
`sudo update-alternatives --config java`  
e seleziona la 1.6.24  
questo sistema ti permette di utilizzare sia  
sun-java che openjdk

Poi:  
`sudo add-apt-repository ppa:ferramroberto/java`  
`sudo apt-get update`  
`sudo apt-get install sun-java6-jre sun-java6-plugin sun-java6-fonts`