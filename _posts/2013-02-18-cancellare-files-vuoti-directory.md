---
id: 1410
title: Cancellare files vuoti in una directory
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1410
permalink: /cancellare-files-vuoti-directory/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:24;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:24;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2162387142
categories:
  - Linux
---
`find <strong>/tmp/</strong> -size 0 | xargs /bin/rm -f`