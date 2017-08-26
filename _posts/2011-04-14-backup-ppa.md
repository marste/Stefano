---
id: 776
title: Backup PPA
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=776
permalink: /backup-ppa/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2341064310
categories:
  - Linux
tags:
  - backup
  - ppa
  - reinstall
---
Generatore di script per reinstallare i programmi aggiungendo prima i vari ppa

<a href="http://projects.paglias.net/ppbackup/" target="_blank">http://projects.paglias.net/ppbackup/</a>

**Esempio:**

<pre>#!/bin/bash
echo 'Thanks for using ppbackup!'
#add ppas
sudo add-apt-repository ppa:loneowais/ppa
sudo add-apt-repository ppa:webupd8team/ubuntu-font-family
sudo add-apt-repository ppa:mozillateam/firefox-stable
sudo add-apt-repository ppa:webupd8team/y-ppa-manager
 
#install packages
sudo apt-get install renamethemall cloudsn synapse audacious audacious-plugins

#update sources
sudo apt-get update

#ask for upgrades
echo 'Do you want to upgrade?(yes/no)'
read ANSWER
	if [  = "yes" ]; then
			sudo apt-get upgrade
			echo 'System upgraded!'
	fi</pre>