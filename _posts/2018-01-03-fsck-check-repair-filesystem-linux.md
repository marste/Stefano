---
title: Check and repair a linux corrupted filesystem
date: 2018-01-03 08:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://raw.githubusercontent.com/snwh/moka-icon-theme/master/Moka/64x64@2x/apps/utilities-terminal.png'
share-img: 'https://raw.githubusercontent.com/snwh/moka-icon-theme/master/Moka/64x64@2x/apps/utilities-terminal.png'
categories:
  - Linux
tags:
  - tftp
  - server
  - cisco
  - ubuntu
  - linux
---
Example:   

	sudo fsck -yvfM /dev/sda1   
	
	sudo fsck -y /dev/sda1   
	
	sudo fsck -tyfc /dev/sda1   
