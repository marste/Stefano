---
title: "Installare e configurare il client VPN di Forcepoint su Debian"
date: 2026-07-31 07:30:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/network.png'
share-img: 'https://marzorati.co/img/network.png'
layout: post
published: false
categories: [Linux]
tags: [vpn, forcepoint, client, debian, cli]
---
**Installa il pacchetto .deb:**   

```
sudo apt install forcepoint-client_2.7.0-20260318+trixie_amd64.deb
```

**Crea alias per avviare la connessione VPN:**

```
sudo nano ~/.bash_aliases
alias vpn=''
source ~/.bash_aliases
vpn
```
