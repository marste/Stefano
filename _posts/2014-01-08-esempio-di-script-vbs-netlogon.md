---
id: 2678
title: Esempio di script .vbs netlogon
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2678
permalink: /esempio-di-script-vbs-netlogon/
authorsure_include_css:
  - 
dsq_thread_id:
  - 2100230056
categories:
  - Windows
tags:
  - home
  - netlogon
  - printer
  - script
---
Option Explicit  
Dim objNetwork  
Dim WshNetwork  
Dim objFSO  
Dim strUNCPrinter1

Set objNetwork = CreateObject(&#8220;WScript.Network&#8221;)  
Set WshNetwork = CreateObject(&#8220;WScript.Network&#8221;)

Set objFSO = CreateObject(&#8220;Scripting.FileSystemObject&#8221;)  
Set WshNetwork = WScript.CreateObject(&#8220;WScript.Network&#8221;)

ON ERROR RESUME NEXT

If Not objFSO.DriveExists (&#8220;H:&#8221;) Then  
WshNetwork.MapNetworkDrive &#8220;H:&#8221;, &#8220;\\ServerNT\&#8221; &#038; WshNetwork.UserName  
End If  
If Not objFSO.DriveExists (&#8220;T:&#8221;) Then  
WshNetwork.MapNetworkDrive &#8220;T:&#8221;,&#8221;\\ServerNT\Transito&#8221;  
End If

strUNCPrinter1 = &#8220;\\Printer\Agenti&#8221;  
objNetwork.AddWindowsPrinterConnection strUNCPrinter1  
objNetwork.SetDefaultPrinter strUNCPrinter1  
Wscript.Quit