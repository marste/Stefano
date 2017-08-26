---
title: How to mount CIFS share permanently on Ubuntu
date: 2015-08-07 09:00:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /how-to-mount-cifs-share-permanently-on-ubuntu/
categories:
  - Linux
tags:
  - mount
  - share
  - cifs
  - automount
  - permanently
  - ubuntu
  - server
  - windows
---
Install:   

	apt-get install cifs-utils

Create directory:   

	mkdir /mnt/cifs

Create file:   

	nano ~/.smbcredentials

Insert the username and password for accessing the remote share:   

	username=administrator
	password=password
	
Run command to get your gid and uid. Replace root with your user name.

	id root

Example output:   

	uid=0(root) gid=0(root) groups=0(root)
	
Now edit the fstab:   

	nano /etc/fstab
	
Add below line to the end and save it:   

	//192.168.5.38/Backup_SRVWEB01 /mnt/cifs cifs credentials=/root/.smbcredentials,iocharset=utf8,gid=0,uid=0,file_mode=0777,dir_mode=0777 0 0

Mount share:   	

	mount -a
