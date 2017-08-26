---
id: 2503
title: 'Errore: Missing required field &#8220;updated&#8221;'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2503
permalink: /errore-missing-required-field-updated/
layout_key:
  - 
post_slider_check_key:
  - 0
dsq_thread_id:
  - 1936323467
authorsure_include_css:
  - 
categories:
  - Linux
  - Windows
tags:
  - entry-date
  - updated
  - wordpress
---
Se avete seguito la procedura per essere riconosciuti come **Autori da Google** ed eseguito la verifica del vostro blog WordPress potreste ottenere l&#8217;errore in oggetto dai risultati di **Rich Snippets Testing Tool**.

Per risolvere il problema è bastato cercare nei files del tema che state usando la riga:

`time class="entry-date"`

e sostituirla con:

`time class="entry-date updated"`

Solitamente potrebbe essere contenuta nel file &#8220;functions.php&#8221;

Se utilizzare il tema Customizr, il file da modificare è: `/theme/customizr/parts/class-content-post_metas.php`