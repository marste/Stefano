---
layout: post
title: Start e Stop da cmd di un servizio Windows
date: '2020-05-25 13:10:00 +0200'
author: Stefano Marzorati
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories: [Windows]
tags: [services, servizio, start, stop, commandline]
published: true
---
Normalmente utilizziamo **services.msc** per avviare o arrestare o disabilitare o abilitare qualsiasi servizio.   
Possiamo fare lo stesso dalla riga di comando di Windows anche usando i comandi **net** e **sc**.   

Di seguito sono riportati degli esempi.   

Comando per stoppare il servizio:   
~~~batch
net stop servizio
~~~
Comando per avviare il servizio:   
~~~batch
net start servizio
~~~
Comando per disabiliare l'avvio automatico di un servizio:
~~~batch
sc config servizio start= disabled
~~~
Comando per abilitare un servizio:   
~~~batch
sc config servizio start= demand
~~~
Comando per abilitare l'avvio automatico di un servizio:
~~~batch
sc config servicename start= auto
~~~