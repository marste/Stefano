---
title: Check and repair a linux corrupted filesystem
date: 2018-01-03 08:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'http://pngimg.com/uploads/linux/linux_PNG2.png'
share-img: 'http://pngimg.com/uploads/linux/linux_PNG2.png'
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

`sudo fsck -yvfM /dev/sda1`
	
`sudo fsck -y /dev/sda1`  
		
`sudo fsck -tyfc /dev/sda1`
	