---
id: 1310
title: Comandi utili Lotus Domino DAOS
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1310
permalink: /comandi-utili-lotus-domino-daos/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1919507932
categories:
  - Windows
---
**Abilitare DAOS su un db:**  
`load compact -C -n -v -daos on mailesempio.nsf`

**Disabilitare DAOS su un db:**  
`load compact -c -daos off mailesempio.nsf`

\***\***\***\****\*\\*\* COMANDI DAOS: \*\*\***\***\***\***\***\***\***\***\***\*****

tell daosmgr resync

tell daosmgr status

Verify that the database is DAOS enabled and the status is Read/Write:  
tell daosmgr status dbsummary dbname

How do I determine which databases are DAOS enabled?

tell daosmgr status dbsummary

List of all NLO files referenced by a database :  
tell daosmgr listnlo mailfile.nsf

tell daosmgr listnlo missing  nomedb.nsf  
tell daosmgr listnlo missing mail  
tell daosmgr listnlo all

The following two notes.ini parameters control when resync will be allowed to run  
–DAOS\_RESYNC\_START_TIME=12:00:00 AM  
–DAOS\_RESYNC\_STOP_TIME=04:00:00 AM

<div id="dc_vk_code" style="display:none;">
</div>