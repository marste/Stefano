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
	Server: GitHub.com
	Content-Type: text/html; charset=utf-8
	Last-Modified: Thu, 23 Jul 2015 20:23:09 GMT
	Access-Control-Allow-Origin: *
	Expires: Thu, 23 Jul 2015 21:14:32 GMT
	Cache-Control: max-age=600
	Content-Length: 6139
	Accept-Ranges: bytes
	Date: Thu, 23 Jul 2015 21:04:32 GMT
	Via: 1.1 varnish
	Age: 0
	Connection: keep-alive
	X-Served-By: cache-lhr6321-LHR
	X-Cache: MISS
	X-Cache-Hits: 0
	X-Timer: S1437685472.532988,VS0,VE105
	Vary: Accept-Encoding
	
O in altri casi più semplici, un risultato simile:   

	HTTP/1.1 200 OK
	Date: Thu, 23 Jul 2015 20:52:02 GMT
	Server: Apache
	Content-Type: text/html
	X-Powered-By: PHP/5.5.9-1ubuntu4.11
	Expires: Thu, 19 Nov 1981 08:52:00 GMT
	Cache-Control: no-store, no-cache, must-revalidate, post-check=0, pre-check=0
	Pragma: no-cache
	X-Ants-Machine-Id: php02
	X-Ants-Host: nginx01
	Set-Cookie: PHPSESSID=9ofov1hcc8fdv2c3h6ubm0l122; path=/
	Vary: Accept-Encoding
	Set-Cookie: HASH_PHPSESSID=05DEA1665720FA9F0B5F85DFF23A8AB2F87BA2DE; path=/
	Content-Length: 129231
	Keep-Alive: timeout=15, max=100
	Connection: Keep-Alive