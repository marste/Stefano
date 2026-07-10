---
title: "Configurare git per github con autenticazione 2FA su Debian Stable"
date: 2026-07-10 07:30:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/git.png'
share-img: 'https://marzorati.co/img/git.png'
layout: post
categories: [Linux]
tags: [debian, git, github, autenticazione, 2FA, gh]
---
Installa le dipendenze   

```
sudo apt update
sudo apt install -y curl gpg
```
Aggiungi la chiave GPG e il repository   

```
sudo mkdir -p -m 755 /etc/apt/keyrings
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null
sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg
```
```
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
```
Installa il pacchetto   

```
sudo apt update
sudo apt install -y gh
```
```
gh auth login
```
```
gh auth setup-git
```
```
git config --global user.email "la.tua.email@dominio.com"
git config --global user.name "Il Tuo Nome"
```
Verifica il funzionamento:   

```
git add .
git commit -m "Descrizione del commit"
git push
```
