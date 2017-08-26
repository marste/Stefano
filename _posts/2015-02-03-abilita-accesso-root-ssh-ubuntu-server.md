---
title: Abilita accesso SSH all'utente root su Ubuntu Server
author: Stefano Marzorati
layout: post
permalink: /abilita-accesso-root-ssh-ubuntu-server/
comments: true
categories:
  - Linux
tags:
  - abilita
  - accesso
  - ssh
  - root
  - ubuntu
---

Cambia la password dell'utente di root con il comando:   
<code>sudo passwd root</code>

Edita il file seguente:   
<code>sudo nano /etc/ssh/sshd_config</code>

Commenta la seguente riga:   
<code># PermitRootLogin without-password</code>

Aggiungi questa riga:   
<code>PermitRootLogin yes</code>

Riavvia il servizio SSH

<code>sudo service ssh reload</code>   
oppure   
<code>sudo service ssh restart</code>
