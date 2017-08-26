---
id: 3180
title: 'Empty contents of a directory &#8211; vbs'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3180
permalink: /empty-contents-of-a-directory-vbs/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3279714310
categories:
  - Windows
tags:
  - contenuto
  - directory
  - svuotare
  - vbs
---
Esempio:

<!-- HTML generated using hilite.me -->

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
  <pre style="margin: 0; line-height: 125%">strFolder = <span style="color: #dd2200; background-color: #fff0f0">"\\netapp\Home_Share\TransitOLD"</span>
intDays = <span style="color: #0000DD; font-weight: bold"></span>
 
<span style="color: #008800; font-weight: bold">Set</span> objFSO	  = CreateObject(<span style="color: #dd2200; background-color: #fff0f0">"Scripting.FileSystemObject"</span>)
<span style="color: #008800; font-weight: bold">Set</span> objFolders  = objFSO.GetFolder(strFolder)
objToday				= Now()
objPastDate	 = DateAdd(<span style="color: #dd2200; background-color: #fff0f0">"d"</span>, intDays*-<span style="color: #0000DD; font-weight: bold">1</span>, objToday)
 
Recurse objFolders



<span style="color: #008800; font-weight: bold">Sub</span> <span style="color: #0066bb; font-weight: bold">recurse</span>(<span style="color: #008800; font-weight: bold">ByRef</span> objFolders)
 
	<span style="color: #008800; font-weight: bold">Set</span> objSubFolders = objFolders.SubFolders
	<span style="color: #008800; font-weight: bold">Set</span> objFiles = objFolders.Files
 
	<span style="color: #008800; font-weight: bold">for</span> <span style="color: #008800; font-weight: bold">each</span> File <span style="color: #008800">in</span> objFiles
		<span style="color: #008800; font-weight: bold">if</span> File.DateLastModified &lt; objPastDate <span style="color: #008800; font-weight: bold">then</span>
			<span style="color: #008800; font-weight: bold">On</span> <span style="color: #008800; font-weight: bold">Error</span> <span style="color: #008800; font-weight: bold">Resume</span> <span style="color: #008800; font-weight: bold">Next</span>
			File.Delete
		<span style="color: #008800; font-weight: bold">end</span> <span style="color: #008800; font-weight: bold">if</span>
	<span style="color: #008800; font-weight: bold">Next</span>
 
	<span style="color: #008800; font-weight: bold">For</span> <span style="color: #008800; font-weight: bold">Each</span> Folder <span style="color: #008800">in</span> objSubFolders
		<span style="color: #008800; font-weight: bold">If</span> Folder.DateLastModified &lt; objPastDate <span style="color: #008800; font-weight: bold">Then</span>
			objFSO.DeleteFolder Folder.Path, <span style="color: #008800; font-weight: bold">True</span>
		<span style="color: #008800; font-weight: bold">Else</span>
			Recurse Folder
		<span style="color: #008800; font-weight: bold">End</span> <span style="color: #008800; font-weight: bold">If</span>
	<span style="color: #008800; font-weight: bold">Next</span>
 
	<span style="color: #008800; font-weight: bold">Set</span> objSubFolders = <span style="color: #008800; font-weight: bold">Nothing</span>
	<span style="color: #008800; font-weight: bold">Set</span> objFiles = <span style="color: #008800; font-weight: bold">Nothing</span>
 
<span style="color: #008800; font-weight: bold">end</span> <span style="color: #008800; font-weight: bold">Sub</span>
</pre>
</div>