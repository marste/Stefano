---
title: Google Chrome Deploy
subtitle: Download Chrome .msi
author: Stefano Marzorati
layout: post
published: true
date: 2019-06-13 10:45:00 +0200
permalink: /google-chrome-deploy/
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories:
  - Windows
---
Scarica il file .msi da:  
<a href="https://cloud.google.com/chrome-enterprise/browser/download/" target="_blank">https://cloud.google.com/chrome-enterprise/browser/download/</a>

	xcopy "\\Server\Software\Windows\Utility\Chrome\Google\GoogleChromeStandaloneEnterprise64.msi" "\\%1C$\Temp*.*" /r/i/c/h/k/e   
	psexec \\%1 -s -d msiexec /i  "C:\Temp\GoogleChromeStandaloneEnterprise64.msi" /qn