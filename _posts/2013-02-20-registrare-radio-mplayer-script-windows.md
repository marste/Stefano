---
id: 1426
title: 'Script per registrare radio con MPlayer &#8211; Windows'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1426
permalink: /registrare-radio-mplayer-script-windows/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2080047448
categories:
  - Windows
---
Esempio:  
`Registra_Radio_Titolo_Minuti.cmd http://sj128.hnux.com Jazz 60`  
(registra da http://sj128.hnux.com che ha titolo &#8220;Jazz&#8221; per 60 minuti)

`for /F "tokens=2-4 delims=/ " %%i in ('date /t') do set DATEFORMATTED=%%k%%i%%j   
start "%2" /min "C:ProgrammiMPlayermplayer.exe" %1 -dumpstream   
set /a SECONDS=%3 * 60   
wait %SECONDS%   
close %2`