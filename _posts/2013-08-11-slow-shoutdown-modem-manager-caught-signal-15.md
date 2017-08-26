---
id: 1900
title: 'Slow shoutdown: modem-manager caught signal 15'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1900
permalink: /slow-shoutdown-modem-manager-caught-signal-15/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
geo_public:
  - 0
  - 0
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1958700218
categories:
  - Linux
tags:
  - acpi
  - apm
  - aspm
  - shutdown
  - slow
  - ubuntu
---
Il problema è molto probabilmente legato al ACPI.  
Dal syslog appare anche la segnalazione:  
`ACPI _OSC support notification failed, disabling PCIe ASPM`  
Purtroppo sembra che il firmware stia indicando al kernel che in realtà non supporta ASPM sul mio hardware.

A questo punto decido di forzare l&#8217;**acpi** e spegnere l&#8217;**apm**

`sudo nano /etc/default/grub`  
modifica la riga:  
`GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"`  
in:  
`GRUB_CMDLINE_LINUX_DEFAULT="quiet splash" acpi=force apm=power_off`  
salva e chiudi

`sudo nano /etc/modules`  
aggiungi questa riga:  
`apm power_off=1`  
salva e chiudi

`sudo update-grub`