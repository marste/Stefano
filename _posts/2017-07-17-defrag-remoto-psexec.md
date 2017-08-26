---
title: Defrag remoto con psexec
date: 2017-07-17 12:00:00 +0200
author: Stefano Marzorati
layout: post
permalink: /defrag-remoto-psexec/
categories:
  - Windows
tags:
  - defrag
  - remote
  - remoto
  - psexec
  - log
  - script
---
**Analisi defrag:**   
<code>psexec \\nome_pc defrag c: -a >> log_analisi.txt 2>&1</code>   

**Esegui defrag:**   
<code>psexec \\nome_pc defrag c: >> log_defrag.txt 2>&1</code>   
