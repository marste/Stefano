---
id: 781
title: Disabilitare o abilitare gli Automatic Updates
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=781
permalink: /disabilitare-o-abilitare-gli-automatic-updates/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2141015044
categories:
  - Linux
---
`gedit /etc/apt/apt.conf.d/10periodic`

Così è tutto disabilitato:

`APT::Periodic::Update-Package-Lists "0";   
APT::Periodic::Download-Upgradeable-Packages "0";   
APT::Periodic::AutocleanInterval "0";   
APT::Periodic::Unattended-Upgrade "0";`