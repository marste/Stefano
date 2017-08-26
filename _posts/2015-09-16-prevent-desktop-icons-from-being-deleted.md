---
title: Linux, prevent desktop icons from being deleted
author: Stefano Marzorati
date: 2015-09-16 14:50:00 -07:00
layout: post
permalink: /prevent-desktop-icons-from-being-deleted/
categories:
  - Linux
tags:
  - ubuntu
  - delete
  - desktop
  - icons
  - prevent
---
Se avete un PC con installato Linux e l'avete dato in uso ad un utente che deve avere un accesso molto limitato, oppure avete paura che elimini dei files o le icone sul desktop dei programmi che utilizza, ecco un semplice comando per impedirglielo.   

Accedere con utente **root**, e digitate da terminal questo comando:   

	sudo chattr +i /home/utente/Desktop/nomedelfile.desktop

Se per caso dovete ripristinare la possibilità di eliminarlo, digitare il comando:   

	sudo chattr -i /home/utente/Desktop/nomedelfile.desktop