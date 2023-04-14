---
title: Verificare se esiste un indirizzo email
author: Stefano Marzorati
layout: post
date: 2023-04-14 07:25:00 +0200
image: 'https://marzorati.co/img/mail.png'
share-img: 'https://marzorati.co/img/mail.png'
categories: [email]
tags: [address, email, verificare, telnet, mail, rcpt, indirizzo, test, recipient, user]
---
**nslookup**  
**set type=mx**  
**dominio.it**

ti annoti l&#8217;mx principale (in questo caso facciamo che sia il seguente)  
**out.mail.it**

~~~batch
**telnet out.mail.it 25**  
**helo dominio.it**   
**AUTH LOGIN**   
**MAIL FROM:<your_email_address>**   
**RCPT TO:<destination_email_address>**   
~~~

Se l&#8217;utente esiste **&#8220;Recipient ok&#8221;**  
Se l&#8217;utente non esiste **&#8220;No such user&#8221;**