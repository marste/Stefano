---
id: 19
title: Installare no-ip.org
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/04/installare-no-ip-org
permalink: /installare-no-ip-org/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 2912111127555251880
  - 2912111127555251880
  - 2912111127555251880
dsq_thread_id:
  - 2266212536
categories:
  - Linux
tags:
  - dns
  - remote
---
`sudo apt-get install noip2`

user: user@gmail.com  
password: miapassword</span>

Per riconfigurarlo:

`sudo /etc/init.d/noip2 stop`  
`sudo noip2 -C`  
Segui la procedura guidata e lo fai ripartire:  
`sudo /etc/init.d/noip2 start`