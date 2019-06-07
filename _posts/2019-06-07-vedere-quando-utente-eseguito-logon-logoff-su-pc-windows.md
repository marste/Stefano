---
title: Vedere quando un utente ha effettuato logon o logoff su un PC
subtitle: Filtrare con query XML dall'Event Viewer
date: 2019-06-07 13:25:00 +0200
published: true
layout: post
image: 'https://marzorati.co/img/windows.png'
share-img: 'https://marzorati.co/img/windows.png'
categories:
  - Windows
tags:
  - event
  - viewer
  - login
  - logon
  - logoff
  - 4624
  - 4634
  - xml
  - filtro
---
Query da utilizzare:   

	<QueryList>
	<Query Id="0" Path="Security">
	<Select Path="Security">*[System[(EventID='4624') or (EventID='4634')] and EventData[Data [@Name='TargetUserName'] = 'MarioRossi'] and EventData[Data [@Name='TargetDomainName'] = 'ACME']]</Select>
	</Query>
	</QueryList>

Avrai vari risultati, per avere dettagli maggiori verifica il campo **LogonType**.   

Significato dei valori di LogonType:   

 - Logon Type 2 – Interactive
 - Logon Type 3 – Network
 - Logon Type 4 – Batch
 - Logon Type 5 – Service
 - Logon Type 7 – Unlock
 - Logon Type 8 – NetworkCleartext
 - Logon Type 9 – NewCredentials
 - Logon Type 10 – RemoteInteractive
 - Logon Type 11 – CachedInteractive
 