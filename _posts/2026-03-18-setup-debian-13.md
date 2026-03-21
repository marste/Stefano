---
title: "Setup Debian 13"
date: 2026-03-18 07:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/debian.png'
share-img: 'https://marzorati.co/img/debian.png'
layout: post
categories: [Linux]
tags: [debian, gnome, setup, install, configure, program, app]
---
**Per prima cosa installa con un unico comando, tutto questo:**   
```
sudo apt install firmware-linux firmware-linux-nonfree firmware-misc-nonfree firmware-realtek firmware-iwlwifi firmware-amd-graphics firmware-intel-sound gstreamer1.0-libav gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly ffmpeg fonts-liberation2 libavcodec-extra gnome-tweaks gnome-shell-extensions gnome-software gnome-software-plugin-flatpak flatpak gnome-shell-extension-manager fonts-cantarell fonts-dejavu fonts-liberation cups system-config-printer fastfetch screenfetch htop wget gnome-shell-extension-prefs mpv upower fzf git gh
```

**Configura il servizio di stampa per avviarsi automaticamente all’avvio del sistema**   
```
sudo systemctl enable --now cups
```

**installa strumenti utili (aggiornamenti automatici + firewall + info aggiornamenti)**
```
sudo apt install unattended-upgrades apt-listchanges gufw
```

**attiva/configura gli aggiornamenti automatici**
```
sudo dpkg-reconfigure unattended-upgrades
```

**aggiorna completamente il sistema**
```
sudo apt update && sudo apt full-upgrade -y
```

**ripulisce ciò che non serve più**
```
sudo apt autoremove --purge -y
```

**Aggiunge il repository Flathub a Flatpak, cioè la principale “app store” per applicazioni Flatpak**
```
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

**Installa queste due estensioni per Gnome:**   
[https://extensions.gnome.org/extension/4994/dash2dock-lite/](https://extensions.gnome.org/extension/4994/dash2dock-lite/)   
[https://extensions.gnome.org/extension/615/appindicator-support/](https://extensions.gnome.org/extension/615/appindicator-support/)

**Installa Spotify:**
```
curl -sS https://download.spotify.com/debian/pubkey_5384CE82BA52C83A.asc | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg
echo "deb https://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
sudo apt-get update && sudo apt-get install spotify-client
```

**Installa Better IPTV:**
[https://github.com/mewset/better-iptv/releases](https://github.com/mewset/better-iptv/releases)

**Inserisci questo URL m3u per i canali del digitale terrestre:**
[https://raw.githubusercontent.com/maginetweb-arch/TVITALIA/refs/heads/main/iptvit.m3u](https://raw.githubusercontent.com/maginetweb-arch/TVITALIA/refs/heads/main/iptvit.m3u)

**Installa Stremio, Shortwave e audiotube da Flathub**

**Installa Mega:**[https://mega.io/it/desktop](https://mega.io/it/desktop)

**Crea alias  per aggiornare tutto con il comando "aggiorna"**
```
sudo nano ~/.bash_aliases
alias aggiorna='sudo apt update && sudo apt full-upgrade -y && sudo apt autoremove --purge -y && sudo apt autoremove && sudo apt clean'
source ~/.bash_aliases
aggiorna
```

**Installare il kernel più recente**
```
echo "deb http://deb.debian.org/debian trixie-backports main" | sudo tee /etc/apt/sources.list.d/backports.list
sudo apt update
sudo apt -t trixie-backports install linux-image-amd64 linux-headers-amd64
sudo reboot
```

**Come ridurre il consumo su Debian 13**
```
sudo apt install tlp
sudo systemctl enable tlp
sudo systemctl start tlp
```