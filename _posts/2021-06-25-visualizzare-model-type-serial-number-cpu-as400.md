---
title: "Visualizzare Type, Model, Serial Number e CPU di AS/400"
subtitle: Comandi
date: 2021-06-25 07:45:00 +0200
published: true
image: https://marzorati.co/img/ibm.png
share-img: https://marzorati.co/img/ibm.png
categories: [AS400]
tags: [type, model, serial number, as400. cpu]
---
Per vedere in una sola riga **SYSTEM TYPE/MODEL/SERIAL NUMBER**   
<code>CALL QSMBTTCC</code>

Oppure:   
<code>DSPSYSVAL QMODEL</code> - model number   
<code>DSPSYSVAL QSRLNBR</code> - serial number   
<code>DSPSYSVAL QPRCFEAT</code> - processor code   
