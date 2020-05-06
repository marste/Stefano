---
title: Trovare da PowerShell i Security Events di LogOn e LogOff di un utente
author: Stefano Marzorati
layout: post
date: 2020-04-29 22:43:00 +0200
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [powershell]
tags: [find, security, events, logon, logoff, failed]
published: true
---
Per trovare tutti gli eventi in cui la persona ***s.marzorati*** ha eseguito un **logon**:
~~~powershell
Get-WinEvent -LogName Security -FilterXPath "*[System[EventID=4624 and TimeCreated[timediff(@SystemTime) <= 86400000]] and EventData[Data[@Name='SubjectUserName'] and Data = 's.marzorati']]"
~~~
Per trovare tutti gli eventi in cui la persona ***s.marzorati*** ha eseguito un **logoff**:
~~~powershell
Get-WinEvent -LogName Security -FilterXPath "*[System[EventID=4634 and TimeCreated[timediff(@SystemTime) <= 86400000]] and EventData[Data[@Name='SubjectUserName'] and Data = 's.marzorati']]"
~~~
Per trovare tutti gli eventi in cui la persona ***s.marzorati*** <u>non è riuscito</u> ad eseguire un **logon**:
~~~powershell
Get-WinEvent -LogName Security -FilterXPath "*[System[EventID=4625 and TimeCreated[timediff(@SystemTime) <= 86400000]] and EventData[Data[@Name='SubjectUserName'] and Data = 't.previti']]"
~~~
Se volete esportare in un file csv **tutti i logon falliti**, digitate:
~~~powershell
GET-EVENTLOG -Logname Security | where { $_.EntryType -eq 'FailureAudit' } | export-csv C:\Failures.csv
~~~