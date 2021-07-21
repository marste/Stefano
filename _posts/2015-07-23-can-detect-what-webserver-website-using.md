---
title: Come posso sapere quale webserver un sito web sta utilizzando?
date: 2021-07-21 09:00:00 -07:00
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/web.png'
share-img: 'https://marzorati.co/img/web.png'
categories: [webserver]
tags: [webserver, website, version, apache, linux, nginx, curl, server, header]
---
Puoi semplicemente digitare:   
`curl -I https://marzorati.co`   
e otterrai un risultato con queste informazioni:   

	HTTP/1.1 200 OK
	Connection: keep-alive
	Content-Length: 12352
	Server: GitHub.com
	Content-Type: text/html; charset=utf-8
	Last-Modified: Tue, 20 Jul 2021 07:28:30 GMT
	Access-Control-Allow-Origin: *
	ETag: "60f67b1e-3040"
	expires: Wed, 21 Jul 2021 07:31:57 GMT
	Cache-Control: max-age=600
	x-proxy-cache: MISS
	X-GitHub-Request-Id: 5570:5467:1BE4DD:1D99E8:60F7CB15
	Accept-Ranges: bytes
	Date: Wed, 21 Jul 2021 07:21:57 GMT
	Via: 1.1 varnish
	Age: 0
	X-Served-By: cache-mxp6975-MXP
	X-Cache: MISS
	X-Cache-Hits: 0
	X-Timer: S1626852118.747827,VS0,VE95
	Vary: Accept-Encoding
	X-Fastly-Request-ID: e261f5ea96bc0c3ecd1d78effeb7f99c1adf6a09
	
O in altri casi più semplici, un risultato simile:   

	HTTP/1.1 200 OK
	Server: nginx
	Date: Wed, 21 Jul 2021 07:23:25 GMT
	Content-Type: text/html; charset=UTF-8
	Connection: keep-alive
	Vary: Accept-Encoding
	X-Dck: 01