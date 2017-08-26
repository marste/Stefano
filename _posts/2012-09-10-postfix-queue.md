---
id: 1192
title: 'Postfix &#8211; Gestione coda'
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1192
permalink: /postfix-queue/
geo_public:
  - 0
  - 0
authorsure_include_css:
  - 
dsq_thread_id:
  - 1975708128
categories:
  - Linux
tags:
  - coda
  - mailq
  - postfix
  - postqueue
  - postuser
  - queue
---
**mail in coda**  
`mailq`

**svuota la coda**  
`postsuper -v -d ALL`

**elimina una specifica email**  
`postsuper -d mailID`

**flush delle email in coda**  
`postqueue -f`

**elimina tutte le mail in deferred**  
`postsuper -d deferred`