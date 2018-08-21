---
title: 'Vmware - No Connection to VR Server: Not Responding'
date: 2018-08-21 10:00:00 +0200
author: Stefano Marzorati
image: 'https://marzorati.co/img/vmware.png'
share-img: 'https://marzorati.co/img/vmware.png'
layout: post
categories:
  - Vmware
tags:
  - vmware
  - connection
  - vr
  - server
  - responding
  - ssh
  - vmreplica
---
  - Per prima cosa abilita il servizio **SSH** sull'host in cui è presente la macchina virtuale che dà quel messaggio di errore.   

  - Poi usando **Putty** ti colleghi in SSH sull'host.   

  - Per ottenere l'ID della macchina virtuale, digita:   

<code>vim-cmd vmsvc/getallvms</code>

  - Trova il VMid della VM con il problema di configurazione e annotati il VMid. Ad esempio, considera che il VMid è 42   

  - Per ottenere lo stato di replica della Macchina Virtuale, esegui il comando:   

<code>vim-cmd hbrsvc/vmreplica.getState 42</code>

  - Per disabilitare la replica VMware sulla macchina virtuale, eseguire il comando:

<code>vim-cmd hbrsvc/vmreplica.disable 42</code>
	
  - Otterrai una cosa simile:   

<code>[root@VMhost:~] vim-cmd hbrsvc/vmreplica.disable 42   
Disable VM Replication:</code>
	
  - Rilancia:

<code>vim-cmd hbrsvc/vmreplica.getState 42</code>

  - Otterrai:

<code>
[root@VMhost:~] vim-cmd hbrsvc/vmreplica.getState 42   
Retrieve VM running replication state:   
(vim.fault.ReplicationVmFault) {   
faultCause = (vmodl.MethodFault) null,   
reason = “notConfigured”,   
state = <unset>,   
instanceId = <unset>,   
vm = ‘vim.VirtualMachine:42’,   
msg = “Received SOAP response fault from [<cs p:1fwaf548, TCP:localhost:80>]: getGroupState   
vSphere Replication operation error: Virtual machine is not configured for replication.”   
}   
</code>