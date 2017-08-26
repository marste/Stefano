---
id: 1412
title: Aggiornare OpenFire su cluster CentOS
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1412
permalink: /update-openfire-cluster-centos/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1979590632
categories:
  - Linux
---
- Entrare in ssh sul nodo1 e sul nodo2

&#8211; scrivi:  
`cd download`  
(su tutte e 2 le sessioni)

&#8211; scarica il pacchetto su tutte e 2 le sessioni con il comando:  
`wget http://www.igniterealtime.org/downloadServlet?filename=openfire/openfire-3.5.1-1.i386.rpm`  
(ovviamente questo è della versione 3.5.1)

&#8211; sul nodo1 scrivi:  
`rpm -Uhv openfire-3.5.1-1.i386.rpm`  
(installa il pacchetto)

&#8211; poi scrivi:  
`/etc/init.d/openfire restart`  
(riavvia il servizio)

&#8211; scrivi:  
`rpm -qi openfire`  
(x verificare che versione di openfire c&#8217;è installata)

&#8211; se è tutto ok, fai la stessa cosa sul nodo2

una volta fatto tutto anche sul nodo2, lancia:  
`csync2 -xv`  
(x verificare che il cluster sia allineato)

fine

Se ci fosse qualche problema sull&#8217;allineamento del cluster.

Esempio:  
se non vuoi che ogni 30 minuti ti arrivi una mail con il contenuto che vedi a video, cioè dobbiamo decidere chi ha il file nuovo e buono, con il comando  
`csync2 -f /opt/openfire/conf/openfire.xml`  
lanciato nel nodo in cui vogliamo tenere il file.

<div id="dc_vk_code" style="display:none;">
</div>