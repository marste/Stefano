---
id: 1505
title: Download from MTV OnDemand
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1505
permalink: /download-from-mtv-ondemand/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
layout_key:
  - 
post_slider_check_key:
  - 0
dsq_thread_id:
  - 1899874708
dsq_needs_sync:
  - 1
categories:
  - Linux
  - Windows
tags:
  - mtv
  - ondemand
---
Utilizzando Chrome, premere F12 e visualizzare il video, esempio:

<p style="text-align: center;">
  <a href="http://ondemand.mtv.it/serie-tv/mario-una-serie-di-maccio-capatonda/s01/mario-una-serie-di-maccio-capatonda-s01e01" target="_blank">http://ondemand.mtv.it/serie-tv/mario-una-serie-di-maccio-capatonda/s01/mario-una-serie-di-maccio-capatonda-s01e01</a>    <a href="http://res.cloudinary.com/marzorati-co/image/upload/v1408107884/chrome1_h76amk.png"><img class="alignnone size-full wp-image-2442" alt="chrome" src="http://res.cloudinary.com/marzorati-co/image/upload/v1408107884/chrome1_h76amk.png" /></a>
</p>

Guarda la sezione &#8220;**Network**&#8220;, come si vede nell&#8217;immagine sopra e trova il file  
**mediaGen.jhtml?uri=&#8230;.** che contiene la **Request URL** <a href="http://intl.esperanto.mtvi.com/www/xml/media/mediaGen.jhtml?uri=mgi..." target="_blank">http://intl.esperanto.mtvi.com/www/xml/media/mediaGen.jhtml?uri=mgi&#8230;</a>

Incolla la request url in una nuova pagina e si aprirà un file .xml contenente i links dei vari formati dei file mp4.

Con <a href="http://www.videohelp.com/tools/RTMPDump" target="_blank">RTMPDump</a>:  
`rtmpdump.exe -r "rtmpe://cp24806.edgefcs.net/ondemand/mtviestor/_!/intlod/it/ontv/mario_mtg/stagione_01/it_mario_mtg_103_768x432_1700_m30.mp4" -o "C:\Video3.mp4" -e`

Ogni tanto si interromperà prima di arrivare al 100% del download, non c&#8217;è problema, rilanciate la stringa e riprenderà il download.

Se si interrompe troppe volte e volete far in modo che ritenti il download automaticamente fino alla fine, ecco un batch Windows:

<!-- HTML generated using hilite.me -->

<div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;">
  <pre style="margin: 0; line-height: 125%">@<span style="color: #008800; font-weight: bold">ECHO</span> <span style="color: #008800; font-weight: bold">OFF</span>
<span style="color: #008800; font-weight: bold">SET</span> <span style="color: #996633">a</span> <span style="color: #333333">=</span> <span style="color: #6600EE; font-weight: bold"></span>

<span style="color: #008800; font-weight: bold">ECHO</span> _________________________ &gt;&gt; C:Download.txt
<span style="color: #008800; font-weight: bold">ECHO</span> Provo a scaricare: <span style="color: #996633">%date%</span> <span style="color: #996633">%time%</span> &gt;&gt; C:\Download.txt
rtmpdump -r rtmpe://cp24806.edgefcs.net/ondemand/mtviestor/_!/intlod/it/ontv/il_testimone/stagione_05/it_iltestimone_515_1280x720_3500_h32.mp4 -o c:Dubai_<span style="color: #6600EE; font-weight: bold">2</span>_parte.mp<span style="color: #6600EE; font-weight: bold">4</span> -e
<span style="color: #008800; font-weight: bold">set</span> /a iNetUseVariable <span style="color: #333333">=</span> <span style="color: #996633">%errorlevel%</span>
<span style="color: #008800; font-weight: bold">ECHO</span> Risultato: (<span style="color: #996633">%iNetUseVariable%</span>) <span style="color: #996633">%date%</span> <span style="color: #996633">%time%</span> &gt;&gt; C:\Download.txt
<span style="color: #008800; font-weight: bold">if</span> <span style="color: #996633">%iNetUseVariable%</span> <span style="color: #333333">EQU</span> <span style="color: #6600EE; font-weight: bold"></span> (<span style="color: #008800; font-weight: bold">GOTO</span> <span style="color: #997700; font-weight: bold">close</span>) <span style="color: #008800; font-weight: bold">ELSE</span> ( <span style="color: #008800; font-weight: bold">GOTO</span> <span style="color: #997700; font-weight: bold">retry</span> )

