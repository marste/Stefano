---
title: Scoprire MAC ADDRESS di un device remoto
author: Stefano Marzorati
layout: post
date: 2020-04-29 16:00:00 +0200
image: 'https://marzorati.co/img/terminal.png'
share-img: 'https://marzorati.co/img/terminal.png'
categories: [networking]
tags: [arp, find, mac address, trovare]
published: false
---
LOGON
Get-WinEvent -LogName Security -FilterXPath "*[System[EventID=4624 and TimeCreated[timediff(@SystemTime) <= 86400000]] and EventData[Data[@Name='SubjectUserName'] and Data = 's.marzorati']]"

LOGOFF
Get-WinEvent -LogName Security -FilterXPath "*[System[EventID=4634 and TimeCreated[timediff(@SystemTime) <= 86400000]] and EventData[Data[@Name='SubjectUserName'] and Data = 's.marzorati']]"

FAILURE LOGON
Get-WinEvent -LogName Security -FilterXPath "*[System[EventID=4625 and TimeCreated[timediff(@SystemTime) <= 86400000]] and EventData[Data[@Name='SubjectUserName'] and Data = 't.previti']]"



GET-EVENTLOG -Logname Security | where { $_.EntryType -eq 'FailureAudit' } | export-csv C:\Failures.csv