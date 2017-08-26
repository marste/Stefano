---
id: 103
title: Wake on LAN (WOL)
author: Stefano Marzorati
layout: post
guid: http://ubbunti.wordpress.com/2011/03/05/wake-on-lan-wol
permalink: /wake-on-lan-wol/
blogger_blog:
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
  - ubbunti.blogspot.com
blogger_author:
  - m@il_of_d@y
  - m@il_of_d@y
  - m@il_of_d@y
blogger_e466c7156e8bac77e64f63e8bad92c92_permalink:
  - 8088673473386015615
  - 8088673473386015615
  - 8088673473386015615
dsq_thread_id:
  - 1953653541
categories:
  - Linux
---
**Requisiti:**

Verificare che WOL sia attivato nel Bios dei pc che vogliamo accendere.

> `# <span style="color:#0000ff;">apt-get install ethtool wakeonlan</span>`

verificare che sulla schede di rete sia abilitato WOL:

> `# <span style="color:#0000ff;">ethtool eth0</span>`

il risultato nel mio caso è questo:

&nbsp;

> root@debian:/home/edmond# ethtool eth0  
> Settings for eth0:  
> Supported ports: [ TP ] Supported link modes: 10baseT/Half 10baseT/Full  
> 100baseT/Half 100baseT/Full  
> 1000baseT/Full  
> Supports auto-negotiation: Yes  
> Advertised link modes: 10baseT/Half 10baseT/Full  
> 100baseT/Half 100baseT/Full  
> 1000baseT/Full  
> Advertised pause frame use: No  
> Advertised auto-negotiation: Yes  
> Speed: 100Mb/s  
> Duplex: Full  
> Port: Twisted Pair  
> PHYAD: 1  
> Transceiver: internal  
> Auto-negotiation: on  
> MDI-X: on  
> Supports Wake-on: pumbag  
> <span style="color:#ff0000;">Wake-on: g</span>  
> Current message level: 0×00000001 (1)  
> Link detected: yes

&#8220;**g**&#8221; significa che WOL è abilitato

nel caso fosse su &#8220;**d**&#8221; significa che è disabilitato, quindi per abilitarlo:

&nbsp;

> `# <span style="color:#0000ff;">ethtool -s eth0 wol g</span>`

creare uno script chiamato **wol** ed inserire:

&nbsp;

> \## /etc/init.d/wol  
> #  
> \# chkconfig: 2345 99 99  
> \# description: Force NIC into WOL mode  
> #  
> ethtool -s eth0 wol umbg  
> exit

quindi:

&nbsp;

> `$ <span style="color:#0000ff;">chmod a+x wol</span>`
> 
> `# <span style="color:#0000ff;">cp wol /etc/init.d/</span>`
> 
> `# <span style="color:#0000ff;">update-rc.d wol defaults</span>`

adesso per svegliare il nostro pc, basta inviare i Magic Packet:

&nbsp;

> `$ <span style="color:#0000ff;">wakeonlan indirizzo_mac_pc</span>`
> 
> <p style="text-align:left;">
>   <code>&lt;span style="color:#0000ff;">&lt;a href="http://www.edmondweblog.com/index.php/2011/01/06/wake-on-lan-wol-su-debian-squeeze/">via&lt;/a>&lt;br />
&lt;/span></code>
> </p>