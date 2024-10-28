---
title: "Come pulire la cache di Microsoft Teams"
date: 2024-10-28 10:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/teams.png'
share-img: 'https://marzorati.co/img/teams.png'
categories: [Windows]
tags: [pulire, cache, Teams, clean, temporanei, chat, spariti, utenti, chat]
---
Se vi è capitato qualche strano malfunzionamento di Teams utilizzando il client su Windows che però non avete riscontrato nella versione web, forse è bene che provate ad eliminare alcuni files temporanei di cache di Teams.

Il percorso dei files è il seguente:

    %AppData%\Microsoft\teams\application cache\cache
    %AppData%\Microsoft\teams\blob_storage
    %AppData%\Microsoft\teams\databases
    %AppData%\Microsoft\teams\cache
    %AppData%\Microsoft\teams\gpucache
    %AppData%\Microsoft\teams\Indexeddb
    %AppData%\Microsoft\teams\Local Storage
    %AppData%\Microsoft\teams\tmp
    %LocalAppData%\Google\Chrome\User Data\Default\Cache
    %LocalAppData%\Google\Chrome\User Data\Default\Cookies
    %LocalAppData%\Google\Chrome\User Data\Default\Web Data
    Internet Explorer Temporary Internet Files
    Internet Explorer Cookies


In alternativa scaricate questo <a href="https://marzorati.co/download/clear_cache_Teams.ps1" target="_blank">script</a> in Powershell che automatizza la cancellazione di questi files.

~~~powershell
$challenge = Read-Host "Are you sure you want to delete Teams Cache (Y/N)?"
$challenge = $challenge.ToUpper()
if ($challenge -eq "N"){
Stop-Process -Id $PID
}elseif ($challenge -eq "Y"){
Write-Host "Stopping Teams Process" -ForegroundColor Yellow
try{
Get-Process -ProcessName Teams | Stop-Process -Force
Start-Sleep -Seconds 3
Write-Host "Teams Process Sucessfully Stopped" -ForegroundColor Green
}catch{
echo $_
}
Write-Host "Clearing Teams Disk Cache" -ForegroundColor Yellow
try{
Get-ChildItem -Path $env:APPDATA\"Microsoft\Teams\application cache\cache" | Remove-Item -Confirm:$false
Get-ChildItem -Path $env:APPDATA\"Microsoft\Teams\blob_storage" | Remove-Item -Confirm:$false
Get-ChildItem -Path $env:APPDATA\"Microsoft\Teams\databases" | Remove-Item -Confirm:$false
Get-ChildItem -Path $env:APPDATA\"Microsoft\Teams\cache" | Remove-Item -Confirm:$false
Get-ChildItem -Path $env:APPDATA\"Microsoft\Teams\gpucache" | Remove-Item -Confirm:$false
Get-ChildItem -Path $env:APPDATA\"Microsoft\Teams\Indexeddb" | Remove-Item -Confirm:$false
Get-ChildItem -Path $env:APPDATA\"Microsoft\Teams\Local Storage" | Remove-Item -Confirm:$false
Get-ChildItem -Path $env:APPDATA\"Microsoft\Teams\tmp" | Remove-Item -Confirm:$false
Write-Host "Teams Disk Cache Cleaned" -ForegroundColor Green
}catch{
echo $_
}
Write-Host "Stopping Chrome Process" -ForegroundColor Yellow
try{
Get-Process -ProcessName Chrome| Stop-Process -Force
Start-Sleep -Seconds 3
Write-Host "Chrome Process Sucessfully Stopped" -ForegroundColor Green
}catch{
echo $_
}
Write-Host "Clearing Chrome Cache" -ForegroundColor Yellow
try{
Get-ChildItem -Path $env:LOCALAPPDATA"\Google\Chrome\User Data\Default\Cache" | Remove-Item -Confirm:$false
Get-ChildItem -Path $env:LOCALAPPDATA"\Google\Chrome\User Data\Default\Cookies" -File | Remove-Item -Confirm:$false
Get-ChildItem -Path $env:LOCALAPPDATA"\Google\Chrome\User Data\Default\Web Data" -File | Remove-Item -Confirm:$false
Write-Host "Chrome Cleaned" -ForegroundColor Green
}catch{
echo $_
}
Write-Host "Stopping IE Process" -ForegroundColor Yellow
try{
Get-Process -ProcessName MicrosoftEdge | Stop-Process -Force
Get-Process -ProcessName IExplore | Stop-Process -Force
Write-Host "Internet Explorer and Edge Processes Sucessfully Stopped" -ForegroundColor Green
}catch{
echo $_
}
Write-Host "Clearing IE Cache" -ForegroundColor Yellow
try{
RunDll32.exe InetCpl.cpl, ClearMyTracksByProcess 8
RunDll32.exe InetCpl.cpl, ClearMyTracksByProcess 2
Write-Host "IE and Edge Cleaned" -ForegroundColor Green
}catch{
echo $_
}
Write-Host "Cleanup Complete... Launching Teams" -ForegroundColor Green
Start-Process -FilePath $env:LOCALAPPDATA\Microsoft\Teams\current\Teams.exe
Stop-Process -Id $PID
}else{
Stop-Process -Id $PID
}
~~~

Se state utilizzando la nuova versione di Teams, il percorso è questo:   

`%localappdata%\packages\MSTeams_8wekyb3d8bbwe\Localcache\Microsoft\MSTeams`