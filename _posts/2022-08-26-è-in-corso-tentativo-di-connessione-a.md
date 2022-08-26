---
title: "È in corso un tentativo di connessione a \\..."
subtitle: Durante la fase di salvataggio di un file
author: Stefano Marzorati
date: 2022-08-26 15:30:00 +0200
layout: post
image: 'https://marzorati.co/img/office.png'
share-img: 'https://marzorati.co/img/office.png'
categories: [Office]
tags: [microsoft, office, word, excel, outlook, corso, tentativo, connessione, salvataggio, salva]
---
Se nella fase in cui state salvando un file Word, Excel o un allegato di Outlook vi esce un popup con un avviso che dice:   
```
È in corso un tentativo di connessione a \\...
```
Il problema è legato al percorso di salvataggio del file di default.   
Ultimamente questo messaggio appare a chi nel percorso di default ha una share di rete e non un percorso locale.   
Come workaround ho trovato che modificando in Word ed Excel il percorso di default, il problema non si propone più.   
Per cui in Word, Excel e PowerPoint basta andare in:   

- Opzioni
- Salvataggio
- Percorso file locale predefinito

E mettere un percorso reale locale.

Per Outlook andrà creata una voce nel registro.   
Andare in:   
```
 HKEY_CURRENT USER\Software\Microsoft\Office\1x.0\Outlook\Options
```
Creare un **Valore Stringa** chiamato **DefaultPath**, fare doppio click e mettere un percorso locale, ad esempio:   
```
C:\Temp
```
Chiudere e riaprire Outlook.