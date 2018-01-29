---
layout: post
title: Togliere protezione o limiti da un file Word senza conoscere la password
date: '2018-01-16 08:00:00 +0200'
author: Stefano Marzorati
image: 'http://thelaymanslawyer.com/wp-content/uploads/2016/05/download-draft-the-laymans-lawyer-2.png'
share-img: 'http://thelaymanslawyer.com/wp-content/uploads/2016/05/download-draft-the-laymans-lawyer-2.png'
categories:
  - Office
tags:
  - word
  - password
  - office
  - protection
  - limit
  - unprotected
published: true
---
1. **Apri il file Word** (doc, docx)   
2. Scegli **"File"**, **"Save as"** e assciurati di salvare il file in formato **.rtf** ("Rich-Text-Format")   
3. Chiudi il file   
4. **Apri** il nuovo file .rtf con un editor di testo (Notepad o **Notepad++**)   
5. Trova all'interno del file la parola **"passwordhash"** e **sostituisci la stringa alfanumerica** con una parola a caso (esempio "nopassword")   
6. **Salva e chiudi**   
7. **Riapri il file .rtf** con Word vai in "Revisione", "Limita modifica" e clicca su **"Rimuovi protezione"**. Togli tutti i flag   
8. Fatto. Hai tolto la protezione al file senza sapere la sua password   
9. Se vuoi puoi risalvare il file in doc o docx   