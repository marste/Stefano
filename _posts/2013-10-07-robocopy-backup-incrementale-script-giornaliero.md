---
id: 2026
title: Script giornaliero Robocopy backup incrementale
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=2026
permalink: /robocopy-backup-incrementale-script-giornaliero/
publicize_twitter_url:
  - http://t.co/bcsnTIPX4t
  - http://t.co/bcsnTIPX4t
publicize_linkedin_url:
  - 'http://www.linkedin.com/updates?discuss=&scope=114372254&stype=M&topic=5792969139047899137&type=U&a=SNHW'
  - 'http://www.linkedin.com/updates?discuss=&scope=114372254&stype=M&topic=5792969139047899137&type=U&a=SNHW'
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
publicize_reach:
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
  - 'a:2:{s:7:"twitter";a:1:{i:3411;i:27;}s:2:"wp";a:1:{i:0;i:2;}}'
authorsure_include_css:
  - 
layout_key:
  - 
post_slider_check_key:
  - 0
dsq_thread_id:
  - 1899928987
categories:
  - Windows
tags:
  - backup
  - incrementale
  - robocopy
  - script
---
![robocopy](http://comptb.cects.com/wp-content/uploads/2014/01/robocopy_output.jpg)   

<!-- HTML generated using hilite.me -->

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
  <pre style="margin: 0; line-height: 125%">@<span style="color: #008800; font-weight: bold">echo</span> <span style="color: #008800; font-weight: bold">off</span>
title Backing Up Files...
color <span style="color: #6600EE; font-weight: bold"></span>A

<span style="color: #888888">rem ******************************************************************************************</span>
<span style="color: #888888">rem * Use variable BV to define location of backup storage volume.                           *</span>
<span style="color: #888888">rem * Do not include trailing &#39;\&#39; character. Do not enclose paths with spaces in quotes.     *</span>
<span style="color: #888888">rem ******************************************************************************************</span>

<span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">BV</span><span style="color: #333333">=</span>C:\tmp

<span style="color: #888888">rem ******************************************************************************************</span>
<span style="color: #888888">rem * Use variable EXC to define the name of directories to be EXCluded from the backup.     *</span>
<span style="color: #888888">rem *                                                                                        *</span>
<span style="color: #888888">rem ******************************************************************************************</span>

<span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">EXC</span><span style="color: #333333">=</span><span style="background-color: #fff0f0">"Temp"</span> <span style="background-color: #fff0f0">"TMP"</span> <span style="background-color: #fff0f0">"Temporary Internet Files"</span> <span style="background-color: #fff0f0">"Cookies"</span> <span style="background-color: #fff0f0">"Recent"</span>

<span style="color: #888888">rem ******************************************************************************************</span>
<span style="color: #888888">rem * Set the backup file TTL (Time To Live) in days.  The backup script will not maintain   *</span>
<span style="color: #888888">rem * backup history beyond the specified number of days.  This is a crude way of keeping    *</span>
<span style="color: #888888">rem * the backup volume from being overfilled.  Adjust this value to provide maxiumum backup *</span>
<span style="color: #888888">rem * history for the amount of data that is being backed up, given the amount of disk space</span>
<span style="color: #888888">rem * available to store it.                                         *</span>
<span style="color: #888888">rem ******************************************************************************************</span>

<span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">BTTL</span><span style="color: #333333">=</span><span style="color: #6600EE; font-weight: bold">32</span>

<span style="color: #888888">rem ******************************************************************************************</span>
<span style="color: #888888">rem * Check to see if the defined backup storage volume is accessible. Some external storage *</span>
<span style="color: #888888">rem * devices will enter a power saving mode (sleep) that may cause this process to fail,    *</span>
<span style="color: #888888">rem * so we&#39;ll check to see if the OS reports the volume as available.                         *</span>
<span style="color: #888888">rem ******************************************************************************************</span>

<span style="color: #008800; font-weight: bold">echo</span>.
<span style="color: #008800; font-weight: bold">echo</span>  Initializing, please wait...
<span style="color: #008800; font-weight: bold">echo</span>.

dir <span style="color: #996633">%BV%</span>

<span style="color: #008800; font-weight: bold">if</span> not <span style="color: #008800; font-weight: bold">exist</span> <span style="background-color: #fff0f0">"%BV%"</span> (
    title Backup Process Failed
    color C<span style="color: #6600EE; font-weight: bold"></span>
    <span style="color: #008800; font-weight: bold">echo</span>.
    <span style="color: #008800; font-weight: bold">echo</span>.
    <span style="color: #008800; font-weight: bold">echo</span>.
    <span style="color: #008800; font-weight: bold">echo</span>.
    <span style="color: #008800; font-weight: bold">echo</span>   The backup volume, <span style="color: #996633">%BV%</span>, appears to be inaccessible.  You may not perform
    <span style="color: #008800; font-weight: bold">echo</span>   a backup at this time.
    <span style="color: #008800; font-weight: bold">echo</span>.
    <span style="color: #008800; font-weight: bold">echo</span>.
    <span style="color: #008800; font-weight: bold">echo</span>.
    <span style="color: #008800; font-weight: bold">echo</span>.
    <span style="color: #008800; font-weight: bold">pause</span>
    exit
)

<span style="color: #888888">rem ******************************************************************************************</span>
<span style="color: #888888">rem *  Determine the month week, time, and day numbers for the construction of the backup    *</span>
<span style="color: #888888">rem *  file names.                                                                           *</span>
<span style="color: #888888">rem ******************************************************************************************</span>

<span style="color: #008800; font-weight: bold">FOR</span> /F <span style="background-color: #fff0f0">"TOKENS=1,2* delims=/ "</span> <span style="color: #996633">%%A</span> IN (<span style="background-color: #fff0f0">&#39;DATE/T&#39;</span>) <span style="color: #008800; font-weight: bold">DO</span> <span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">MON</span><span style="color: #333333">=</span><span style="color: #996633">%date:~3</span>,<span style="color: #6600EE; font-weight: bold">2</span>%
<span style="color: #008800; font-weight: bold">FOR</span> /F <span style="background-color: #fff0f0">"TOKENS=1,2,3* delims=/ "</span> <span style="color: #996633">%%A</span> IN (<span style="background-color: #fff0f0">&#39;DATE/T&#39;</span>) <span style="color: #008800; font-weight: bold">DO</span> <span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">DAY</span><span style="color: #333333">=</span><span style="color: #996633">%date:~0</span>,<span style="color: #6600EE; font-weight: bold">2</span>%
<span style="color: #008800; font-weight: bold">FOR</span> /f <span style="background-color: #fff0f0">"TOKENS=1,2,3 delims=: "</span> <span style="color: #996633">%%A</span> in (<span style="background-color: #fff0f0">&#39;TIME /T&#39;</span>) <span style="color: #008800; font-weight: bold">do</span> <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">TM</span><span style="color: #333333">=</span><span style="color: #996633">%date:~</span><span style="color: #6600EE; font-weight: bold">-4</span>,<span style="color: #6600EE; font-weight: bold">4</span>%

<span style="color: #008800; font-weight: bold">IF</span> <span style="color: #996633">%MON%</span> <span style="color: #333333">==</span> <span style="color: #6600EE; font-weight: bold">01</span> (<span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">MONTH</span><span style="color: #333333">=</span>Gennaio
 <span style="color: #008800; font-weight: bold">goto</span> <span style="color: #997700; font-weight: bold">:begin</span>)
<span style="color: #008800; font-weight: bold">IF</span> <span style="color: #996633">%MON%</span> <span style="color: #333333">==</span> <span style="color: #6600EE; font-weight: bold">02</span> (<span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">MONTH</span><span style="color: #333333">=</span>Febbraio
 <span style="color: #008800; font-weight: bold">goto</span> <span style="color: #997700; font-weight: bold">:begin</span>)
<span style="color: #008800; font-weight: bold">IF</span> <span style="color: #996633">%MON%</span> <span style="color: #333333">==</span> <span style="color: #6600EE; font-weight: bold">03</span> (<span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">MONTH</span><span style="color: #333333">=</span>Marzo
 <span style="color: #008800; font-weight: bold">goto</span> <span style="color: #997700; font-weight: bold">:begin</span>)
<span style="color: #008800; font-weight: bold">IF</span> <span style="color: #996633">%MON%</span> <span style="color: #333333">==</span> <span style="color: #6600EE; font-weight: bold">04</span> (<span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">MONTH</span><span style="color: #333333">=</span>Aprile
 <span style="color: #008800; font-weight: bold">goto</span> <span style="color: #997700; font-weight: bold">:begin</span>)
<span style="color: #008800; font-weight: bold">IF</span> <span style="color: #996633">%MON%</span> <span style="color: #333333">==</span> <span style="color: #6600EE; font-weight: bold">05</span> (<span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">MONTH</span><span style="color: #333333">=</span>Maggio
 <span style="color: #008800; font-weight: bold">goto</span> <span style="color: #997700; font-weight: bold">:begin</span>)
<span style="color: #008800; font-weight: bold">IF</span> <span style="color: #996633">%MON%</span> <span style="color: #333333">==</span> <span style="color: #6600EE; font-weight: bold">06</span> (<span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">MONTH</span><span style="color: #333333">=</span>Giugno
 <span style="color: #008800; font-weight: bold">goto</span> <span style="color: #997700; font-weight: bold">:begin</span>)
<span style="color: #008800; font-weight: bold">IF</span> <span style="color: #996633">%MON%</span> <span style="color: #333333">==</span> <span style="color: #6600EE; font-weight: bold">07</span> (<span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">MONTH</span><span style="color: #333333">=</span>Luglio
 <span style="color: #008800; font-weight: bold">goto</span> <span style="color: #997700; font-weight: bold">:begin</span>)
<span style="color: #008800; font-weight: bold">IF</span> <span style="color: #996633">%MON%</span> <span style="color: #333333">==</span> <span style="color: #6600EE; font-weight: bold">08</span> (<span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">MONTH</span><span style="color: #333333">=</span>Agosto
 <span style="color: #008800; font-weight: bold">goto</span> <span style="color: #997700; font-weight: bold">:begin</span>)
<span style="color: #008800; font-weight: bold">IF</span> <span style="color: #996633">%MON%</span> <span style="color: #333333">==</span> <span style="color: #6600EE; font-weight: bold">09</span> (<span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">MONTH</span><span style="color: #333333">=</span>Settembre
 <span style="color: #008800; font-weight: bold">goto</span> <span style="color: #997700; font-weight: bold">:begin</span>)
<span style="color: #008800; font-weight: bold">IF</span> <span style="color: #996633">%MON%</span> <span style="color: #333333">==</span> <span style="color: #6600EE; font-weight: bold">10</span> (<span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">MONTH</span><span style="color: #333333">=</span>Ottobre
 <span style="color: #008800; font-weight: bold">goto</span> <span style="color: #997700; font-weight: bold">:begin</span>)
<span style="color: #008800; font-weight: bold">IF</span> <span style="color: #996633">%MON%</span> <span style="color: #333333">==</span> <span style="color: #6600EE; font-weight: bold">11</span> (<span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">MONTH</span><span style="color: #333333">=</span>Novembre
 <span style="color: #008800; font-weight: bold">goto</span> <span style="color: #997700; font-weight: bold">:begin</span>)
<span style="color: #008800; font-weight: bold">IF</span> <span style="color: #996633">%MON%</span> <span style="color: #333333">==</span> <span style="color: #6600EE; font-weight: bold">12</span> (<span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">MONTH</span><span style="color: #333333">=</span>Dicembre
 <span style="color: #008800; font-weight: bold">goto</span> <span style="color: #997700; font-weight: bold">:begin</span>)

<span style="color: #997700; font-weight: bold">:begin</span>

<span style="color: #008800; font-weight: bold">IF</span> <span style="color: #996633">%DAY%</span> <span style="color: #333333">LEQ</span> <span style="color: #6600EE; font-weight: bold">31</span> <span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">WEEK</span><span style="color: #333333">=</span>Four
<span style="color: #008800; font-weight: bold">IF</span> <span style="color: #996633">%DAY%</span> <span style="color: #333333">LEQ</span> <span style="color: #6600EE; font-weight: bold">21</span> <span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">WEEK</span><span style="color: #333333">=</span>Three
<span style="color: #008800; font-weight: bold">IF</span> <span style="color: #996633">%DAY%</span> <span style="color: #333333">LEQ</span> <span style="color: #6600EE; font-weight: bold">14</span> <span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">WEEK</span><span style="color: #333333">=</span>Two
<span style="color: #008800; font-weight: bold">IF</span> <span style="color: #996633">%DAY%</span> <span style="color: #333333">LEQ</span> <span style="color: #6600EE; font-weight: bold">07</span> <span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">WEEK</span><span style="color: #333333">=</span>One

<span style="color: #008800; font-weight: bold">echo</span>.
<span style="color: #008800; font-weight: bold">echo</span>.
<span style="color: #008800; font-weight: bold">echo</span>.
<span style="color: #008800; font-weight: bold">echo</span>   Beginning backup process, please wait...
<span style="color: #008800; font-weight: bold">echo</span>.
<span style="color: #008800; font-weight: bold">echo</span>.
<span style="color: #008800; font-weight: bold">echo</span>.

<span style="color: #888888">rem ******************************************************************************************</span>
<span style="color: #888888">rem * Before we copy a bunch of backup data to the backup volume, let&#39;s get rid of the old   *</span>
<span style="color: #888888">rem * stuff.  All files older than the amount of days defined by BTTL are deleted.           *</span>
<span style="color: #888888">rem ******************************************************************************************</span>

<span style="color: #008800; font-weight: bold">if</span> <span style="color: #008800; font-weight: bold">exist</span> <span style="background-color: #fff0f0">"%BV%"</span> (
    forfiles /p <span style="color: #996633">%BV%</span> /d -<span style="color: #996633">%BTTL%</span> /c <span style="background-color: #fff0f0">"CMD /Q /C @rmdir /S /Q @PATH"</span>
    forfiles /p <span style="color: #996633">%BV%</span> /d -<span style="color: #996633">%BTTL%</span> /c <span style="background-color: #fff0f0">"CMD /Q /C del /F /Q @PATH"</span>
    <span style="color: #008800; font-weight: bold">cls</span>
)

<span style="color: #888888">rem ******************************************************************************************</span>
<span style="color: #888888">rem * If the current months _Complete folder exists, a complete backup has already been      *</span>
<span style="color: #888888">rem * performed, so perform an incremental instead.                                          *</span>
<span style="color: #888888">rem ******************************************************************************************</span>

<span style="color: #008800; font-weight: bold">if</span> <span style="color: #008800; font-weight: bold">exist</span> <span style="background-color: #fff0f0">"%BV%\%MONTH%_Completo"</span> (
    <span style="color: #008800; font-weight: bold">echo</span>.
    <span style="color: #008800; font-weight: bold">echo</span>.
    <span style="color: #008800; font-weight: bold">echo</span>  Performing incremental backup...
    <span style="color: #008800; font-weight: bold">echo</span>.
    <span style="color: #008800; font-weight: bold">echo</span>.
    mkdir <span style="background-color: #fff0f0">"%BV%\%MONTH%_%DAY%_%TM%_Incrementale"</span>
    <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">BLOG</span><span style="color: #333333">=</span><span style="color: #996633">%BV%</span>\<span style="color: #996633">%MONTH%</span>_<span style="color: #996633">%DAY%</span>_<span style="color: #996633">%TM%</span>_Incrementale_BackupLog.txt
    robocopy <span style="background-color: #fff0f0">"C:\Cartella1"</span> <span style="background-color: #fff0f0">"%BV%\%MONTH%_%DAY%_%TM%_Incrementale\Cartella1"</span> /B /E /M /R:0 /V /NP /TEE /XJ /LOG+:"%BV%\%MONTH%_%DAY%_%TM%_Incrementale_BackupLog_Cartella1.txt" /XD <span style="color: #996633">%EXC%</span>
	robocopy <span style="background-color: #fff0f0">"C:\Cartella2"</span> <span style="background-color: #fff0f0">"%BV%\%MONTH%_%DAY%_%TM%_Incrementale\Cartella2"</span> /B /E /M /R:0 /V /NP /TEE /XJ /LOG+:"%BV%\%MONTH%_%DAY%_%TM%_Incrementale_BackupLog_Cartella2.txt" /XD <span style="color: #996633">%EXC%</span>
) <span style="color: #008800; font-weight: bold">else</span> (
    <span style="color: #008800; font-weight: bold">echo</span>.
    <span style="color: #008800; font-weight: bold">echo</span>.
    <span style="color: #008800; font-weight: bold">echo</span>  Performing complete backup...
    <span style="color: #008800; font-weight: bold">echo</span>.
    <span style="color: #008800; font-weight: bold">echo</span>.
    <span style="color: #008800; font-weight: bold">set</span> <span style="color: #996633">BLOG</span><span style="color: #333333">=</span><span style="color: #996633">%BV%</span>\<span style="color: #996633">%MONTH%</span>_Completo_BackupLog.txt
    robocopy <span style="background-color: #fff0f0">"C:\Cartella1"</span> <span style="background-color: #fff0f0">"%BV%\%MONTH%_Completo\Cartella1"</span> /B /E /R:0 /CREATE /NP /TEE /XJ /LOG+:"%BV%\%MONTH%_Completo_BackupLog_Cartella1.txt" /XD <span style="color: #996633">%EXC%</span>
    robocopy <span style="background-color: #fff0f0">"C:\Cartella1"</span> <span style="background-color: #fff0f0">"%BV%\%MONTH%_Completo\Cartella1"</span> /B /E /R:0 /V /NP /TEE /XJ /LOG+:"%BV%\%MONTH%_Completo_BackupLog_Cartella1.txt" /XD <span style="color: #996633">%EXC%</span>
	
	robocopy <span style="background-color: #fff0f0">"C:\Cartella2"</span> <span style="background-color: #fff0f0">"%BV%\%MONTH%_Completo\Cartella2"</span> /B /E /R:0 /CREATE /NP /TEE /XJ /LOG+:"%BV%\%MONTH%_Completo_BackupLog_Cartella2.txt" /XD <span style="color: #996633">%EXC%</span>
    robocopy <span style="background-color: #fff0f0">"C:\Cartella2"</span> <span style="background-color: #fff0f0">"%BV%\%MONTH%_Completo\Cartella2"</span> /B /E /R:0 /V /NP /TEE /XJ /LOG+:"%BV%\%MONTH%_Completo_BackupLog_Cartella2.txt" /XD <span style="color: #996633">%EXC%</span>
attrib -A <span style="background-color: #fff0f0">"C:\Cartella1\*.*"</span> /S
attrib -A <span style="background-color: #fff0f0">"C:\Cartella2\*.*"</span> /S
    )
)

<span style="color: #997700; font-weight: bold">:end</span>

exit
</pre>
</div>

In allegato, lo script di esempio:  
[Script Backup Incrementale][1]

 [1]: http://marzorati.co/download/backup.doc