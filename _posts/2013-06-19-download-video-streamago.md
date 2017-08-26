---
id: 1696
title: Download video da Streamago
author: Stefano Marzorati
layout: post
guid: http://marzorati.co/?p=1696
permalink: /download-video-streamago/
publicize_twitter_user:
  - marzorati_ste
  - marzorati_ste
authorsure_include_css:
  - 
dsq_thread_id:
  - 1902021208
layout_key:
  - 
post_slider_check_key:
  - 0
categories:
  - Linux
  - Windows
---
Con **URL Snooper** cattura il flusso.

**Vedrai una url tipo:**  
`<a href="Krtmp://94.32.97.9:80/cache?idutente=29664&idcanale=23952&idmovie=32780&pwd=" target="_blank">Krtmp://94.32.97.9:80/cache?idutente=29664&idcanale=23952&idmovie=32780&pwd=</a>`

**Segnati la versione di Flash:**  
`11,7,700,224`

**Segnati il path del file swf:**  
`<a href="http://www.streamago.tv/app/StreamVideo.swf" target="_blank">http://www.streamago.tv/app/StreamVideo.swf</a>`

**Segnati l&#8217;url della pagina in cui compare il video:**  
`<a href="http://www.streamago.tv/general/29664/motociclismo/web-2013-06-16-19-21-52.html" target="_blank">http://www.streamago.tv/general/29664/motociclismo/web-2013-06-16-19-21-52.html</a>`

**Segnati parte dell&#8217;ulr che contiene il file .mp4, specificando il formato del file:**  
Apri Chrome, premi F12 e guarda la sezione &#8220;Network&#8221;  
Tra i file scaricati troverai un file xml, esempio: &#8220;web-2013-10-13-18-20-07.43740.xml&#8221;  
Apri la **Request URL**:<a href="http://www.streamago.tv/xml/23790/web-2013-10-13-18-20-07.43740.xml" target="_blank">http://www.streamago.tv/xml/23790/web-2013-10-13-18-20-07.43740.xml</a> in una nuova pagina e troverai il percorso del file **.mp4**  
`streamago-vod/stg02/29/29664/23952/mp4:web1371401974003.mp4`

Con rtmpdump componi questa stringa:  
`rtmpdump -r "rtmp://94.32.101.17:80/cache?idutente=29664&idcanale=23952&idmovie=32780&pwd=" -a "cache?idutente=29664&idcanale=23952&idmovie=32780&pwd=" -f "WIN 11,7,700,224" -W "http://www.streamago.tv/app/StreamVideo.swf" -p "http://www.streamago.tv/general/29664/motociclismo/web-2013-06-16-19-21-52.html" -y "streamago-vod/stg02/29/29664/23952/mp4:web1371401974003.mp4" -o mp4_web1371401974003.flv --realtime -e`

Se non arrivasse al 100% del download, aggiungi l&#8217;opzione &#8220;-e&#8221; per riprendere il download da dove era arrivato.