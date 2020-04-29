---
title: Trovare su che porta è collegato un certo device conoscendo solo l'IP address
author: Stefano Marzorati
layout: post
date: 2020-04-29 16:00:00 +0200
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories: [networking]
tags: [arp, find, mac address, trovare, porta, switch]
published: true
---
Una volta che avete individuato l'indirizzo IP e lo pingate, digitate semplicemente il comando:
~~~telnet
arp -a
~~~
Nella lista di IP ci sarà anche quello che cercate con il suo relativo **MAC ADDRESS**.

Se volete avere più informazioni inerenti a quel <a href="https://macvendors.com/" target="_blank">MAC ADDRESS</a>, ad esempio il **produttore della scheda di rete**.   
Poi collegatevi sullo switch Cisco che fa da centro stella e digitate:   

~~~telnet
show mac address-table address 6400.6a16.3f4c
~~~

Avrete una risposta che vi indica su quale porta trova quel mac address:   
~~~telnet
Gi1/0/5
~~~

A questo punto digitate:   

~~~telnet
show cdp neighbors
~~~

e vi verrà mostrato lo switch successivo da cui passare per arrivare a quel mac-address.   
Andate avanti così finchè non lo troverete su una porta che non è una porta di rilancio.   

