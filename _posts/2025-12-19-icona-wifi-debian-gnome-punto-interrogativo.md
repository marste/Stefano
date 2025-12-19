---
title: "In Debian 13 con GNOME l'icona del WiFi compare con un punto interrogativo"
subtitle: "anche se c'è connettività"
date: 2025-12-19 10:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/linux.png'
share-img: 'https://marzorati.co/img/linux.png'
layout: post
categories: [Linux]
tags: [debian, gnome, icon, wifi, check, connettività]
---
Su Debian 13, su alcuni notebook DELL, l'icona del WiFi compare con un punto interrogativo anche se si è correttamente connessi e si naviga in internet.   
A volte riavviando il NetworkManager l'icona rimane con il simbolo corretto, ma solo in rari casi.   
Il problema è legato puramente a qualche ritardo grafico e alla verifica di connessione.   

Qua di seguito un workaround che risolve il problema:   

Verifica cosa ritorna l'endpoint di Ubuntu usato per effettuate test di connettività con questo comando:   
```
curl -I http://connectivity-check.ubuntu.com
```
se ti ritorna un **204** è ok e possiamo indicarlo per il test di connettività editando:   

```
sudo nano /etc/NetworkManager/conf.d/20-connectivity.conf
```
con questo contenuto:   

```
[connectivity]
enabled=true
uri=http://connectivity-check.ubuntu.com
interval=300
```

Salva, esci e riavvia con:   

```
sudo systemctl restart NetworkManager
```

Altri URL di connectivity check:   
- http://connectivitycheck.gstatic.com/generate_204
- http://www.gstatic.com/generate_204
- http://connectivitycheck.android.com/generate_204