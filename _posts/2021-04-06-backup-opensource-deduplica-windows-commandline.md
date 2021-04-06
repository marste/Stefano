---
title: 'Restic: backup opensource con deduplica su Windows da command line'
author: Stefano Marzorati
layout: post
date: 2021-04-06 13:20:00 +0200
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [Windows]
tags: [backup, open, source, opensource, deduplica, windows, commandline, restic, veloce, sicuro, efficiente, multipiattaforma, aws, sftp, azure, google]
---

## Installa SCOOP da Powershell

~~~powershell
Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
Set-ExecutionPolicy RemoteSigned -scope CurrentUser
~~~

## Installa RESTIC

~~~powershell
scoop install restic
~~~

## Inizializza il repository

<code>restic init --repo F:\backup</code>

<u>Inserisci una password che non dovrai mai dimenticare</u>

## Esegui il BACKUP

<code>restic backup -r F:\backup C:\work D:\another_work_folder</code>

Se rilanci il backup degli stessi percorsi senza cambiare nulla, vedrete che finirà immediatamente creando una nuova snapshot.   

## Vedere la lista degli snapshot effettuati

<code>restic snapshots -r F:\backup</code>

## Vedere la lista dei files di una snapshot:

<code>restic ls -l -r F:\backup latest</code>

oppure   

<code>restic ls -l -r F:\backup 99474ce3</code>


## Esegui il Restore

<code>restic restore 47a15bab -r F:\backup --target C:\restore</code>

oppure   

<code>restic restore latest -r F:\backup --target C:\restore</code>

Restore singolo file:

<code>restic restore latest -r F:\backup --target C:\restore --include /C/TMP/ok.txt</code>

## Elimina gli snapshot

<code>restic forget --prune -r F:\backup 1ba98702</code>

## Auto Pulizia

<code>restic forget --prune --keep-daily 7 --keep-monthly 12 --keep-yearly 3 -r F:\backup</code>

## Aggiorna la versione

<code>restic self-update</code>