---
title: 'Download Office365 Enterprise Offline'
author: Stefano Marzorati
layout: post
date: 2021-03-31 13:20:00 +0200
image: 'https://marzorati.co/img/office.png'
share-img: 'https://marzorati.co/img/office.png'
categories: [Office]
tags: [office, deployment, tool, pacchetto, microsoft, configuration]
---
* Andare sul sito <a href="https://config.office.com/deploymentsettings" target="_blank">https://config.office.com/deploymentsettings</a> scegliere l'architettura e gli applicativi da scaricare e alla fine esportare il tutto nel file .xml, chiamandolo **mia_configurazione.xml**   

* Scaricare l'**Office Deployment Tool** dal sito <a href="https://www.microsoft.com/en-us/download/confirmation.aspx?id=49117" target="_blank">https://www.microsoft.com/en-us/download/confirmation.aspx?id=49117</a>   

estrarre i files in una cartella e ti troverai un **setup.exe**, **configuration-Office365-x64.xml**, **configuration-Office365-x86.xml**, **configuration-Office2019Enterprise.xml**.   

* In questa stessa cartella copia anche il mio file **mia_configurazione.xml**

* Creo un file batch **download.bat** per il download di Office, questo scaricherà nella sottocartella **Office** tutti gli applicativi:

~~~batch
.\setup.exe /download .\mia_configurazione.xml
~~~

* Poi creo un file batch **install.bat** per l'installazione di Office:

~~~batch
.\setup.exe /configure .\configurazione_e3.xml
~~~

* Poi prendo tutta la cartella principale, la copio sul PC in cui dovrò installare l'Office.   

* Qua lancerò il file **install.bat**
