---
title: How to stop scanning Symantec Endpoint Protection Cloud
date: 2015-12-28 16:00:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /how-to-stop-scan-symantec-sep-cloud/
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