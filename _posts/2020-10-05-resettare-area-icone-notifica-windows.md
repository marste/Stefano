---
title: "Area di notifica con spazi vuoti in Windows 10"
subtitle: Reset cache icone
author: Stefano Marzorati
date: 2020-10-05 12:40:00 +0200
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
layout: post
categories:
  - windows
tags:
  - reset
  - icone
  - notifica
  - cache
  - regedit
  - area
  - notification
  - windows10
---
L'area di notifica si trova all'estremità destra della barra delle applicazioni e contiene icone di app e di sistema che forniscono lo stato e le notifiche su cose come la posta in arrivo, gli aggiornamenti e la connettività di rete.

A volte la cache delle icone dell'area di notifica potrebbe danneggiarsi causando la visualizzazione errata o distorta delle icone e continuare a mostrare le icone delle app disinstallate nelle impostazioni delle icone dell'area di notifica. Quando ciò accade, le icone dell'area di notifica devono essere eliminate dal registro per ripristinarle e ricrearle automaticamente.

La cache delle icone dell'area di notifica per ogni account utente si trova come valori binari di IconStreams e PastIconsStream nella chiave di registro di seguito.

<code>HKEY_CURRENT_USER\SOFTWARE\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\TrayNotify</code>

Potete resettare le icone nell'area di notifica, <a href="https://marzorati.co/download/Reset_Notification_Area_Icons_Cache.bat" target="_blank">cliccando su questo batch</a> che eseguira questi comandi:   

~~~batch
@echo off

set regPath=HKCU\Software\Classes\Local Settings\Software\Microsoft\Windows\CurrentVersion\TrayNotify
set regKey1=IconStreams
set regKey2=PastIconsStream


echo.
echo The Explorer process must be temporarily killed before deleting your notification area icons cache. 
echo.
echo Please SAVE ALL OPEN WORK before continuing.
echo.
pause


echo.
taskkill /IM explorer.exe /F
echo.
FOR /F "tokens=*" %%a in ('Reg Query "%regpath%" /v %regkey1% ^| find /i "%regkey1%"') do goto IconStreams
echo Registry key "IconStreams" already deleted.
echo.

:verify-PastIconsStream
FOR /F "tokens=*" %%a in ('Reg Query "%regpath%" /v %regkey2% ^| find /i "%regkey2%"') do goto PastIconsStream
echo Registry key "PastIconsStream" already deleted.
echo.
goto restart

:IconStreams
reg delete "%regpath%" /f /v "%regkey1%"
goto verify-PastIconsStream

:PastIconsStream
reg delete "%regpath%" /f /v "%regkey2%"


:restart
echo.
echo.
echo You will need to restart the PC to finish resetting your notification area icons.
echo.
CHOICE /C:YN /M "Do you want to restart the PC now?"
IF ERRORLEVEL 2 goto no
IF ERRORLEVEL 1 goto yes


:no
echo.
echo.
echo Restarting explorer.... 
echo.
echo Please remember to restart the PC later to finish resetting your notification area icons.
echo.
start explorer.exe
pause
exit /B

:yes
shutdown /r /f /t 00
~~~


