---
id: 1880
title: Install Vmware Tools on Debian using commandline interface
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1880
permalink: /install-vmware-tools-on-debian-using-commandline-interface/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
geo_public:
  - 0
  - 0
authorsure_include_css:
  - 
dsq_thread_id:
  - 1938833001
categories:
  - Linux
tags:
  - command line
  - commandline
  - debian
  - tools
  - vmware
---
``apt-get install gcc-4.4 make linux-headers-`uname -r` -y``  
da vSphere Client installa da Guest &#8211; Install VMware Tools  
`mount /dev/cdrom /media/cdrom`  
`cd /media/cdrom`  
`ls -l`  
`cd /home/`  
`tar xvfz /media/cdrom/VMwareTools-8.6.5-621624.tar.gz`  
`cd /home/vmware-tools-distrib/`  
`./vmware-install.pl`

Vi verranno fatte delle domande e se è tutto ok e i path del gcc vengono trovati, procedere dando invio.