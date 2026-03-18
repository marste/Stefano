---
title: "Verifica lo stato di salute e capacità di una batteria di un notebook su Debian 13"
date: 2026-03-18 07:30:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/debian.png'
share-img: 'https://marzorati.co/img/debian.png'
layout: post
categories: [Linux]
tags: [debian, batteria, verifica, capacity, capacità, energy, design]
---
Installa upower (se non c’è già):
```
sudo apt install upower
```

Esegui:    
```
upower -i $(upower -e | grep BAT)
```
Guarda il valore di **Capacity**   

Se vedi:
* 95–100% → batteria ottima
* 80–95% → buona
* 60–80% → usurata
* <60% → da sostituire
   

In alternativa leggendo i dati direttamente dal kernel:   
```
cat /sys/class/power_supply/BAT0/capacity
```
E calcoli:   
```
capacità % = (energy_full / energy_full_design) × 100
```