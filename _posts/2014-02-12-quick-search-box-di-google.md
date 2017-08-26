---
id: 2738
title: Quick Search Box di Google
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2738
permalink: /quick-search-box-di-google/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2256770967
categories:
  - Windows
tags:
  - box
  - google
  - quick
  - search
---
Se cercate ancora l&#8217;introvabile tool &#8220;Quick Search Box&#8221; di Google, ve lo allego:  
[Quick Search Box][1]

Se volete farlo avviare all&#8217;avvio, ecco un esempio da aggiungere al registry:  
`reg.exe add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v "Quick Search Box" /t REG_SZ /d "C:\Batch\Quick Search Box\GoogleQuickSearchBox.exe /autorun"`

Se lo volete fare a mano, aprite regedit:  
- `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`  
- Aggiungi la stringa: `Quick Search Box`  
- Con valore: `C:\Batch\Quick Search Box\GoogleQuickSearchBox.exe /autorun`

 [1]: http://marzorati.co/download/Quick-Search-Box.zip