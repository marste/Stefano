---
title: Come eliminare partizioni da una chiavetta USB in Windows con diskpart
date: 2017-02-27 11:15:00 +0200
author: Stefano Marzorati
layout: post
permalink: /come-eliminare-partizioni-chiavetta-usb-windows-diskpart/
categories:
  - Windows
tags:
  - eliminare
  - partizioni
  - chiavetta
  - usb
  - diskpart
---
<code>diskpart</code>   
<code>list disk</code>   
<code>select disk X</code>   
<code>clean</code>   
<code>create partition primary</code>   
<code>format fs=ntfs quick</code>   
<code>active</code>   
<code>assign</code>   
<code>exit</code>   
<BR>