---
title: "Veeam: Cannot create a shadow copy of the volumes containing writer's data"
subtitle: "VSS asynchronous operation is not completed. Operation: [Shadow copies commit]. Code: [0x8004231f]"
author: Stefano Marzorati
date: 2022-10-13 10:30:00 +0200
layout: post
image: 'https://marzorati.co/img/veeam.png'
share-img: 'https://marzorati.co/img/veeam.png'
categories: [Windows]
tags: [microsoft, veeam, backup, failed, job, vss, shadow, copy, 0x8004231f]
---
*Questo errore è in genere causato da spazio su disco insufficiente su un volume nel sistema operativo Windows di cui viene eseguito il backup.   
Questo può includere la partizione riservata del sistema.   
Può anche essere causato dalla definizione di associazioni di archiviazione shadow con una dimensione massima inferiore a quella necessaria per creare la copia shadow.*   

1. Verificare se si ha sufficiente spazio sui dischi
2. Digitare il comando `vssadmin list shadowstorage`
Se come risultato avrete `No items found that satisfy the query` probabilmente avete un problema con le shadow copy.
3. Verificare se il servizio Windows VSS `Volume Shadow Copy` sia running
4. Entrate nelle properties del disco C:\ e andate al tab **Shadow Copies**
5. Selezionate il disco C:\ e cliccate su **Settings**, fate una modifica alla dimensione limite, salvatelo e poi rimettere il valore precedente.
6. Riprovate a schedulare il backup e digitare nuovamente il comando al punto 2.

Se tutto OK dovreste avere un risultato simile:   

> Shadow Copy Storage association   
>   For volume: (C:)\\?\Volume{f7185a0f-3733-4ef3-a256-6fcd6e61e2ab}\   
>   Shadow Copy Storage volume: (C:)\\?\Volume{f7185a0f-3733-4ef3-a256-6fcd6e61e2ab}\   
>   Used Shadow Copy Storage space: 19,5 MB (0%)   
>   Allocated Shadow Copy Storage space: 480 MB (0%)   
>   Maximum Shadow Copy Storage space: 9,94 GB (9%)   