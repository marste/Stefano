---
title: Check computer uptime using PowerShell
author: Stefano Marzorati
date: 2015-12-03 12:20:00 -07:00
layout: post
permalink: /check-computer-server-uptime-using-powershell/
categories:
  - Windows
tags:
  - command-line
  - uptime
  - server
  - remote
  - powershell
---
Per il computer o server locale:   

	$Booted = (Get-WmiObject Win32_OperatingSystem).LastBootUpTime
	[Management.ManagementDateTimeConverter]::ToDateTime($Booted)

Per un computer o server remoto:

	$Computer = "nome_della_macchina"
	$Booted = Get-WmiObject -Class Win32_OperatingSystem -Computer $Computer
	$Booted.ConvertToDateTime($Booted.LastBootUpTime)
