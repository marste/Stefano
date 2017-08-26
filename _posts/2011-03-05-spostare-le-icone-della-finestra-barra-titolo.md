---
id: 110
title: Spostare le icone della finestra barra titolo
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/spostare-le-icone-della-finestra-barra-titolo
permalink: /spostare-le-icone-della-finestra-barra-titolo/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 7785006476131777898
  - 7785006476131777898
  - 7785006476131777898
categories:
  - Linux
---
Premete **ALT+F2** e nella finestra che si apre scrivete `gconf-editor`.

A questo punto, nella finestra che si aprirà, sulla sinistra scegliete **Apps -> Metacity -> General**, poi nella parte destra selezionate la voce `button_layout`, dovreste avere come valore una stringa del tipo:

> `close,minimize,maximize:menu`

Semplicemente, cambiatela in:

> `menu:minimize,maximize,close`

In pratica, i due punti rappresentano il **titolo** della finestra..