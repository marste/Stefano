---
title: Abilita o disabilita UAC da command line
date: 2017-05-05 14:00:00 +0200
author: Stefano Marzorati
layout: post
permalink: /abilita-disabilita-uac-command-line/
categories:
  - Windows
tags:
  - windows
  - enable
  - disable
  - uac
  - command
  - line
  - change
  - user
  - account
  - control
---
**Disabilita UAC:**   

<code>C:\Windows\System32\cmd.exe /k %windir%\System32\reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 0 /f</code>   

**Abilita UAC:**   

<code>C:\Windows\System32\cmd.exe /k %windir%\System32\reg.exe ADD HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f</code>