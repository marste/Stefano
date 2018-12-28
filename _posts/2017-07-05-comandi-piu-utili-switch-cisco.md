---
title: Comandi più usati su Switch Cisco
date: 2017-07-05 15:00:00 +0200
author: Stefano Marzorati
layout: post
image: 'https://marzorati.co/img/cisco.png'
share-img: 'https://marzorati.co/img/cisco.png'
categories:
  - Networks
tags:
  - switch
  - Cisco
  - comandi
  - utili
  - vlan
  - porte
  - access
  - trunk
---
**Verifica su quale porta è collegato un certo pc o device:**   

	ping *ipaddress*   
	show ip arp *ipaddress*   
	show mac address-table address *mac-address*   

**Trova l'indirizzo IP di un device con un certo mac-address facente parte di una VLAN specifica:**   

	show ip arp vlan 100

**Per assegnare una VLAN su una determinata porta:**   

	conf t   
	interface gig1/0/x   
	switchport access vlan 50   
	end   
	wr memory   


**Per mettere una porta in trunk su piu VLAN:**   

	conf t
	interface gig1/0/x
	switchport mode trunk
	switchport trunk allowed vlan 1,100
	end
	wr memory


**Togliere trunk:**  

	conf t 
	interface gig1/0/x
	switchport mode access
	end
	wr memory


**Per vedere quali porte sono in trunk e su quali VLAN:**   

	show interfaces trunk


**Per vedere lo stato di tutte le porte e la loro descrizione:**   

	show interfaces description


**Per poter configurare una porta a cui sarà collegato uno switch bisogna fare quanto segue:**   

	conf t
	interface gig1/0/<numero porta>
	switchport mode trunk
	no spanning-tree portfast
	shutdown
	no shutdown


**Mentre per configurare una porta dove ci sarà collegato un pc più telefono il commando è quello che segue:**   

	conf t
	interface GigabitEthernet1/0/numero porta
	description *** PC + Voice VLAN ***
	switchport trunk allowed vlan 100
	switchport mode trunk
