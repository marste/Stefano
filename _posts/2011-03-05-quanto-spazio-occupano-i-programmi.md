---
id: 91
title: Quanto spazio occupano i programmi?
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/quanto-spazio-occupano-i-programmi
permalink: /quanto-spazio-occupano-i-programmi/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 6795889840315226141
  - 6795889840315226141
  - 6795889840315226141
dsq_thread_id:
  - 2026318236
categories:
  - Linux
tags:
  - space
---
`dpkg-query --show --showformat='${Package;-50}t${Installed-Size}n' | sort -k 2 -n | grep -v deinstall | awk '{printf "%.3f MB t %sn", $2/(1024), $1}' | tail -n 30`