---
id: 1428
title: Google Chrome Deploy
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1428
permalink: /google-chrome-deploy/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:24;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:24;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1983835518
categories:
  - Windows
---
Scarica il file .msi da:  
<a href="https://www.google.com/intl/en/chrome/business/browser/admin/" target="_blank">https://www.google.com/intl/en/chrome/business/browser/admin/</a>

`xcopy "\Server\Software\Windows\Utility\Chrome\Google\ChromeStandaloneEnterprise.msi" "\%1C$Temp*.*" /r/i/c/h/k/e   
psexec \%1 -s -d msiexec /i  "C:\Temp\GoogleChromeStandaloneEnterprise.msi" /qn`