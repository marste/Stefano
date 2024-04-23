---
title: "Testare la velocità effettiva di una rete con NTTTCP"
date: 2024-04-23 10:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/network.png'
share-img: 'https://marzorati.co/img/network.png'
layout: post
categories: [network]
tags: [test, speed, velocità, rete, network, ntttcp, iperf]
---
Per testare e valutare la velocità e le prestazioni di una rete in condizioni controllate e riproducibili, uno strumento molto utile può essere questo tool Microsoft che si chiama **NTTTCP**.

Per attivare il modulo server di <a href="https://github.com/microsoft/ntttcp/releases" target="_blank">NTTTCP</a>, si può usare la sintassi seguente:

~~~batch
ntttcp.exe -r -m 4,*,192.168.0.10 -t 20
~~~

La prima opzione -r specifica l’avvio del server ntttcp; -m 4,*,<IP> indica il numero di thread utilizzati (in questo caso, quattro threads); l’asterisco (*) esprime nessuna affinità CPU specifica ovvero che il processo può essere eseguito su qualunque core. L’ultima opzione -t 20 indica la durata del test, espressa in secondi.

Lato client, il seguente comando invierà il traffico di rete verso l’IP del server ntttcp specificato:

~~~batch
ntttcp.exe -s -m 4,*,192.168.0.10 -t 20
~~~
