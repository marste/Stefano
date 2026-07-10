---
title: "Alternativa a LibreOffice, installare OnlyOffice su Debian"
date: 2026-07-10 08:30:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/office.png'
share-img: 'https://marzorati.co/img/office.png'
layout: post
categories: [Linux]
tags: [debian, office, libreoffice, onlyoffice, repository, install]
---
Scarica la chiave GPG di sicurezza:   

```
mkdir -p -m 755 /etc/apt/keyrings
wget -O- https://download.onlyoffice.com/GPG-KEY-ONLYOFFICE | gpg --dearmor | sudo tee /etc/apt/keyrings/onlyoffice.gpg > /dev/null
```
Aggiungi il repository all'elenco delle sorgenti:   

```
echo "deb [signed-by=/etc/apt/keyrings/onlyoffice.gpg] https://download.onlyoffice.com/repo/debian squeeze main" | sudo tee /etc/apt/sources.list.d/onlyoffice.list
```

Aggiorna l'indice ed esegui l'installazione:   

```
sudo apt update
sudo apt install onlyoffice-desktopeditors
```
Rimuovere LibreOffice:   

```
sudo apt purge "libreoffice*"
sudo apt autoremove --purge
sudo apt clean
rm -rf ~/.config/libreoffice
```

