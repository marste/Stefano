---
title: Installare e configurare DKIM con Postfix su Debian
date: 2015-05-06 08:15:00 -07:00
author: Stefano Marzorati
layout: post
permalink: /installare-configurare-dkim-postfix-debian/
categories:
  - Software
tags:
  - installare
  - configurare
  - dkim
  - postfix
  - debian
---
Prima di iniziare l'installazione, un aggiornamento di sistema è consigliato:   

`sudo apt-get update`   
`sudo apt-get dist-upgrade`

Installare OpenDKIM e le sue dipendenze:   

`sudo apt-get install opendkim opendkim-tools`

Cominciamo con il file di configurazione principale:   

`sudo nano /etc/opendkim.conf`

	AutoRestart             Yes
	AutoRestartRate         10/1h
	UMask                   002
	Syslog                  yes
	SyslogSuccess           Yes
	LogWhy                  Yes
	
	Canonicalization        relaxed/simple
	
	ExternalIgnoreList      refile:/etc/opendkim/TrustedHosts
	InternalHosts           refile:/etc/opendkim/TrustedHosts
	KeyTable                refile:/etc/opendkim/KeyTable
	SigningTable            refile:/etc/opendkim/SigningTable
	
	Mode                    sv
	PidFile                 /var/run/opendkim/opendkim.pid
	SignatureAlgorithm      rsa-sha256
	
	UserID                  opendkim:opendkim
	
	Socket                  inet:12301@localhost
	
Collegare milter a Postfix:   

`sudo nano /etc/default/opendkim`   

Aggiungere la seguente riga, modificare il numero di porta solo se se ne utilizza uno personalizzato:   
`SOCKET="inet:12301@localhost"`   

Configurare postfix per usare questo milter:   

`sudo nano /etc/postfix/main.cf`

Assicurarsi che queste due linee sono presenti nel file di configurazione Postfix e non siano commentate:   
	milter_protocol = 2
	milter_default_action = accept	

E' probabile che un filtro (SpamAssasin, Clamav etc.) sia già utilizzato da Postfix; se sono presenti i seguenti parametri, basta aggiungere il milter di opendkim (milters sono separati da una virgola), il numero di porta deve essere lo stesso che c'è nella configurazione `opendkim.conf`:	

	smtpd_milters = unix:/spamass/spamass.sock, inet:localhost:12301
	non_smtpd_milters = unix:/spamass/spamass.sock, inet:localhost:12301	
	
Se i parametri sono mancanti, definirli come segue:   

	smtpd_milters = inet:localhost:12301
	non_smtpd_milters = inet:localhost:12301

Creare una struttura di directory che conterrà i TrustedHosts, le KeyTable, SigningTable e keys:	

`sudo mkdir /etc/opendkim`
`sudo mkdir /etc/opendkim/keys`   

Specificare gli host attendibili:   

`sudo nano /etc/opendkim/TrustedHosts`

	127.0.0.1
	localhost
	192.168.0.1/24
	
	*.example.com
	
	#*.example.net
	#*.example.org   
	
Crea una key table:   
`sudo nano /etc/opendkim/KeyTable`	

Esempio:   

`mail._domainkey.example.com example.com:mail:/etc/opendkim/keys/example.com/mail.private`

Crea una signing table:   

`sudo nano /etc/opendkim/SigningTable`   

Esempio:   

`*@example.com mail._domainkey.example.com`

Vai in:   

`cd /etc/opendkim/keys`

	sudo mkdir example.com
	cd example.com

Genera le chiavi:   
	
`sudo opendkim-genkey -s mail -d example.com`   

Cambia il proprietario:   
`sudo chown opendkim:opendkim mail.private`   

Apri mail.txt:   
`sudo nano -$ mail.txt`   

La chiave pubblica viene definita sotto il parametro p. Non utilizzare quella riportata di seguito, è solo un esempio e non funziona su server.   

	`mail._domainkey IN TXT "v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC5N3lnvvrYgPCRSoqn+awTpE+iGYcKBPpo8HHbcFfCIIV10Hwo4PhCoGZSaKVHOjDm4yefKXhQjM7iKzEPuBatE7O47hAx1CJpNuIdLxhILSbEmbMxJrJAG0HZVn8z6EAoOHZNaPHmK2h4UUrjOG8zA5BHfzJf7tGwI+K619fFUwIDAQAB" ; ----- DKIM key mail for example.com`

Copiare la chiave e aggiungere un record TXT alle voci DNS del dominio:   

	Name: mail._domainkey.example.com.
	Text: "v=DKIM1; k=rsa; p=MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQC5N3lnvvrYgPCRSoqn+awTpE+iGYcKBPpo8HHbcFfCIIV10Hwo4PhCoGZSaKVHOjDm4yefKXhQjM7iKzEPuBatE7O47hAx1CJpNuIdLxhILSbEmbMxJrJAG0HZVn8z6EAoOHZNaPHmK2h4UUrjOG8zA5BHfzJf7tGwI+K619fFUwIDAQAB"	

Riavvia:   
	
`sudo service postfix restart`   
`sudo service opendkim restart`

La configurazione può essere testato con l'invio di una e-mail vuota a <check-auth@verifier.port25.com> e nella risposta verrà ricevuto il risultato.

*[https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-dkim-with-postfix-on-debian-wheezy](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-dkim-with-postfix-on-debian-wheezy)*
