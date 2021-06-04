---
title: 'Installare e utilizzare WinGet su Windows 10'
author: Stefano Marzorati
layout: post
date: 2021-06-04 13:25:00 +0200
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories: [Windows]
tags: [winget, installare, commandline, applicazioni, github, usare]
---
Andare sul sito <a href="https://github.com/microsoft/winget-cli/releases" target="_blank">https://github.com/microsoft/winget-cli/releases</a> e scaricare il file **Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.appxbundle**.

Una volta scaricato e installato, aprire il prompt dei comandi e digitare:   

<code>winget install</code>

Poi sarà possibile ricercare i programmi da installare digitando:   

<code>winget search nome_programma</code>

e installarlo digitando:   

<code>winget install nome_programma</code>

Sarà possibile creare anche un batch per poter installare in automatico varie applicazioni, ecco un esempio:

~~~batch
@echo off  
Echo Install Powertoys and Terminal  
REM Powertoys  
winget install Microsoft.Powertoys  
if %ERRORLEVEL% EQU 0 Echo Powertoys installed successfully.  
REM Terminal  
winget install Microsoft.WindowsTerminal  
if %ERRORLEVEL% EQU 0 Echo Terminal installed successfully.   %ERRORLEVEL%
~~~