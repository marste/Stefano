---
title: Xiaomi RedMi2 - Install recovery and last ROM MIUI
date: 2015-05-03 23:00:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /xiaomi-redmi2-install-recovery-last-rom-miui-multilanguage/
categories:
  - Smartphone
tags:
  - xiaomi
  - redmi2
  - recovery
  - rom
  - miui
  - HM2014813
---
If you bought a smartphone **Xiaomi RedMi2** (second edition with 2GB of RAM and 16GB of ROM) from a Chinese retailer, perhaps on [Aliexpress](http://www.aliexpress.com/) like myself, here some useful information that will help you a lot.   

The phone that I received was the model **HM2014813** (HM 2LTE-CU) which differs from the model HM2014811.   

  - HM2014813 (Chinese)
  - HM2014811 (International)
  
The model is under the battery.   

This phone had a preinstalled ROM MIUI modded, namely **MIUI version 16.2.4.0 (KHJCNBK) Stable**, obviously not original and not upgradeable.   
Shortly after that I was using an internet connection, they kept out pop-up ads by google.   
when I opened any app, it opened a full-screen advertising or just below, but to keep you from using the keyboard.   
I began to doubt strongly this ROM.   
After some research on the forum I had confirmation from experts that these ROMs are full of bloatware and are definitely not recommended.   
I decided to install app [Malwarebytes Anti-Malware](https://play.google.com/store/apps/details?id=org.malwarebytes.antimalware&hl=en) and I discovered that there were in two .apk file **two Trojans**.

  - <code>/system/app/twitter _qd_3025.apk</code>
  - <code>/system/app/miuivideo.apk</code>

I remove these files, but the problem of pop-up remains.   
I decided at this point to install a new ROM and I decide to flash the Multilingual latest update.   

At this point, I find the documentation on the forum [http://en.miui.com](http://en.miui.com) which lose me a lot of time and run into various errors.   

**WARNING THIS PROCEDURE NOT WORKING**   

  - I downloaded from the Google Play app "Flashify" in order to install the recovery
  - I downloaded [Philz Touch Recovery](https://javteam.wordpress.com/download/xiaomi-redmi-2)
  - I tried to install this [ROM](https://www.androidfilehost.com/?fid=24052804347822070)

The installation ended with this error:   
**This package is for HM2014813 device; this is a HM2014811**

I began to have doubts about which model I really, but fortunately the model was really the one shown on the battery.   

**SOLUTION**   

In the end I managed to install all by following these steps:   

  - I downloaded from the Google Play app "Flashify" in order to install the recovery
  - I downloaded this [CWM Recovery](http://marzorati.co/download/CWM_Recovery.zip)
  - I downloaded the latest ROM **MIUI 7** for this model from the site [<del>http://htcfanboys.com/download/acid/?action=list&folder=75939</del>](http://htcfanboys.com/download/acid/?action=list&folder=75939) or [https://www.androidfilehost.com/?w=search&s=HM2014813](https://www.androidfilehost.com/?w=search&s=HM2014813) or [http://xiaomi.eu/community/threads/5-9-24.28459/](http://xiaomi.eu/community/threads/5-9-24.28459/)
  - The phone started with the new version of MIUI 7
  - I'm back in Official MIUI recovery mode from the options of System Update
  - I ran a full wipe cache and data
