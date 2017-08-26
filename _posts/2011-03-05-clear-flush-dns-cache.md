---
id: 83
title: Clear flush dns cache
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/clear-flush-dns-cache
permalink: /clear-flush-dns-cache/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 7918002575743704979
  - 7918002575743704979
  - 7918002575743704979
dsq_thread_id:
  - 1923007722
categories:
  - Linux
tags:
  - dns
---
`sudo apt-get install nscd`

Flush DNS Cache in Ubuntu Using the following command

`sudo /etc/init.d/nscd restart`