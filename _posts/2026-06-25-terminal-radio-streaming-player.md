---
title: "Radio Streaming Terminal Player per Linux"
date: 2026-06-25 07:30:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/music.png'
share-img: 'https://marzorati.co/img/music.png'
layout: post
categories: [Linux]
tags: [debian, mpv, music, player, radio, streaming, debian]
---
Per avere un player con embedded la lista delle stazioni, scarica il file radio_player_v2_3.py e copialo con questo comando:
```
sudo wget https://marzorati.co/download/radio_player_v2_3.py -qO /usr/local/bin/radio && sudo chmod +x /usr/local/bin/radio
```

Requisito:   
```
sudo apt install mpv python3 alsa-utils
```

Esegui:   
```
radio
```   

Se invece preferisci avere il player che ha come sorgente un file esterno, dove poter aggiungere/modificare/rimuovere le stazioni radio, allora scarica questo file:   
```
sudo wget https://marzorati.co/download/radio_player.py -qO /usr/local/bin/radio && sudo chmod +x /usr/local/bin/radio
```
Il file JSON esterno dovrai renderlo raggiungibile.   
Qua di seguito l'esempio del mio file:   
```
https://marzorati.co/download/radio_stations.json
```