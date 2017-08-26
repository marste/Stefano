---
id: 2545
title: Query mysql WHERE LENGTH
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2545
permalink: /query-mysql-lunghezza/
authorsure_include_css:
  - 
layout_key:
  - 
post_slider_check_key:
  - 0
dsq_thread_id:
  - 2020581171
categories:
  - Linux
  - Windows
tags:
  - lunghezza
  - mysql
  - query
  - where
---
Selezionare dalla tabella newsletter, tutto ciò che è più lungo di 30 caratteri nel campo email:

``SELECT * FROM `newsletter` WHERE LENGTH( email ) >30``