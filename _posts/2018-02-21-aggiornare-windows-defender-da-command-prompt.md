---
layout: post
title: Aggiornare Windows Defender da Command Prompt
date: '2018-02-21 10:02:00 +0200'
author: Stefano Marzorati
image: 'http://mininook.com/wp-content/uploads/2014/03/utilities-terminal-icon.png'
share-img: 'http://mininook.com/wp-content/uploads/2014/03/utilities-terminal-icon.png'
categories:
  - Windows
tags:
  - esegui
  - defender
  - windows
  - update
  - quickscan
  - command line
published: true
---
**Per aggiornare Windows Defender**   
`"%ProgramFiles%\Windows Defender\MpCmdRun.exe" -SignatureUpdate`

**Per eseguire uno scan veloce**   
`"%ProgramFiles%\Windows Defender\MpCmdRun.exe" -Scan -ScanType 1`

**Per eseguire uno scan completo**   
`"%ProgramFiles%\Windows Defender\MpCmdRun.exe" -Scan -ScanType 2`

**Per eseguire uno scan al settore di boot**   
`"%ProgramFiles%\Windows Defender\MpCmdRun.exe" -Scan -ScanType -BootSectorScan`
