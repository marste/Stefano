---
id: 2603
title: Come modificare la lista allegati che si possono caricare su WordPress
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2603
permalink: /come-modificare-la-lista-allegati-che-si-possono-caricare-su-wordpress/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2058136394
categories:
  - Linux
  - Windows
tags:
  - add
  - allegati
  - attachments
  - extension
  - file
  - permission
  - upload
  - wordpress
---
Edita il file: `wp-includes/functions.php`

Arriva alla riga: `function wp_get_mime_types()`

Quì aggiungi il mime-type dell&#8217;estensione di file che vorrai aggiungere.

Ad esempio, se vuoi permettere di caricare i files .gpx, dovrai aggiungere la seguente riga:

`'gpx' => 'application/graphx',`