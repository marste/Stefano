---
title: "Invoke-WebRequest : The request was aborted: Could not create SSL/TLS secure channel"
date: 2024-06-10 07:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
layout: post
categories: [powershell]
tags: [invoke, WebRequest, request, aborted, create, SSL, TLS, secure, channel, error]
---
Se digitando il seguente comando powershell di esempio:

~~~powershell
Invoke-WebRequest -Uri https://your.url.raw.githubusercontent.com/blablabla.../
~~~

Avete l'errore:

~~~powershell
Invoke-WebRequest : The request was aborted: Could not create SSL/TLS secure channel.
~~~

Prima del comando, digitate:   

~~~powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
~~~