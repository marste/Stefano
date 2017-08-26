---
id: 2573
title: Disabilitare l’aggiornamento automatico di WordPress
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2573
permalink: /disabilitare-laggiornamento-automatico-di-wordpress/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2045523724
categories:
  - Linux
  - Windows
tags:
  - automatic
  - disable
  - update
  - wordpress
---
Basta aprire il file **wp-config.php** e aggiungere la seguente riga:

`define( 'WP_AUTO_UPDATE_CORE', false );`

Se si vuole disabilitare anche i temi e i plugins, la riga da aggiungere a **wp-config.php** è la seguente:

`define( 'AUTOMATIC_UPDATER_DISABLED', true );`

Maggiori dettagli li potete trovare <a href="http://codex.wordpress.org/Configuring_Automatic_Background_Updates" target="_blank">qua</a>