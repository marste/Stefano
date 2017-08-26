---
id: 2485
title: Creare un utente con privilegi di root
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2485
permalink: /creare-un-utente-con-privilegi-di-root/
layout_key:
  - 
post_slider_check_key:
  - 0
dsq_thread_id:
  - 1924145841
categories:
  - Linux
tags:
  - aggiungi
  - crea
  - privilegi
  - root
  - user
---
**Crea un nuovo utente:**  
`useradd amministratore`

**Imposta una password per il nuovo utente:**  
`passwd amministratore`

**Edita questo file:**  
`nano /etc/sudoers`

**Vai alla linea *\## Allow root to run any commands anywhere* e aggiungi il tuo utente:**  
`amministratore ALL=(ALL) ALL`