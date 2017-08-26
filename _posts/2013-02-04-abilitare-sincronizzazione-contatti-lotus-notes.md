---
id: 1286
title: Abilitare sincronizzazione contatti Lotus Notes
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1286
permalink: /abilitare-sincronizzazione-contatti-lotus-notes/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1940872951
categories:
  - Windows
---
Enabling contacts synchronization keeps your mail file contacts and device contacts up-to-date. Before you can synchronize your contacts, you must set a contacts preference that enables synchronization.

1.    If you use **Lotus Notes 8 Standard**, follow these steps:  
a.    Click File > Preferences.  
b.    Click Contacts.  
c.    Select Synchronize Contacts on the Replicator and click OK.  
d.    Click Open > Replication.  
e.    Make sure that Synchronize Contacts is selected.  
f.    Click Start Now.

2.    If you use **Lotus Notes 8 Basic**, follow these steps:  
a.    Click in the bookmark bar to open your local contacts file (names.nsf).  
b.    Click Actions > More > Preferences.  
c.    Select Enable &#8220;Synchronize Contacts&#8221; on the Replicator and click OK.  
d.    Click in the bookmark bar.  
e.    Make sure that Synchronize Contacts is selected.  
f.    Click Start Now.

Your contacts are ready for synchronization.

Nel caso ci fosse la rubrica con il template vecchio, aggiornarlo nel seguente modo:

**C:Programmilotusnotesdata>c:Programmilotusnotesnconvert.exe names.nsf * pernames.ntf**