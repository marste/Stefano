---
id: 1114
title: 'Runlevel &#8211; init'
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1114
permalink: /runlevel-init/
publicize_results:
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"172602001153204224";}}}'
  - 'a:1:{s:7:"twitter";a:1:{i:396682267;a:2:{s:7:"user_id";s:13:"marzorati_ste";s:7:"post_id";s:18:"172602001153204224";}}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 2199045946
categories:
  - Linux
tags:
  - init
  - runlevel
---
**Runlevel 0** : Avvia la sequenza di arresto del sistema (shutdown)

**Runlevel 1**: Rappresenta la modalità singolo utente, nessun altro utente può collegarsi, il servizio di rete è disabilitato.

**Runlevel 2**: Rappresenta lo stato multiutente, il servizio rete è attivo ma è disabilitato il file sharing.

**Runlevel 3**: In genere è quello predefinito quando si opera in modalità testuale, tutti i servizi sono attivi.

**Runlevel 4**: Inutilizzato. Può essere dedicato ad usi personali

**Runlevel 5**: E&#8217; il predefinito quando si vuole avviare Linux in modalità grafica

**Runlevel 6**: serve a riavviare la macchina

Per cambiare runlevel si utilizza il comando** init**