---
title: Disabilitare Windows Defender su Windows Server 2016 da PowerShell
date: 2018-10-26 11:47:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories:
  - Windows
tags:
  - windows
  - defender
  - antivirus
  - realtime
  - server
  - 2016
  - powershell
---
**Check the Windows Defender Configuration and Settings:**   

	Get-MpPreference

**Turn off Windows Defender Real-Time Protection using PowerShell**   

	Set-MpPreference -DisableRealtimeMonitoring $true

**Turn onWindows Defender Real-Time Protection using PowerShell**   

	Set-MpPreference -DisableRealtimeMonitoring $false

**Add a File path exclusion:**   

	Set-MpPreference -ExclusionPath "C:\temp", "C:\VM", "C:\NanoServer"

**Add process exclusion**   

	Set-MpPreference -ExclusionProcess "vmms.exe", "Vmwp.exe"

 

**To remove windows defender open command prompt with administrator and copy following**   

	Dism /online /Disable-Feature /FeatureName:Windows-Defender /Remove /NoRestart /quiet

restart server   

	Get-MpPreference 