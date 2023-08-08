---
title: "Office 365 - Disabilitare le risposte automatiche per indirizzi specifici"
author: Stefano Marzorati
layout: post
date: 2023-08-08 11:20:00 +0200
image: 'https://marzorati.co/img/outlook.png'
share-img: 'https://marzorati.co/img/outlook.png'
categories: [Exchange]
tags: [disable, automatic, replies, email, address, specific]
---
A tale scopo è possibile impostare una **regola di trasporto**.   
Nel portale di Office 365, accedere a **Exchange Admin Center** e selezionare **Flusso di posta**.   
Nella sezione **Regole**, fare clic sul simbolo + per creare una nuova regola vuota.   
Creare più di una condizione.   

L'aspetto dovrebbe essere il seguente:   

<center><img src="https://marzorati.co/img/post/rule_exchange_1.png" alt="Exchange Rule"></center>

In italiano le voci sono:

Le proprietà del messaggio - includono il tipo di messaggio OOF
Il mittente è questa persona (elencare i mittenti)
Blocca il messaggio - elimina il messaggio senza inviare alcuna notifica

Assicurati che la regola abbia una priorità abbastanza alta da non essere bloccata da altre regole di trasporto.   