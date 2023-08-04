---
title: "Come verificare se i domain controller sono sincronizzati tra loro?"
author: Stefano Marzorati
layout: post
date: 2023-08-04 17:38:00 +0200
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories: [Windows]
tags: [domain, controller, sync, check, sincronizzati, repadmin, replsummary]
---
Accedete su un Domain Controller e digitate questo comando:   

~~~batch
repadmin /replsummary
~~~

Se è tutto OK, dovreste trovarvi nessun **Fail**.   
Se invece trovate dei **Fail** con un numero di giorni alto che indica da quanto tempo i vari DC non si sincronizzano, avete un problema a volte di non semplice risoluzione.   
