---
id: 2707
title: Script per ascoltare radio con mplayer
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2707
permalink: /script-per-ascoltare-radio-con-mplayer/
dsq_thread_id:
  - 2170313924
categories:
  - Windows
tags:
  - listen
  - mplayer
  - radio
  - script
  - Windows
---
<code>
@ECHO OFF   
CLS   
:LOOP   
ECHO 1) Radio Planet   
ECHO 2) Radio DeeJay   
ECHO 3) Radio 24   
ECHO 4) Smoothjazz.com   
ECHO 5) Venus Radio Mykonos   
ECHO 6) m2o   
ECHO 7) Hardcoreradio.nl   
ECHO 8) Hot Mix Radio 80   
ECHO 9) Radio Party Groove   
ECHO 10) Razor FM   
ECHO 11) Radio 538 IBIZA   
ECHO 12) PulsRadio 80   
ECHO 13) ----------   
ECHO 14) SKY.FM 80   
ECHO 15) ----------   
ECHO 16) ----------   
ECHO 17) ----------   
ECHO 18) ----------   
ECHO 19) Classica   
ECHO 20) Solo Piano   
ECHO.   
ECHO e) Esci   
:: SET /P prompts for input and sets the variable   
:: to whatever the user types   
ECHO.   
SET Choice=   
SET /P Choice=Scegli la radio che vuoi ascoltare e premi INVIO:   
:: The syntax in the next line extracts the substring   
:: starting at 0 (the beginning) and 1 character long   
IF NOT '%Choice%'=='' SET Choice=%Choice:~0,2%   
ECHO.   
:: /I makes the IF comparison case-insensitive   
IF /I '%Choice%'=='1' GOTO Item1   
IF /I '%Choice%'=='2' GOTO Item2   
IF /I '%Choice%'=='3' GOTO Item3   
IF /I '%Choice%'=='4' GOTO Item4   
IF /I '%Choice%'=='5' GOTO Item5   
IF /I '%Choice%'=='6' GOTO Item6   
IF /I '%Choice%'=='7' GOTO Item7   
IF /I '%Choice%'=='8' GOTO Item8   
IF /I '%Choice%'=='9' GOTO Item9   
IF /I '%Choice%'=='10' GOTO Item10   
IF /I '%Choice%'=='11' GOTO Item11   
IF /I '%Choice%'=='12' GOTO Item12   
IF /I '%Choice%'=='13' GOTO Item13   
IF /I '%Choice%'=='14' GOTO Item14   
IF /I '%Choice%'=='15' GOTO Item15   
IF /I '%Choice%'=='16' GOTO Item16   
IF /I '%Choice%'=='17' GOTO Item17   
IF /I '%Choice%'=='18' GOTO Item18   
IF /I '%Choice%'=='19' GOTO Item19   
IF /I '%Choice%'=='20' GOTO Item20   
IF /I '%Choice%'=='e' GOTO End   
ECHO "%Choice%" Ma cosa cazzo hai scelto? Riprova va...   
ECHO.   
GOTO Loop   
:Item1   
mplayer http://91.121.104.139:8100   
GOTO Again   
:Item2   
mplayer http://mp3.kataweb.it:8000/RadioDeejay   
GOTO Again   
:Item3   
mplayer http://shoutcast.radio24.it:8000/   
GOTO Again   
:Item4   
mplayer http://sj128.hnux.com   
GOTO Again   
:Item5   
mplayer http://s7.onweb.gr:8410/   
GOTO Again   
:Item6   
mplayer https://radiom2o-lh.akamaihd.net/i/RadioM2o_Live_1@42518/index_96_a-b.m3u8?sd=10&rebase=on   
GOTO Again   
:Item7   
mplayer http://shoutcast2.hardcoreradio.nl   
GOTO Again   
:Item8   
mplayer http://wma.hotmixradios.net/hotmixradio80?MSWMExt=.asf   
GOTO Again   
:Item9   
mplayer http://stream12.top-ix.org:80/partygroove   
GOTO Again   
:Item10   
mplayer http://radio.razorfm.nl:443/   
GOTO Again   
:Item11   
mplayer http://82.201.100.9:8000/WEB19_WEB_MP3   
GOTO Again   
:Item12   
mplayer http://stream80.pulsradio.com:6000   
GOTO Again   
:Item13   
mplayer ------------   
GOTO Again   
:Item14   
mplayer http://pub2.sky.fm/sky_the80s_aacplus   
GOTO Again   
:Item15   
mplayer ------------   
GOTO Again   
:Item16   
mplayer ------------   
GOTO Again   
:Item17   
mplayer ------------   
GOTO Again   
:Item18   
mplayer ------------   
GOTO Again:   
:Item19   
mplayer http://222.122.131.58:6400   
GOTO Again   
:Item20   
mplayer http://stream-76.shoutcast.com:80/piano_skyfm_mp3_96kbps   
GOTO Again   
:Again   
PAUSE   
CLS   
GOTO Loop   
:End
</code>