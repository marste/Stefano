---
id: 3182
title: 'Robocopy &#8211; Move files and directory from one to another with exclusion'
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=3182
permalink: /robocopy-move-files-and-directory-from-one-to-another-with-exclusion/
authorsure_include_css:
  - 
dsq_thread_id:
  - 3279736719
categories:
  - Windows
tags:
  - directory
  - files
  - move
  - sposta
---
<!-- HTML generated using hilite.me -->

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
  <pre style="margin: 0; line-height: 125%">@<span style="color: #008800; font-weight: bold">ECHO</span> <span style="color: #008800; font-weight: bold">OFF</span>
<span style="color: #008800; font-weight: bold">SETLOCAL</span>


<span style="color: #008800; font-weight: bold">SET</span> <span style="color: #336699">_source</span>=<span style="color: #dd2200; background-color: #fff0f0">"\\netapp\Home_Share\Transito"</span>

<span style="color: #008800; font-weight: bold">SET</span> <span style="color: #336699">_dest</span>=<span style="color: #dd2200; background-color: #fff0f0">"\\netapp\Home_Share\TransitOLD"</span>

<span style="color: #008800; font-weight: bold">SET</span> <span style="color: #336699">_what</span>=/COPYALL /SEC /E /Z /R:3 /W:2 /MOVE /XD <span style="color: #dd2200; background-color: #fff0f0">"\\netapp\Home_Share\Transito\Test"</span> <span style="color: #dd2200; background-color: #fff0f0">"\\netapp\Home_Share\Transito\Prova"</span> <span style="color: #dd2200; background-color: #fff0f0">"\\netapp\Home_Share\Transito\ICT"</span> <span style="color: #dd2200; background-color: #fff0f0">"\\netapp\Home_Share\Transito\Produzione"</span>

<span style="color: #888888">:: /COPYALL :: COPY ALL file info</span>
<span style="color: #888888">:: /B :: copy files in Backup mode.</span>
<span style="color: #888888">:: /SEC :: copy files with SECurity</span>
<span style="color: #888888">:: /MIR :: MIRror a directory tree</span>

<span style="color: #008800; font-weight: bold">SET</span> <span style="color: #336699">_options</span>=/R:0 /W:0 /LOG:MyLogfile2.txt /NFL /NDL
<span style="color: #888888">:: /R:n :: number of Retries</span>
<span style="color: #888888">:: /W:n :: Wait time between retries</span>
<span style="color: #888888">:: /LOG :: Output log file</span>
<span style="color: #888888">:: /NFL :: No file logging</span>
<span style="color: #888888">:: /NDL :: No dir logging</span>

ROBOCOPY <span style="color: #336699">%_source%</span> <span style="color: #336699">%_dest%</span> <span style="color: #336699">%_what%</span>
</pre>
</div>