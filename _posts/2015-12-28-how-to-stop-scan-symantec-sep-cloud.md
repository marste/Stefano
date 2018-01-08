---
title: How to stop scanning Symantec Endpoint Protection Cloud
date: 2015-12-28 16:00:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /how-to-stop-scan-symantec-sep-cloud/
image: 'https://tigerware.lsu.edu/image/e7275ace-8ee7-4baf-9fe7-df2f62e76682.png'
share-img: 'https://tigerware.lsu.edu/image/e7275ace-8ee7-4baf-9fe7-df2f62e76682.png'
categories:
  - Windows
tags:
  - symantec
  - scanning
  - stop
  - service
  - cloud
  - sep
  - commandline
---
Stops the client service and unloads it from memory.   

From command line:   

	"C:\Program Files\Symantec.cloud\EndpointProtectionAgent\smc.exe" -p password -stop
	
Starts the client service.   

	"C:\Program Files\Symantec.cloud\EndpointProtectionAgent\smc.exe" -p password -start