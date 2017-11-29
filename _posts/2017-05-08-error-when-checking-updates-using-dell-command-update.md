---
title: Error when checking for updates using Dell Command Update
date: 2017-05-08 14:00:00 +0200
author: Stefano Marzorati
image: 'https://www.vouchercodes.co.uk/static/v10/images/merchant/logo/128px/278_170913182442.png'
share-img: 'https://www.vouchercodes.co.uk/static/v10/images/merchant/logo/128px/278_170913182442.png'
layout: post
permalink: /error-when-checking-updates-using-dell-command-update/
categories:
  - Windows
tags:
  - windows
  - dell
  - command
  - update
  - error
  - catalog
  - GUI-UVM15
---
Se cercando di aggiornare il vostro PC con il Dell Command Update quest'ultimo va in errore con il seguente messaggio:   

**Error when checking for updates using Dell Command Update** e nei dettagli dell'errore mi riporta il codice **GUI-UVM15**

Dal prompt dei comandi digitate:   

<code>del /Q/F/S %TEMP%\*</code>