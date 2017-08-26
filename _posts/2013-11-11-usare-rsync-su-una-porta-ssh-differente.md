---
id: 2508
title: Usare rsync su una porta ssh differente
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2508
permalink: /usare-rsync-su-una-porta-ssh-differente/
layout_key:
  - 
post_slider_check_key:
  - 0
dsq_thread_id:
  - 1955783794
categories:
  - Linux
tags:
  - different
  - port
  - rsync
  - ssh
---
Esempio:  
`rsync -e "ssh -p 32" -avz --progress --exclude /cache/ /var/www/html/cms/ root@marzorati.co:/var/www/html/site/`