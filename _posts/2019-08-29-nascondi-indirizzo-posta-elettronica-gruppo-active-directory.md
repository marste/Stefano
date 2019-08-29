---
title: Nascondi l'indirizzo email di un gruppo di Active Directory
date: 2019-08-29 16:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/office.png'
share-img: 'https://marzorati.co/img/office.png'
layout: post
categories:
  - Office365
tags:
  - nascondere
  - email
  - posta
  - office365
  - exchange
  - editor
  - attributi
  - active directory

---
- Andare nelle **Proprietà** del gruppo in Active Directory
- Andare in **Editor Attributi**
- Impostare l'attributo **msExchHideFromAddressLists** del gruppo di protezione su **True**
- Sincronizzare, eventualmente, con il tenant di Office365.