---
title: "Inviare email con PowerShell"
subtitle: "Usando l'SMTP di Office365"
date: 2025-01-27 10:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [email]
tags: [powershell, smtp, test, inviare, mail, send, office365, cmd, telnet]
---
Se avete bisogno di inviare email, ad esempio per eseguire un test o verificare delle credenziali di accesso, potete utilizzare PowerShell con il seguente comando di esempio:

~~~powershell
Send-MailMessage -To 'mario.rossi@acme.com' -From 'no-reply@acme.com' -Subject 'Your message subject' -Body 'Some important plain text!' -Credential (Get-Credential) -SmtpServer 'smtp.office365.com' -Port 587 -UseSsl
~~~