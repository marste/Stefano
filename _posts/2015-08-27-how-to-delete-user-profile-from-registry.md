---
title: How to delete a User Profile from the registry 
date: 2015-08-27 09:00:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /how-to-delete-user-profile-from-registry/
categories:
  - Windows
tags:
  - delete
  - user
  - profile
  - registry
  - windows
---
Come prima cosa devi trovare il SID dell'utente.   
Questo comando lo puoi lanciare da qualsiasi PC nel dominio.   

	wmic useraccount get name,sid

Verranno mostrati tutti i SID della rete, ad esempio:   

	s.marzorati            S-1-5-21-962121045-2614314580-1061092883-1174

Vai sul PC a cui devi rimuovere il profilo ed entra con regedit al seguente percorso:   

	HKLM\Software\Microsoft\WindowsNT\CurrentVersion\ProfileList

Qua cancella la chiave con il SID trovato in precedenza.   
Poi vai in:   

	HKLM\Software\Microsoft\WindowsNT\CurrentVersion\ProfileGuid

e elimini la chiave con quel SID

Disconnettiti e riconnettiti e il profilo verrà ricreato.