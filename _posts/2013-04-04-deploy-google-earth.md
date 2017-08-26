---
id: 1494
title: Deploy Google Earth
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1494
permalink: /deploy-google-earth/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2278290029
categories:
  - Windows
---
- Installa Google Earth su un pc  
&#8211; Copia il contenuto di questa directory in rete (ex. &#8220;\ServerUtilityGoogleEarth&#8221;):  
`C:Documents and SettingsUtenteImpostazioni localiTemp;._msige61`

Script:  
`xcopy "\ServerUtilityGoogleEarth*.*" "\%1C$TempGoogleEarth*.*" /r/i/c/h/k/e   
psexec \%1 -s -d msiexec /i  "C:TempGoogleEarthGoogle Earth.msi" /qn /norestart`