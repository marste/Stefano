---
id: 130
title: 'Spostare i log dell&#8217;httpd in un altro percorso'
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/10/spostare-i-log-dellhttpd-in-un-altro-percorso
permalink: /spostare-i-log-dellhttpd-in-un-altro-percorso/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 9056537475444638506
  - 9056537475444638506
  - 9056537475444638506
categories:
  - Linux
tags:
  - apache
  - log
---
`cd /var/log`

`/etc/init.d/httpd stop`

`mkdir -p /srv/cluster/var/log/httpd`

`cp /var/log/httpd/* /srv/cluster/var/log/httpd`

`rm -rf /var/log/httpd/`

`ln -s /srv/cluster/var/log/httpd`

`/etc/init.d/httpd start`