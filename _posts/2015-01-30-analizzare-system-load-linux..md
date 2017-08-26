---
title: Analizzare system load su Linux
author: Stefano Marzorati
layout: post
permalink: /analizzare-system-load-linux/
comments: true
categories:
  - Linux
tags:
  - average
  - carico
  - linux
  - load
  - medio
  - sistema
---

Per vedere il carico medio del server Linux, si possono digitare questi comandi:   
- <code>uptime</code>   
- <code>w</code>   
- <code>top</code>   

Il risultato sarà tipo questo:
<pre><code>09:51:09 up 2 days, 21:46,  4 users,  load average: 1.76, 2.18, 3.37</code></pre>

Gli ultimi 3 numeri rappresentano il carico medio nell'ultimo minuto, negli ultimi 5 minuti e negli ultimi 15.

Per analizzare il carico medio, dobbiamo sapere quanti core ha la nostra CPU, con questo comando:   
<code>cat /proc/cpuinfo | grep processor | wc -l</code> oppure <code>nproc</code>

Se il carico rimane sotto questo valore, allora è tutto ok
Vorrà dire che la cpu riesce a "star dietro" a tutti i processi, se il carico diventa superiore a questo dato significa che alcuni processi sono rallentati, in quanto sono spesso in attesa che la cpu sia libera per soddisfarli.
Se il carico diventa molto superiore, e se si riflette in particolare nel 2° e 3° dato, quindi è un problema che si protrae nel tempo.

Per analizzare meglio lo stato del sistema e della cpu usiamo il comando <strong>vmstat</strong>.

Digitiamo il comando: <code>vmstat 1</code>

<pre>
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 1  0   4552 350468 8490724 49764236    0    0    16    42    7    1  1  1 97  1  0
 0  0   4552 348508 8490728 49765260    0    0   436   128 9811 22726  2  1 96  1  0
 0  0   4552 348908 8490756 49765804    0    0     0   660 12895 38834  3  1 95  0  0
 0  0   4552 348184 8490780 49766500    0    0    88   564 13221 38769  3  2 94  1  0
 0  0   4552 347660 8490788 49766956    0    0     4  4260 16405 52879  5  3 92  0  0
</pre>

r: Numero di processi in attesa di CPU. Se è spesso superiore a 2*(numero core) molto probabilmente il problema è nella CPU

b: Numero di processi bloccati (dormienti). Non stanno facendo nulla, normalmente in attesa di I/O (spesso disco), ma non è detto al 100%.

swpd: Quantità di swap usata

free: Quantità di memoria fisica libera

buff: Quantità di memoria usata per i buffer (usata per velocizzare alcune operazioni su disco)

cache: Memoria usata come cache

si: Fattore di ritorno dello swap (da disco a RAM)

so: Fattore di uscita dello swap (da RAM a disco)

bi: Scritture I/O in blocchi/secondo

bo: Letture I/O in blocchi/secondo

in: Numero di interrupt al secondo

cs: Numero di context switch al secondo

us: Percentuale di CPU impegnata in processi utente (le applicazioni)

sy: Percentuale di CPU impegnata in processi di sistema (kernel)

id: Percentuale di CPU libera

wa: Percentuale di CPU passata in attesa di I/O


Guardiamo come prima cosa la colonna "<strong>wa</strong>": se questo valore è spesso alto il problema è da ricercarsi nell'I/O (poca ram o hard disk troppo lento o con troppe operazioni), tanto che la nostra CPU è spesso bloccata in sua attesa.

In questo caso guardiamo anche le colonne relative allo swap, "si" e "so": se sono spesso sopra lo 0 significa che il sistema usa molto lo swap, e questo avviene quando finisce la memoria RAM.

In caso contrario guardiamo alla colonna "<strong>id</strong>", che ci dice quanto la CPU è "rilassata". <strong>Se è troppo spesso uguale a 0 significa che non lo è per niente, la CPU è spesso impegnata al 100%</strong> a seguire i processi di sistema (sy) o utente (us). Se il problema è nei processi di sistema si può cercare il problema in demoni di sistema o in altri processi in background di root (una causa comune è il firewall di sistema e il suo "iptable"). Se il problema è nei processi utenti conviene usare un programma come "top" per vedere qual'è il processo che sta mangiando la CPU.

<a href="http://myhq.it/analizzare-un-alto-carico-di-sistema-su-linux" target="_blank">Via Myhq.it</a>