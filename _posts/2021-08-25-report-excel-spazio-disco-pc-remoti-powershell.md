---
title: "Report Excel con PowerShell su spazio disco libero di PC remoti"
date: 2021-08-25 07:30:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/powershell.png'
share-img: 'https://marzorati.co/img/powershell.png'
categories: [PowerShell]
tags: [report, excel, script, space, disk, remote, pc, export]
---
Crea il file **Space_Disk.ps1** copiando/incollando il codice qua sotto:   

~~~powershell
$erroractionpreference = "SilentlyContinue" 
$a = New-Object -comobject Excel.Application 
$a.visible = $True  

$b = $a.Workbooks.Add() 
$c = $b.Worksheets.Item(1) 

$c.Cells.Item(1,1) = "Server Name" 
$c.Cells.Item(1,2) = "Drive" 
$c.Cells.Item(1,3) = "Total Size (GB)" 
$c.Cells.Item(1,4) = "Free Space (GB)" 
$c.Cells.Item(1,5) = "Free Space (%)"
$c.Cells.Item(1,6) = "Date" 

$d = $c.UsedRange 
$d.Interior.ColorIndex = 19 
$d.Font.ColorIndex = 11 
$d.Font.Bold = $True 

$intRow = 2 

$colComputers = get-content ".\ServerIPs.txt" 
foreach ($strComputer in $colComputers) 
{ 
  $colDisks = get-wmiobject Win32_LogicalDisk -computername $strComputer -Filter "DriveType = 3"  
  foreach ($objdisk in $colDisks) 
  { 
    $c.Cells.Item($intRow, 1) = $objDisk.SystemName 
    $c.Cells.Item($intRow, 2) = $objDisk.DeviceID 
    $c.Cells.Item($intRow, 3) = "{0:N0}" -f ($objDisk.Size/1GB) 
    $c.Cells.Item($intRow, 4) = "{0:N0}" -f ($objDisk.FreeSpace/1GB) 
    $c.Cells.Item($intRow, 5) = "{0:P0}" -f ([double]$objDisk.FreeSpace/[double]$objDisk.Size) 
    $c.Cells.Item($intRow, 6) = Get-Date
    $intRow = $intRow + 1 
  } 
}
~~~

Nella stessa cartella in cui salverai questo file, crea anche un file con nome **ServerIPs.txt** in cui inserirai tutti i nomi dei PC o Servers remoti.   

Da PowerShell lancia il file **Space_Disk.ps1**, ti si aprirà un foglio Excel che si autocompilerà con i dati di spazio rilevati.