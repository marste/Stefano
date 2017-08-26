---
id: 2888
title: Configurare un Tunnel SSH
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2888
permalink: /configurare-un-tunnel-ssh/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2826542337
categories:
  - Linux
  - Windows
tags:
  - ssh
  - tunnel
  - vnc
  - vncviewer
---
Prima di tutto abbiamo bisogno di <a href="http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html" title="Putty" target="_blank">Putty:</a> e di <a href="https://www.realvnc.com/download/viewer/" target="_blank">Vnc Viewer</a>

Creiamo la connessione al server a cui vogliamo collegarci in remoto:

[<img src="http://res.cloudinary.com/marzorati-co/image/upload/v1408107869/tunnel_ssh_1_bm7hce.jpg" alt="tunnel_ssh_1" class="aligncenter size-full wp-image-2889" />][1]

Andiamo sotto **Connection** &#8211; **SSH** &#8211; **Tunnels** e aggiungiamo la **Source Port** a **5900** e la **Destination** con lo stesso indirizzo del server, ma con la **porta 5901**.

[<img src="http://res.cloudinary.com/marzorati-co/image/upload/v1408107868/tunnel_ssh_2_m2vqpw.jpg" alt="tunnel_ssh_2" class="aligncenter size-full wp-image-2890" />][2]

Se vogliamo, salviamo la connessione e la facciamo partire.  
Ci logghiamo con user e password sul server:

[<img src="http://res.cloudinary.com/marzorati-co/image/upload/v1408107867/tunnel_ssh_4_rkmpqr.jpg" alt="tunnel_ssh_4" class="aligncenter size-full wp-image-2891" />][3]

A questo punto lanciamo vncviewer e digitiamo come VNC Server: **localhost**

[<img src="http://res.cloudinary.com/marzorati-co/image/upload/v1408107866/tunnel_ssh_3_mmsnxb.jpg" alt="tunnel_ssh_3" class="aligncenter size-full wp-image-2892" />][4]

Se è stato fatto tutto correttamente si aprirà il desktop del server remoto.

 [1]: http://res.cloudinary.com/marzorati-co/image/upload/v1408107869/tunnel_ssh_1_bm7hce.jpg
 [2]: http://res.cloudinary.com/marzorati-co/image/upload/v1408107868/tunnel_ssh_2_m2vqpw.jpg
 [3]: http://res.cloudinary.com/marzorati-co/image/upload/v1408107867/tunnel_ssh_4_rkmpqr.jpg
 [4]: http://res.cloudinary.com/marzorati-co/image/upload/v1408107866/tunnel_ssh_3_mmsnxb.jpg