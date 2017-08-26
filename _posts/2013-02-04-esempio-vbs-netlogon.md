---
id: 1336
title: Esempio vbs netlogon
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1336
permalink: /esempio-vbs-netlogon/
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:1;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:1;}}'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 2442702025
categories:
  - Windows
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
WshNetwork.MapNetworkDrive &#8220;H:&#8221;, &#8220;\Server&#8221; & WshNetwork.UserName  
End If  
If Not objFSO.DriveExists (&#8220;T:&#8221;) Then  
WshNetwork.MapNetworkDrive &#8220;T:&#8221;,&#8221;\ServerTransito&#8221;  
End If

strUNCPrinter1 = &#8220;\PrinterCommerciali&#8221;  
objNetwork.AddWindowsPrinterConnection strUNCPrinter1  
objNetwork.SetDefaultPrinter strUNCPrinter1  
Wscript.Quit

<div id="dc_vk_code" style="display:none;">
</div>