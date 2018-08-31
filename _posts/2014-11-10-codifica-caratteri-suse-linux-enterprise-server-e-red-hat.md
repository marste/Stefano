---
id: 3150
title: Codifica caratteri SUSE Linux Enterprise Server e Red Hat
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/linux.png'
share-img: 'https://marzorati.co/img/linux.png'
permalink: /codifica-caratteri-suse-linux-enterprise-server-e-red-hat/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3210557498
categories:
  - Linux
tags:
  - caratteri
  - codifica
  - euro
  - redhat
  - suse
---
**SLES**

**it_IT.UTF-8** è l&#8217;impostazione di default se si seleziona Italiano come lingua.

A quanto sembra su Linux, IBM &#8211; Cognos Business Intelligence non è aggiornato al supporto della codifica UTF-8.  
Il problema della SUSE è che, oltre all&#8217;UTF-8, non ha una combinazione lingua + codifica dei caratteri per l&#8217;italiano che supporti l&#8217;euro e i caratteri latini.  
Dobbiamo quindi crearla noi, e forzare l&#8217;utente root ad avviare il servizio con la nostra codifica.  
Pertanto questi sono i passi da seguire:

&#8211; da shell, con utente root, lanciare il comando 

`localedef -i it_IT -f ISO-8859-15 it_IT.ISO-8859-15`

&#8211; editare il file `/etc/sysconfig/language` e modificare i seguenti parametri come segue:

`RC_LANG="it_IT.ISO-8859-15"   
RC_LC_ALL="it_IT.ISO-8859-15"   
ROOT_USES_LANG="yes"   
AUTO_DETECT_UTF8="no"`

&#8211; se non esiste il file `/root/.bashrc`, copiare il file `/etc/skel/.bashrc` in /root/.bashrc  
&#8211; editare il file `/root/.bashrc` ed aggiungere in coda la seguente riga:

`export LANG=it_IT.ISO-8859-15`

&#8211; **riavviare il server linux** e conseguentemente il server Cognos.

Se il problema dovesse persistere:

&#8211; arrestare il server Cognos

&#8211; verificare da shell con l&#8217;utente root la lingua con il comando

`env | grep -i lang`

dovrebbe risultare la seguente variabile:

`LANG=it_IT.ISO-8859-15`

&#8211; riavviare dalla stessa shell il server Cognos con il comando

/opt/cognos/c8_64/bin64/cogconfig.sh -s

**RED HAT**  
Con la codifica UTF-8 Cognos su Red Hat non visualizza correttamente i caratteri, ha bisogno della codifica ISO-8859-15 ,  
che supporta sia i caratteri latini (come la ISO-8859-1) che l&#8217;euro.  
Pertanto nel file `/etc/sysconfig/i18n` va inserita la seguente stringa  
`LANG="it_IT.iso885915@euro"`  
e successivamente va effettuato il reboot della macchina.