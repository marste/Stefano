---
id: 1396
title: Esempio di rsync con esclusione directory
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1396
permalink: /esempio-di-rsync-esclusione-directory/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:24;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:24;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2026136341
categories:
  - Linux
---
`rsync -avz --progress --exclude /cache/ /var/www/html/sito/ root@192.168.1.58:/var/www/html/sito/`