<span style="color: #997700; font-weight: bold">:retry</span>
<span style="color: #008800; font-weight: bold">set</span> /a a<span style="color: #333333">=</span><span style="color: #996633">%a%</span> + <span style="color: #6600EE; font-weight: bold">1</span> 
<span style="color: #008800; font-weight: bold">if</span> <span style="color: #996633">%a%</span> <span style="color: #333333">==</span> <span style="color: #6600EE; font-weight: bold">60</span> (<span style="color: #008800; font-weight: bold">GOTO</span> <span style="color: #997700; font-weight: bold">error</span>) <span style="color: #008800; font-weight: bold">ELSE</span> (<span style="color: #008800; font-weight: bold">GOTO</span> <span style="color: #997700; font-weight: bold">remount</span>)

<span style="color: #997700; font-weight: bold">:remount</span>
<span style="color: #008800; font-weight: bold">ECHO</span> Error: <span style="color: #996633">%date%</span> <span style="color: #996633">%time%</span> &gt;&gt; C:\Download.txt
<span style="color: #008800; font-weight: bold">ECHO</span> Interrotto: <span style="color: #996633">%date%</span> <span style="color: #996633">%time%</span> &gt;&gt; C:\Download.txt
<span style="color: #008800; font-weight: bold">ECHO</span> Riprovo: <span style="color: #996633">%date%</span> <span style="color: #996633">%time%</span> &gt;&gt; C:\Download.txt
rtmpdump -r rtmpe://cp24806.edgefcs.net/ondemand/mtviestor/_!/intlod/it/ontv/il_testimone/stagione_05/it_iltestimone_515_1280x720_3500_h32.mp4 -o c:Dubai_<span style="color: #6600EE; font-weight: bold">2</span>_parte.mp<span style="color: #6600EE; font-weight: bold">4</span> -e
<span style="color: #008800; font-weight: bold">set</span> /a iNetUseVariable <span style="color: #333333">=</span> <span style="color: #996633">%errorlevel%</span>
<span style="color: #008800; font-weight: bold">ECHO</span> Risultato: (<span style="color: #996633">%iNetUseVariable%</span>) <span style="color: #996633">%date%</span> <span style="color: #996633">%time%</span> &gt;&gt; C:Download.txt
<span style="color: #008800; font-weight: bold">IF</span> <span style="color: #996633">%iNetUseVariable%</span> <span style="color: #333333">EQU</span> <span style="color: #6600EE; font-weight: bold"></span> (<span style="color: #008800; font-weight: bold">GOTO</span> <span style="color: #997700; font-weight: bold">close</span>) <span style="color: #008800; font-weight: bold">ELSE</span> (<span style="color: #008800; font-weight: bold">GOTO</span> <span style="color: #997700; font-weight: bold">retry</span>)


<span style="color: #997700; font-weight: bold">:close</span>
<span style="color: #008800; font-weight: bold">ECHO</span> Scaricato: <span style="color: #996633">%date%</span> <span style="color: #996633">%time%</span> &gt;&gt; C:\Download.txt
exit

<span style="color: #997700; font-weight: bold">:error</span>
<span style="color: #008800; font-weight: bold">ECHO</span> Unknown error: <span style="color: #996633">%data</span> <span style="color: #996633">%time%</span> &gt;&gt; C:\Download.txt
exit
</pre>
</div>

Se ti occorre convertire il file mp4 in avi per vederlo eventualmente su una Smart TV, puoi usare:

`ffmpeg -i c:\video.mp4 -acodec mp3 -vcodec libx264 -preset ultrafast c:\video.avi`
