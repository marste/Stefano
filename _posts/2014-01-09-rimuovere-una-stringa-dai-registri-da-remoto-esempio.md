---
id: 2686
title: 'Rimuovere una stringa dai registri da remoto &#8211; Esempio'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2686
permalink: /rimuovere-una-stringa-dai-registri-da-remoto-esempio/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2102030421
categories:
  - Windows
tags:
  - chiave
  - registro
  - remoto
  - rimuovere
---
`psexec \\%1 reg delete HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v CCleaner /f`