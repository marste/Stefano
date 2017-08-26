---
title: Google Chrome non vede più il plugin di Java
date: 2015-04-28 12:36:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /google-chrome-non-vede-plugin-java/
categories:
  - Windows
tags:
  - google
  - chrome
  - java
  - plugin
  - problema
---


Se avete Windows XP e utilizzate Google Chrome può capitare che Java non sia abilitato su quest'ultimo.   

  - Verificate nel Pannello di Controllo - Java - Generale che ci sia riportata la scritta "Java nel browser è abilitato"
  - Se è disabilitato, ovviamente lo dovete abilitare.
  - Poi andate nel tab "Sicurezza" e mettete un livello di sicurezza medio. (testato con Java 7 aggiornamento 80)   
  **ATTENZIONE** Se avete installato Java 8 il livello di sicurezza può essere solo alto o molto alto.
  - Riavviate il browser   

Anche se è abilitato, digitando [chrome://plugins](chrome://plugins) non vedrete il plugin abilitato.   
Per visualizzarlo, digitate: [chrome://flags/#enable-npapi](chrome://flags/#enable-npapi) e abilitatelo.   

Per verificare che Java sia nuovamente funzionante sul browser, potete andare sul sito:   

[http://javatester.org/version.html](http://javatester.org/version.html)   

Controllate nella barra degli indirizzi di abilitare il sito ad utilizzare Java.   
Se i siti che aprite, ad esempio quello della vostra banca, sono sempre gli stessi, dite di abilitarlo sempre per quel sito.
