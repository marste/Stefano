---
title: Delete Wi-Fi profiles from command line
date: 2016-12-13 17:42:00 +0200
author: Stefano Marzorati
layout: post
image: 'http://marzorati.co/img/wifi.png'
share-img: 'http://marzorati.co/img/wifi.png'
permalink: /delete-wifi-profile-command-line/
categories:
  - Windows
tags:
  - delete
  - remove
  - wifi
  - profile
  - commandline
  - netsh
---
Innanzitutto verifichiamo quali profili WiFi son memorizzati sul PC:   

<code>netsh wlan show profiles</code>

Una volta identificato il profilo da eliminare, digita il comando:   

<code>netsh wlan delete profile name="WIFI_DA_ELIMINARE"</code>