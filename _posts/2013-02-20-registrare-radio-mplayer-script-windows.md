---
title: 'Script per registrare web radio con MPlayer su Windows'
author: Stefano Marzorati
date: 2021-08-13 07:30:00 +0200
image: 'https://marzorati.co/img/music.png'
share-img: 'https://marzorati.co/img/music.png'
layout: post
categories: [Music]
tags: [music, mplayer, recorder, script, commandline, registrare, musica, mp3, dump]
---
Esempio:  
`Registra_Radio_Titolo_Minuti.cmd http://sj128.hnux.com Jazz 60`  
(registra da http://sj128.hnux.com che ha titolo ***Jazz*** per 60 minuti)

~~~batch
for /F "tokens=2-4 delims=/ " %%i in ('date /t') do set DATEFORMATTED=%%k%%i%%j
start "%2" /min "C:\Programmi\MPlayer\mplayer.exe" %1 -dumpstream -dumpfile "%2.mp3"
set /a SECONDS=%3 * 60
wait %SECONDS%
close %2
~~~