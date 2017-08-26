---
id: 1210
title: Cambiare indirizzo IP da remoto in Windows
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=1210
permalink: /change-ip-address-remotely-netsh/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:0;i:11;}s:2:"wp";a:1:{i:0;i:0;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:0;i:11;}s:2:"wp";a:1:{i:0;i:0;}}'
authorsure_include_css:
  - 
dsq_thread_id:
  - 1901608705
categories:
  - Windows
---
`psexec.exe \ip_o_hostname cmd`

`netsh interface ip show config`

`netsh interface ip set address name="Connessione alla rete locale (LAN)" static 192.168.1.34 255.255.255.0 192.168.1.254 1`

`netsh interface ip set dns "Connessione alla rete locale (LAN)" static 192.168.101.34`

`netsh interface ip add dns "Connessione alla rete locale (LAN)" 192.168.101.46`

`netsh interface ip set dns "Connessione alla rete locale (LAN)" source=dhcp`  
`netsh interface ip set address name="Connessione alla rete locale (LAN)" source=dhcp`