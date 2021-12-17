---
title: "Disconnettere da remoto tutti gli utenti collegati via RDP da un Terminal Server"
date: 2021-12-17 08:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
layout: post
categories: [Windows]
tags: [logoff, all, user, terminal, server, session, script, batch, rdp, rds]
---
Ecco uno script di esempio che farà una query sul server SERVER01 per vedere tutte le sessioni aperte e le scrive nel file session1.txt.   
Da questo file prenderà l'ID della sessione e farà un logoff di questa.   
Alla fine eliminerà il file session1.txt   

~~~batch
quser /server:SERVER01 > C:\Temp\session1.txt
for /f "skip=1 tokens=3," %%i in (C:\Temp\session1.txt) DO logoff %%i /server:SERVER01
del C:\Temp\session1.txt
~~~
