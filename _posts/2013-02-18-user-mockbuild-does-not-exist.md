---
id: 1404
title: user mockbuild does not exist
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1404
permalink: /user-mockbuild-does-not-exist/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:24;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:24;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1985327307
categories:
  - Linux
---
Problema:  
`warning: user mockbuild does not exist - using root   
warning: group mockbuild does not exist - using root`

Risoluzione:  
`yum install mock`  
`useradd -s /sbin/nologin mockbuild`