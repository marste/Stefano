---
title: "Installare Firefox da repository su Debian Stable"
date: 2026-07-06 07:30:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/firefox.png'
share-img: 'https://marzorati.co/img/firefox.png'
layout: post
categories: [Linux]
tags: [debian, firefox, repository, key, update, release, last]
---
Mozilla mette a disposizione un repository APT ufficiale.   
In questo modo Firefox viene aggiornato con apt come gli altri pacchetti, senza dover usare script o installazioni manuali.   

Crea la directory per le chiavi:   
```
sudo install -d -m 0755 /etc/apt/keyrings
```

Scarica la chiave Mozilla:   
```
wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | \
sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null
```   

Aggiungi il repository:
```
echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | \
sudo tee /etc/apt/sources.list.d/mozilla.list
```

Imposta una priorità alta:
```
echo '
Package: *
Pin: origin packages.mozilla.org
Pin-Priority: 1000
' | sudo tee /etc/apt/preferences.d/mozilla
```

Aggiorna e installa:
```
sudo apt update && sudo apt install firefox
```

Rimuovi Firefox ESR:
```
sudo apt remove firefox-esr
sudo apt autoremove
```