---
id: 1912
title: Installare Acrobat Reader su Fedora
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1912
permalink: /installare-acrobat-reader-su-fedora/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2102691803
categories:
  - Linux
tags:
  - acrobat
  - fedora
  - reader
---
`rpm -ivh http://linuxdownload.adobe.com/adobe-release/adobe-release-i386-1.0-1.noarch.rpm`  
`rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-adobe-linux`  
`yum install nspluginwrapper.i686 AdobeReader_enu`

Se vogliamo installarlo in un&#8217;altra lingua, digita:  
`yum list AdobeReader*`