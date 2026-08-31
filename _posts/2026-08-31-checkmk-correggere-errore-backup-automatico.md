---
title: "CheckMK - Backup problem AttributeError: ‘NoneType’ object has no attribute ‘name’"
subtitle: Correzione manuale del bug
date: 2026-08-31 07:30:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/cmk.png'
share-img: 'https://marzorati.co/img/cmk.png'
layout: post
published: true
categories: [networking]
tags: [cmk, checkmk, linux, backup, error, bug, fixed]
---
Per correggere il backup:

Andare al file python del backup:
```
/omd/versions/2.5.0pXXX.pro/lib/python3/omdlib/backup.py
```

Trova:
```
if not predicate(tarinfo):
```

Sostituisci con:
```
if tarinfo is None or not predicate(tarinfo):
```
