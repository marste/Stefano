---
id: 1828
title: Deploy Skype .msi
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1828
permalink: /deploy-skype-msi/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1909957291
categories:
  - Windows
tags:
  - business
  - deploy
  - installer
  - msi
  - skype
  - Windows
---
Download from:  
<a href="http://www.skype.com/go/getskype-msi" target="_blank">http://www.skype.com/go/getskype-msi</a>

Script:  
`xcopy "\\Server\Skype\SkypeSetup.msi" "\\%1C$\Temp*.*" /r/i/c/h/k/e`   
`psexec \\%1 -s -d msiexec /i  "C:\Temp\SkypeSetup.msi" /qn /norestart`