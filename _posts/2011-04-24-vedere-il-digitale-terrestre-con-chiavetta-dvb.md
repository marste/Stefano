---
id: 839
title: Vedere il Digitale Terrestre con chiavetta DVB
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/?p=839
permalink: /vedere-il-digitale-terrestre-con-chiavetta-dvb/
authorsure_include_css:
  - 
dsq_thread_id:
  - 1899928947
categories:
  - Linux
tags:
  - channels
  - Dexatek
  - digitale terrestre
  - dongle
  - dvb
  - frequenze
  - mencoder
  - mplayer
  - RTL2832U
  - tv
---
Io posseggo la chiavetta USB marchiata Think Xtra (RTL2832U) che da Ubuntu viene riconosciuta così:  
`Bus 001 Device 004: ID 1d19:1101 Dexatek Technology Ltd. DK DVB-T Dongle`  
Occorre installare:  
`` sudo apt-get install mercurial build-essential linux-headers-`uname -r` ``  
`hg clone http://linuxtv.org/hg/v4l-dvb`  
`cd v4l-dvb`  
`wget http://xgazza.altervista.org/Linux/DVB/Drivers/RTL2832U_patch_v4l_dvb.diff`  
`patch -p1 < RTL2832U_patch_v4l_dvb.diff`  
`make`  
`sudo make install`  
Poi:  
`sudo apt-get install dvb-apps`  
Vai sul sito: <a href="http://www.dgtvi.it/" target="_blank">http://www.dgtvi.it/</a> e cerca la tua città.  
Ti si aprirà una pagina in cui compariranno i canali, clicca su &#8220;**elenco multiplex**&#8221; per vedere le frequenze.

Creiamo un file **frequenze.txt** e inseriamo ad esempio:  
T **706**000000 8MHz 2/3 1/2 QAM64 8k 1/32 NONE  
Dove il **706** è la frequenza che trovo sul sito.

Aggiungi tutte le frequenze che vedi nel file che verrà tipo così:

T 682000000 8MHz 2/3 1/2 QAM64 8k 1/32 NONE  
T 802000000 8MHz 2/3 1/2 QAM64 8k 1/32 NONE  
T 786000000 8MHz 2/3 1/2 QAM64 8k 1/32 NONE  
T 506000000 8MHz 2/3 1/2 QAM64 8k 1/32 NONE  
T 690000000 8MHz 2/3 1/2 QAM64 8k 1/32 NONE  
T 490000000 8MHz 2/3 1/2 QAM64 8k 1/32 NONE  
T 546000000 8MHz 2/3 1/2 QAM64 8k 1/32 NONE  
T 514000000 8MHz 2/3 1/2 QAM64 8k 1/32 NONE  
T 626000000 8MHz 2/3 1/2 QAM64 8k 1/32 NONE  
T 706000000 8MHz 2/3 1/2 QAM64 8k 1/32 NONE  
T 722000000 8MHz 2/3 1/2 QAM64 8k 1/32 NONE  
T 594000000 8MHz 2/3 1/2 QAM64 8k 1/32 NONE  
T 698000000 8MHz 2/3 1/2 QAM64 8k 1/32 NONE  
T 758000000 8MHz 2/3 1/2 QAM64 8k 1/32 NONE  
T 770000000 8MHz 2/3 1/2 QAM64 8k 1/32 NONE

Attacchiamo la nostra chiavetta USB e digitiamo:  
`scan frequenze.txt`  
Vedrai:  
`using ‘/dev/dvb/adapter0/frontend0′ and ‘/dev/dvb/adapter0/demux0′`  
Significa che avete i driver installati, e il frontend e’ stato assegnato. Tutto Ok

Allora fai così:  
`scan frequenze.txt > channels.conf`  
In questo file channels.conf verranno scritti i canali e la loro frequenza.  
Esempio:  
`Rete4:698000000:INVERSION_AUTO:BANDWIDTH_8_MHZ:FEC_3_4:FEC_3_4:QAM_64:TRANSMISSION_MODE_8K:GUARD_INTERVAL_1_4:HIERARCHY_NONE:1630:1631:4004 Canale5:698000000:INVERSION_AUTO:BANDWIDTH_8_MHZ:FEC_3_4:FEC_3_4:QAM_64:TRANSMISSION_MODE_8K:GUARD_INTERVAL_1_4:HIERARCHY_NONE:1610:1611:4005 Italia1:698000000:INVERSION_AUTO:BANDWIDTH_8_MHZ:FEC_3_4:FEC_3_4:QAM_64:TRANSMISSION_MODE_8K:GUARD_INTERVAL_1_4:HIERARCHY_NONE:1620:1621:4006 Mediaset Extra:698000000:INVERSION_AUTO:BANDWIDTH_8_MHZ:FEC_3_4:FEC_3_4:QAM_64:TRANSMISSION_MODE_8K:GUARD_INTERVAL_1_4:HIERARCHY_NONE:1760:1761:4011 La 5:698000000:INVERSION_AUTO:BANDWIDTH_8_MHZ:FEC_3_4:FEC_3_4:QAM_64:TRANSMISSION_MODE_8K:GUARD_INTERVAL_1_4:HIERARCHY_NONE:1730:1731:4013 TG Mediaset:698000000:INVERSION_AUTO:BANDWIDTH_8_MHZ:FEC_3_4:FEC_3_4:QAM_64:TRANSMISSION_MODE_8K:GUARD_INTERVAL_1_4:HIERARCHY_NONE:1810:1811:4014`  
Salva questo file in:  
`/etc/mplayer`  
A questo punto, per vedere ad esempio Rete4, basterà digitare:  
`mplayer dvb://Rete4`  
Se andrà un po&#8217; a scatti consiglio di digitare:  
`mplayer -cache 8192 dvb://Rete4`  
Grazie a <a href="http://forum.ubuntu-it.org/index.php/topic,413840.msg3406367.html#msg3406367" target="_blank">questo link </a>e a <a href="http://divilinux.netsons.org/archives/435" target="_blank">quest&#8217;altro</a>.

Per registrare, posso consigliare mencoder:

`mencoder dvb://"Canale5" -ovc lavc -lavcopts aspect=16/9 vcodec=mpeg4:vbitrate=5000 -oac mp3lame -o test2.avi`

oppure

`mencoder dvb://"Italia1" -ovc lavc -lavcopts aspect=16/9 vcodec=mpeg2video:vrc_buf_size=1835:vrc_maxrate=9800:vbitrate=5000 -oac mp3lame -o test4.avi`

ma meglio ancora:  
`mencoder dvb://Canale5 -o canale5.avi -ovc xvid -xvidencopts bitrate=800 -oac mp3lame -lameopts cbr:br=128`