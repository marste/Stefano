---
title: Check and repair a corrupted filesystem
date: 2018-01-03 08:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'http://www.gandotech.net/wp-content/uploads/2015/04/Terminal-icon-shell-linux-unix.png'
share-img: 'http://www.gandotech.net/wp-content/uploads/2015/04/Terminal-icon-shell-linux-unix.png'
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