---
id: 2526
title: Aggiornare phpBB e migrare dati su nuovo server
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2526
permalink: /aggiornare-phpbb-migrare-dati-server/
authorsure_include_css:
  - 
layout_key:
  - 
post_slider_check_key:
  - 0
dsq_thread_id:
  - 2000710336
categories:
  - Linux
  - Windows
tags:
  - aggiornare
  - install
  - migrare
  - phpbb
---
Ipotizziamo di avere la versione 3.0.8 di phpBB su un server.  
Vorremmo installare l&#8217;ultima versione 3.0.12 di phpBB su un nuovo server.  
Come posso migrare?  
Ecco quali sono i passi principali:

1) Fai un backup del database  
2) Installa l'ultima versione di phpBB 3.0.12 e configuralo come se fosse la prima installazione.  
3) Importa il database backuppato in precedenza sovrascrivendo quello dell'installazione nuova.  
4) Lancia l'url `../install/database_update.php` in questo modo aggiornerà il database  
5) Rinomina la directory "**install**"  
6) Copiare dal vecchio server al nuovo server tutta la directory "**images**", "**files**" e "**store**".

Fine

**Se invece dovete migrare da una versione 3.0.x alla versione 3.1.x, fate così:**

1) Fate la copia di tutta la directory di phpBB sul nuovo server  
2) Fate un dump del db e importatelo sul nuovo server  
3) Fate attenzione che nel file config.php ci sono le credenziali di accesso al db, per cui se queste differiscono dal vecchio, modificatele.  
4) Se cambiate l’url del vostro forum, dovrete modificare la tabella phpbb_config (es. script_path e/o server_name)  
5) Se avete fatto tutto correttamente il nuovo forum si aprirà come sul vecchio server.  

Ora aggiorniamolo:  

1) Elimina tutto tranne il file **config.php** e le cartelle: **images**, **files**, **store**  
2) Carica tutto il contenuto del pacchetto completo della nuova versione 3.1.x nella cartella del forum  
3) Vai alla pagina http://www.tuo-forum<strong>/install/database_update.php</strong>  
4) Elimina la cartella **install**  

Fine  
