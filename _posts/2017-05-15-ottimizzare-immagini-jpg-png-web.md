---
title: Ottimizzare immagini per il Web
date: 2017-05-15 11:00:00 +0200
author: Stefano Marzorati
layout: post
permalink: /ottimizzare-immagini-jpg-png-web/
categories:
  - Web
tags:
  - ottimizzare
  - immagini
  - web
  - jpegtran
  - command
  - line
  - optipng
  - jpg
  - png
---
<a href="http://jpegclub.org/jpegtran/" target="_blank">Download jpegtran</a>   

Esempio per files JPG:   
<code>jpegtran -copy none -optimize -progressive -outfile output.jpg input.jpg</code>   


<a href="http://optipng.sourceforge.net/" target="_blank">Download optipng</a>   

Esempio per files PNG:   
<code>optipng -o7 -strip all -out output.png input.png</code>   


Se avete molti files da ottimizzare, potete creare un semplice batch:   

<code>@echo off</code>   
<code>echo Optimizing JPEG ^& PNG Images...</code>   
<code>forfiles /s /m *.jpg /c "cmd /c @\"C:\Batch\jpegtran.exe\" -copy none -optimize -progressive -outfile @file @file"</code>   
<code>forfiles /s /m *.png /c "cmd /c @\"C:\Batch\optipng.exe\" -o7 -strip all @file"</code>   
<code>echo. & echo Process done!</code>   
<code>pause</code>   
