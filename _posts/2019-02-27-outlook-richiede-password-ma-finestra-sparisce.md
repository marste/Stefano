---
title: 'Outlook 2016 richiede la password, ma la finestra sparisce'
date: 2019-02-27 09:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/office.png'
share-img: 'https://marzorati.co/img/office.png'
layout: post
categories:
  - Office365
tags:
  - outlook
  - office
  - password
  - office365
  - finestra
  - box
  - disappears
---
Se vi è successo che Outlook non si sincronizzi in attesa della password, ma quando premete il pulsante per inserirla, vedete la finestra che dovrebbe farvi inserire le credenziali che sparisce (si apre e si chiude in mezzo secondo), allora Microsoft vi consiglia di tornare alla vecchia modalità della gestione delle password in questa maniera:   

Vai nei registri di Windows: **Esegui** - **Regedit**   

	HKEY_CURRENT_USER\Software\Microsoft\Office\16.0\Common\Identity

Entra in  **Identity** e crea una nuova **REG_DWORD** chiamandola **EnableADAL** e lasciare il valore a **0**   

Riavvia Outlook o tutto il PC e vedrete che vi verrà richiesta la password.   
