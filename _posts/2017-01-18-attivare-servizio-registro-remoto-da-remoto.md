---
title: Attivare servizio registro di sistema remoto da remoto
date: 2017-01-18 12:00:00 +0200
author: Stefano Marzorati
layout: post
permalink: /attivare-servizio-registro-remoto-da-remoto/
categories:
  - Windows
tags:
  - start
  - RemoteRegistry
  - remote
  - commandline
  - registro
  - remoto
---
Se dovete collegarvi al registro di un PC remoto, occorre che su tale PC sia attivo il servizio **RemoteRegistry**.   

Potete avviarlo da remoto con il seguente commando:   

<code>psservice \\nome_pc start RemoteRegistry</code>