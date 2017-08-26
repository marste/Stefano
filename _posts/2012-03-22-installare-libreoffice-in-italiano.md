---
id: 1125
title: Installare LibreOffice in italiano
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1125
permalink: /installare-libreoffice-in-italiano/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"182900888149565440";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"182900888149565440";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1926048823
categories:
  - Linux
tags:
  - deb
  - installare
  - italiano
  - libreoffice
---
Esempio:  
Scaricare i 3 files necessari dal sito <a href="http://www.libreoffice.org/download/" title="LibreOffice" target="_blank">http://www.libreoffice.org/download/</a>

Disinstallare le vecchie versioni:

`sudo apt-get purge libreoffice*`

Decomprimere:  
`tar xzvf LibO_3.5.1_Linux_x86_install-deb_en-US.tar.gz`  
`tar xzvf LibO_3.5.1_Linux_x86_langpack-deb_it.tar.gz`  
`tar xzvf LibO_3.5.1_Linux_x86_helppack-deb_it.tar.gz`

Installare in questo ordine:  
`cd`  
`cd LibO_3.5.1rc2_Linux_x86_install-deb_en-US/DEBS/`  
`sudo dpkg -i *.deb`  
`cd desktop-integration`  
`sudo dpkg -i *.deb`  
`cd`  
`cd LibO_3.5.1rc2_Linux_x86_langpack-deb_it/DEBS/`  
`sudo dpkg -i *.deb`  
`cd`  
`cd LibO_3.5.1rc2_Linux_x86_helppack-deb_it/DEBS/`  
`sudo dpkg -i *.deb`