---
id: 1567
title: Aggiornare Prestashop ver. 1.5.x
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1567
permalink: /aggiornare-prestashop-1-5/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:25;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1906740611
categories:
  - Linux
  - Windows
---
- Disattiva il negozio (&#8220;Maintenance&#8221; page of the &#8220;Preferences&#8221; menu)

(Se non funziona edita il file /classes/controller/FrontController.php e cambia &#8220;HTTP/1.1 503 temporarily overloaded&#8221; in &#8220;www.sito.it&#8221;)

&#8211; Backuppa via FTP tutto il contenuto in una nuova directory &#8220;prestashop-old&#8221;  
&#8211; Backuppa il database via phpmyadmin  
&#8211; Backuppa la lingua personalizzata (&#8220;Esporta Traduzioni&#8221; Localizzazione &#8211; Traduzioni) 

&#8211; Scarica e unzippa l&#8217;ultima versione di PrestaShop: http://www.prestashop.com/en/download e scompatta il contenuto nella directory &#8220;prestashop-new&#8221;  
&#8211; Copia i tuoi files personali da &#8220;prestashop-old&#8221; a &#8220;prestashop-new&#8221; sul tuo computer.

/mails

/img &#8211; copia tutto tranne /img/admin e /img/jquery-ui

/modules &#8211; (attenzione al modulo di paypal)

/themes/themeName &#8211; copia solo il tema che stai utilizzando

Se usi il tema di default non copiare questa directory (/themes/prestashop)  
Se hai fatto modifiche al tema di default, copia questa directory (/themes/default)

/download e /upload

/classes &#8211; Se hai fatto delle modifiche alle classi in questa directory, copiale nella nuova 

/classesfolder

/config &#8211; copia questo file essenziale: &#8220;settings.inc.php&#8221;

/translations &#8211; se si utilizza una lingua diversa da quelle disponibili di default

&#8211; La tua directory &#8220;prestashop-new&#8221; è pronta!

&#8211; Copia la directory &#8220;prestashop-new&#8221; sul server

&#8211; Rinomina la directory su server &#8220;prestashop&#8221; in &#8220;prestashop-backup&#8221;  
&#8211; Rinomina la directory &#8220;prestashop-new&#8221; in &#8220;prestashop&#8221;

&#8211; Lancia l&#8217;aggiornamento http://server/prestashop/install/upgrade/upgrade.php

&#8211; Ci metterà qualche minuto e poi apparirà una pagina XML che inizierà così: 

&#8211; Nella directory /prestashop rinomina la directory &#8220;install&#8221; e la directory &#8220;admin&#8221; nel nome che c&#8217;era prima

Rimettilo online (Preferenze &#8211; Manutenzione)

Se avevi apportato delle modifiche al file .htaccess, ripristinalo.  
Per reimpostare la lingua italiana, vai in Localizzazione &#8211; Traduzioni e aggiungi la lingua italiana.