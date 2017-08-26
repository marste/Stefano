---
id: 2701
title: Rimuovere da remoto Microsoft .NET Framework 1.1
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2701
permalink: /rimuovere-da-remoto-microsoft-net-framework-1-1/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2125171929
categories:
  - Windows
tags:
  - disinstallare
  - key
  - programma
  - registry
  - remote
  - uninstall
---
`psexec -s -d \\nomepc MsiExec.exe /qn /x {CB2F7EDD-9D1F-43C1-90FC-4F52EAE172A1}`

La stringa la trovi nei registri:  
`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall`

Cerchi il prodotto da disinstallare e noterai la chiave di registro con la stringa di uninstall.