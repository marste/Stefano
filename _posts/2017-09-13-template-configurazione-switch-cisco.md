---
layout: post
title: Template di configurazione di uno switch Cisco
date: '2017-09-13 13:00:00 +0200'
author: Stefano Marzorati
image: 'https://farm5.staticflickr.com/4383/36390662603_aa17d0fa81_o.png'
share-img: 'https://farm5.staticflickr.com/4383/36390662603_aa17d0fa81_o.png'
categories:
  - Network
tags:
  - tftp
  - server
  - cisco
  - template
  - commandline
published: true
---
 - Collegare lo switch con il cavo seriale e rispondere di `no` alla richiesta di configurazione iniziale (wizard)
 - Digitare `enable` per entrare nella modalità di configurazione
 - Controllare la versione del firmware, digitando: `show version` e controllare dal sito Cisco se corrisponde all'ultima versione suggerita.
 - Se non fosse l'ultima versione, procedere come segue per aggiornarlo.

***Aggiornamento IOS***

Oltre al collegamento con la seriale, collegarsi anche con un cavo ethernet, impostando al PC l'indirizzo `1.1.1.1` e subnet `255.255.255.252`

	#conf t
	#interface vlan 1
	#ip address 1.1.1.2 255.255.255.252
	#end

Installare un server TFTP <a href="http://tftpd32.jounin.net/tftpd32_download.html" target="_blank">(Tftpd64)</a> locale sul PC per trasferire il firmware sullo switch e metterlo in modalità *PXE Compatibility*

	#archive tar /xtrac tftp://1.1.1.1/c2960x-universalk9-mz.152-2.E6.tar flash:
	#verify /md5 flash:/c2960x-universalk9-mz.152-2.E6/c2960x-universalk9-mz.152-2.E6.bin 

	#conf t
	#boot system flash:/c2960x-universalk9-mz.152-2.E6/c2960x-universalk9-mz.152-2.E6.bin 
	#end

	#write memory

	#show boot
	#reload

***Configurazione Switch***

	# conf t

	service timestamps debug datetime msec
	service timestamps log datetime msec
	service password-encryption
	!
	hostname SW-2960-48p-Primo_Piano
	!
	enable secret password_scelta
	!
	username admin privilege 15 secret password_scelta
	!
	clock timezone GMT 1 0
	clock summer-time OraLegale recurring last Sun Mar 3:00 last Sun Oct 3:00
	!
	ip domain-name dominio.com
	!
	spanning-tree mode rapid-pvst
	spanning-tree portfast bpduguard default
	spanning-tree extend system-id
	!
	interface Vlan1
	description *** VLAN 1 ***
	ip address 192.168.25.25 255.255.0.0
	!
	ip default-gateway 192.168.10.254
	ip http server
	ip http secure-server
	!
	ip ssh version 2
	!
	!
	!
	!
	line con 0
	login local
	line vty 0 4
	login local
	line vty 5 15
	login local
	!
	ntp server 193.204.114.232 prefer
	ntp server 193.204.114.233
	!
	vtp mode client
	vtp domain Dominio-VTP
	vtp password password_vlt
	!
	end
	!
	wr memory

***Port Configuration***

Per selezionare un tot. di porte sul quale applicare il comando   

	interface range gig1/0/1-2   
	
Per riportare a default la configurazione della porta   

	default interface gig1/0/1


**Porta dedicata a VLAN VOCE**   

	interface GigabitEthernet1/0/1
	description *** Voice VLAN ***
	switchport access vlan 100
	switchport mode access
	spanning-tree portfast


**Porta client + IPPHONE**   

	interface GigabitEthernet1/0/1
	description *** PC + Voice VLAN ***
	switchport trunk allowed vlan 1,100
	switchport mode trunk
	spanning-tree portfast trunk
 
**Porta Uplink**   

	interface GigabitEthernet1/0/49
	switchport mode trunk
	description *** Uplink Interface ***
 
**Porta Access Point**   

	interface GigabitEthernet1/0/49 
	switchport mode trunk
	description *** Access Point Interface ***

**Porta VLAN Dedicata**   

	interface GigabitEthernet1/0/10
	description *** VLAN 50 ***
	switchport access vlan 50
	switchport mode access

**Per disabilitare/abilitare una porta**   

	interface GigabitEthernet1/0/x
	shutdown
	no shutdown
	
**Togliere trunk**   

	interface gig1/0/x
	switchport mode access