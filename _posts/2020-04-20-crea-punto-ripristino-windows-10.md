---
title: "Crea punto di ripristino in Windows 10"
subtitle: "Ripristino configurazione di sistema"
date: 2020-04-20 11:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories: [Backup]
tags: [backup, punto, ripristino, windows, configurazione]
---
Per abilitare **Ripristino configurazione di sistema** in Windows 10 occorre digitare da PowerShell aperta con i diritti di amministratore, quanto segue:   

~~~powershell
Enable-ComputerRestore -drive "C:\"
vssadmin resize shadowstorage /on=c: /for=c: /maxsize=4%
~~~

Per creare al volo un **punto di ripristino**, basta digitare:   

~~~powershell
Checkpoint-Computer "Nome del punto di ripristino"
~~~

Se volessi ripristinare un punto di ripristino, basterà digitare:   

~~~powershell
rstrui
~~~