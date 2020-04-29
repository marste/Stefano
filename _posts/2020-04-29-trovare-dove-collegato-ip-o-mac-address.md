---
title: Scoprire MAC ADDRESS di un device remoto
author: Stefano Marzorati
layout: post
date: 2020-04-29 16:00:00 +0200
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories: [networking]
tags: [arp, find, mac address, trovare]
published: false
---
Una volta che avete individuato l&#8217;indirizzo IP e lo pingate, digitate semplicemente il comando:

`arp -a`

Nella lista di IP ci sarà anche quello che cercate con il suo relativo **MAC ADDRESS**.

Se volete avere più informazioni inerenti a quel MAC ADDRESS, ad esempio il **produttore della scheda di rete**, andate sul sito:

<a href="https://macvendors.com/" target="_blank">https://macvendors.com/</a>



dal centro stella
show mac address-table address 6400.6a16.3f4c
mi dice Gi1/0/5
show cdp neighbors

vai avanti finchè non lo trovi su una porta che non è una porta di rilancio
