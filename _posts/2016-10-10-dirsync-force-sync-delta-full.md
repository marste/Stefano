---
title: Come eseguire manualmente un DirSync per sincronizzare l'Active Directory con Office 365
date: 2016-10-10 12:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
layout: post
permalink: /dirsync-azure-force-sync-delta-full/
categories:
  - Office365
tags:
  - dirsync
  - azure
  - force
  - office365
  - powershell
  - delta
  - full
  - AD
---

To initiate a Delta Sync, open Windows PowerShell and run:   

<code>Import-Module ADSync</code>   

<code>Start-ADSyncSyncCycle -PolicyType Delta</code>

To initiate a Full Sync, open Windows PowerShell and run:   

<code>Import-Module ADSync</code>   

<code>Start-ADSyncSyncCycle -PolicyType Initial</code>
