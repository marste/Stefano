---
id: 60
title: Wireshark come root
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/wireshark-come-root
permalink: /wireshark-come-root/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 4391950784792750522
  - 4391950784792750522
  - 4391950784792750522
categories:
  - Linux
tags:
  - wireshark
---
`sudo chgrp admin /usr/bin/dumpcap`  
`sudo chmod 750 /usr/bin/dumpcap`  
`sudo setcap cap_net_raw,cap_net_admin+eip /usr/bin/dumpcap`

filtro:  
http && http.request.method == &#8220;GET&#8221;