---
id: 3191
title: 'How to Debug Prestashop &#8211; Error 500'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3191
permalink: /how-to-debug-prestashop-error-500/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3306000093
categories:
  - Linux
  - Windows
tags:
  - debug
  - prestashop
---
Se avete aggiornato Prestashop e avete un errore 500 sulla home page, è bene poter capire meglio cosa lo manda in errore.  
Per far ciò basta semplicemente mettere in modalità di debug Prestashop.

Vai nella directory **/config/** ed edita il file **defines.inc.php**

Trova la riga:  
`define('_PS_MODE_DEV_', false);`

e metti come valore **true**

Ora non avrai più la schermata che riporta l&#8217;errore 500, ma vedrai proprio qual è l&#8217;errore reale.