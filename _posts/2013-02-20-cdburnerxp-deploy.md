---
id: 1430
title: CdBurnerXP Deploy
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1430
permalink: /cdburnerxp-deploy/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:24;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:24;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2176589650
categories:
  - Windows
tags:
  - cdburnerxp
  - deploy
  - remote
---
`psexec \%1 -s -d "C:ProgrammiCDBurnerXPunins000.exe" /VERYSILENT   
sleep 15   
xcopy "\ServerSoftwareWindowsUtilityCDBurnerXPcdbxp_setup_4.5.0.3685.exe" "\%1C$Temp*.*" /r/i/c/h/k/e   
psexec \%1 -s -d "C:Tempcdbxp_setup_4.5.0.3685.exe" /VERYSILENT`