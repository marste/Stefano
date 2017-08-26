---
id: 2879
title: Abilitare il Trim sui dischi SSD in Windows 7
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2879
permalink: /abilitare-il-trim-sui-dischi-ssd-in-windows-7/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2812072885
categories:
  - Windows
tags:
  - ssd
  - trim
---
- Aprire **cmd** in modalità amministratore  
&#8211; Digitare: `fsutil behavior query DisableDeleteNotify`  
Se il risultato è **0 = Trim abilitato**  
Se il risultato è **1 = Trim disabilitato**

&#8211; Per abilitare il Trim, digitate:  
`fsutil behavior set disablenotify 0`

Il comando TRIM si può abilitare su Windows 7, Windows Server 2008 R2 e il controller del disco deve essere impostato in modalità AHCI.