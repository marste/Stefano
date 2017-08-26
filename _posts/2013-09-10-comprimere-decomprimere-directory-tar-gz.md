---
id: 1968
title: Comprimere e decomprimere directory in tar.gz
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1968
permalink: /comprimere-decomprimere-directory-tar-gz/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2180589573
categories:
  - Linux
tags:
  - compress
  - comprimere
  - tar.gz
  - uncompress
  - zippare
---
Esempio di compressione:

`tar cvzf test.tar.gz /home/test` (non mettere lo slash alla fine dell&#8217;ultima directory)

Esempio di decompressione:  
`tar -xvf test.tar.gz`

Vedere il contenuto di un file tar.gz:  
`tar -tvf test.tar.gz`

Estrai un singolo file:  
`tar -zxvf test.tar.gz prova.xml`

Estrai tutti i files che hanno una certa estensione:  
`tar -zxvf test.tar.gz --wildcards '*.php'`