---
id: 1136
title: Installare Virtualbox Guest Addition su Ubuntu Server (no GUI)
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1136
permalink: /installare-virtualbox-guest-addition-ubuntu-server-no-gui/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"185070173340962816";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"185070173340962816";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1968211983
categories:
  - Linux
tags:
  - addition
  - guest
  - server
  - ubuntu
  - virtualbox
---
`sudo apt-get install dkms build-essentials`  
`sudo reboot`  
`sudo mkdir /mnt/cdrom`  
`sudo mount -t iso9660 /dev/cdrom /mnt/cdrom`  
`sudo sh /mnt/cdrom/VBoxLinuxAdditions.run`