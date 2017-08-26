---
id: 89
title: Rimuovere i pacchetti del giorno
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/rimuovere-i-pacchetti-del-giorno
permalink: /rimuovere-i-pacchetti-del-giorno/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 895842796477964765
  - 895842796477964765
  - 895842796477964765
dsq_thread_id:
  - 2343713499
categories:
  - Linux
tags:
  - pacchetti
  - rimuovere
---
``grep -e `date +%Y-%m-%d` /var/log/dpkg.log | awk '/install / {print $4}' | uniq | xargs apt-get -y remove``