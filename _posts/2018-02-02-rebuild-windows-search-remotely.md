---
layout: post
title: Rebuild Windows Search remotely
date: '2018-02-02 16:00:00 +0200'
author: Stefano Marzorati
published: true
image: 'http://mininook.com/wp-content/uploads/2014/03/utilities-terminal-icon.png'
share-img: 'http://mininook.com/wp-content/uploads/2014/03/utilities-terminal-icon.png'
categories:
  - Windows
tags:
  - rebuild
  - reset
  - windows
  - search
  - wsearch
  - service
  - command line
---
Potete usare questo script batch:   

	psexec -s -d \\%1 net stop wsearch
	sleep 30
	del "\\%1\C$\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows.edb.bak"
	move "\\%1\C$\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows.edb" "\\%1\C$\ProgramData\Microsoft\Search\Data\Applications\Windows\Windows.edb.bak"
	psexec -s -d \\%1 net start wsearch
