---
id: 1953
title: Trova i files più grandi di 100 Mb
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1953
permalink: /trova-files-piu-grandi-100-mb/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1973728997
categories:
  - Linux
tags:
  - big
  - files
  - find
  - grandi
  - trova
---
Esempio:  
`find /home -type f -size +100000000c -exec ls -lh {} ;`