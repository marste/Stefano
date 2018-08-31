---
id: 1046
title: Migliorare prestazioni di Flash in Linux
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/linux.png'
share-img: 'https://marzorati.co/img/linux.png'
permalink: /performance-flash-in-linux/
authorsure_include_css:
  - 
dsq_thread_id:
  - 1907651497
categories:
  - Linux
tags:
  - cpu
  - flash
  - gpu
  - Linux
  - migliorare
---
`sudo mkdir /etc/adobe/`  
`sudo nano /etc/adobe/mms.cfg`  
e scrivici dentro:  
`OverrideGPUValidation=true`  
`EnableLinuxHWVideoDecode=1`

Facendo così, userà la GPU al posto della CPU