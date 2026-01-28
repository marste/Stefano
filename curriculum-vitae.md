---
layout: page
title: Curriculum Vitae
permalink: /curriculum-vitae/
image: 'https://marzorati.co/img/cv.png'
share-img: 'https://marzorati.co/img/cv.png'
---

    
    <style>
        :root {
            --primary-color: #2563eb;
            --primary-light: #dbeafe;
            --bg-color: #f8fafc;
            --line-color: #e2e8f0;
            --card-bg: #ffffff;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --border-default: #e2e8f0;
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-main);
            line-height: 1.6;
            margin: 0;
            padding: 60px 20px;
        }

        .container { max-width: 800px; margin: 0 auto; }

        header { text-align: center; margin-bottom: 70px; }
        h1 { margin: 0; font-size: 2.8rem; font-weight: 800; letter-spacing: -0.02em; }
        .contact-bar { color: var(--text-muted); margin-top: 15px; font-weight: 400; }

        /* Timeline */
        .timeline {
            position: relative;
            padding-left: 40px;
        }

        .timeline::before {
            content: '';
            position: absolute;
            left: 0; top: 0; bottom: 0;
            width: 3px;
            background: var(--line-color);
        }

        .timeline-date-label {
            position: relative;
            font-weight: 700;
            color: var(--primary-color);
            font-size: 0.85rem;
            margin-bottom: 15px;
            display: inline-block;
            background: var(--primary-light);
            padding: 4px 14px;
            border-radius: 20px;
            text-transform: uppercase;
        }

        .timeline-date-label::before {
            content: '';
            position: absolute;
            left: -46px;
            top: 50%;
            transform: translateY(-50%);
            width: 12px;
            height: 12px;
            background: var(--bg-color);
            border: 3px solid var(--primary-color);
            border-radius: 50%;
            z-index: 2;
        }

        /* Card con bordo dinamico */
        .card {
            background: var(--card-bg);
            border: 1px solid var(--border-default);
            border-radius: 12px;
            padding: 30px;
            margin-bottom: 50px;
            position: relative;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease-in-out;
        }

        .card:hover {
            transform: translateY(-5px);
            border-color: var(--primary-color);
            box-shadow: 0 12px 20px -5px rgba(37, 99, 235, 0.15);
        }

        .role { font-size: 1.75rem; font-weight: 800; color: var(--text-main); margin: 0; }
        
        /* Stile Azienda e Descrizione */
        .company-name { font-size: 1.2rem; color: var(--primary-color); font-weight: 600; margin-top: 5px; display: block; }
        .company-name a { color: inherit; text-decoration: none; }
        .company-desc { font-size: 0.9rem; color: var(--text-muted); font-weight: 400; display: block; margin-top: 2px; font-style: italic; }

        .cv-section { margin-top: 25px; }
        .cv-section-title { 
            display: block;
            font-weight: 700; 
            text-transform: uppercase; 
            font-size: 0.75rem; 
            color: var(--text-muted); 
            letter-spacing: 0.05em;
            margin-bottom: 12px;
            border-bottom: 1px solid #f1f5f9;
        }

        /* Formattazione Testo Attività */
        .cv-text {
            font-size: 0.95rem;
            text-align: justify;
            color: #334155;
            margin-bottom: 0;
        }
        .cv-text b { color: var(--text-main); }

        .skill-container {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-top: 10px;
        }

        .skill-tag {
            background: #f8fafc;
            border: 1px solid var(--border-default);
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.8rem;
            color: var(--text-main);
            transition: background 0.2s;
        }

        .card:hover .skill-tag { background: #ffffff; border-color: var(--primary-light); }

        @media (max-width: 600px) {
            .role { font-size: 1.4rem; }
            .timeline { padding-left: 30px; }
            .timeline-date-label::before { left: -36px; }
        }
    </style>

<body>

<div class="container">
    

    <div class="timeline">

        <span class="timeline-date-label">07/2023 – OGGI</span>
        <div class="card">
            <h2 class="role">IT Manager</h2>
            <span class="company-name"><b><a href="http://www.alfavarese.it/" target="_blank">ALFA S.r.l.</a></b></span>
            <span class="company-desc">Società pubblica costituita nel giugno 2015 che gestisce il Servizio Idrico Integrato della Provincia di Varese.</span>
            
            <div class="cv-section">
                <span class="cv-section-title">Principali competenze ed attività trasversali</span>
                <div class="cv-text">
                    <p>Nel corso della mia esperienza, mi sono occupato di <b>migliorare i processi aziendali</b> attraverso l'implementazione di strategie mirate, che hanno permesso di ridurre le inefficienze e aumentare significativamente la produttività del team.
				<p>Ho avuto la <b>responsabilità completa della gestione delle infrastrutture IT</b>, assicurando la massima continuità operativa e guidando il costante aggiornamento tecnologico. In questo contesto, ho sviluppato e gestito <b>ambienti virtualizzati</b> per ottimizzare l'utilizzo delle risorse hardware, migliorando così la scalabilità e la flessibilità dell'intero ecosistema IT.</p>
				<p>Un aspetto a cui ho sempre dedicato grande attenzione è la <b>cybersecurity</b>. Ho implementato soluzioni di sicurezza per proteggere i dati aziendali, concentrandomi sia sulla prevenzione proattiva delle minacce che sulla gestione delle vulnerabilità.</p>
				<p>Ho guidato con successo un <b>team IT multidisciplinare</b>, promuovendo una cultura di forte collaborazione e crescita professionale. La mia attività ha incluso la <b>gestione dell'infrastruttura di rete</b>, garantendo una connettività sicura e affidabile tra tutti i siti aziendali.</p>
				<p>Nel quotidiano, ho applicato le mie capacità di <b>problem solving</b> per risolvere situazioni complesse legate all'infrastruttura e ai processi, assicurando sempre il ripristino rapido delle operazioni critiche. Queste competenze sono state fondamentali anche nella <b>gestione di progetti IT</b> end-to-end, che ho portato a termine rispettando tempi, budget e obiettivi, con un costante focus sulla qualità e sulla soddisfazione degli stakeholder.</p>
				<p>A livello di pianificazione, ho <b>collaborato con vari dipartimenti</b> per anticipare le esigenze future, gestire il rifornimento e garantire la continuità operativa. Sul fronte economico e contrattuale, ho <b>gestito e negoziato contratti</b> con fornitori e partner, ottenendo condizioni vantaggiose, e mi sono occupato della <b>stesura e del monitoraggio del budget IT</b>, assicurando un uso efficiente delle risorse. Queste attività sono parte integrante di un più ampio lavoro di <b>pianificazione strategica, definizione del budget e previsioni</b> per il dipartimento IT, che sviluppo in allineamento con gli obiettivi aziendali a lungo termine.</p>
                </div>
            </div>

            <div class="cv-section">
                <span class="cv-section-title">Tech Stack</span>
                <div class="skill-container">
                    <span class="skill-tag">Cybersecurity</span>
                    <span class="skill-tag">Infrastructure</span>
                    <span class="skill-tag">Budget Management</span>
                </div>
            </div>
        </div>

        <span class="timeline-date-label">05/2015 – 07/2023</span>
        <div class="card">
            <h2 class="role">IT Manager</h2>
            <span class="company-name"><b><a href="http://www.siitgroup.com/" target="_blank">S.I.I.T. S.r.l.</a></b></span>
            <span class="company-desc">Azienda leader partner per lo sviluppo e produzione di specialità medicinali e integratori alimentari.</span>
            
            <div class="cv-section">
                <span class="cv-section-title">Principali competenze ed attività tecniche</span>
                <div class="cv-text">
                    <p>
<li>Gestione di tutto l'apparato ICT</li>
<li>Gestione della sicurezza degli accessi interni ed esterni alle risorse ICT</li>
<li>Gestione della sicurezza degli accessi interni ed esterni dei vari plant industriali</li>
<li>Interfaccia sia con gli utenti interni che con consulenti esterni per quanto riguarda il monitoring dei sistemi e l'indirizzo di problematiche che potessero insorgere</li>
<li>Amministrazione delle utenze in linea con le politiche di accesso vigenti in azienda</li>
<li>Attività di ottimizzazione dei processi informatici aziendali</li>
<li>Analisi di nuove problematiche o nuovi progetti</li>
<li>Creazione e manutenzione di procedure ICT</li>
<li>Gestione e organizzazione dei database aziendali</li>
<li>Monitoraggio data recovery e prevenzione problematiche legate alla security IT</li>
<li>Coordinamento progetti</li>
<li>Monitoraggio giornaliero dei logs dei sistemi di produzione</li>
<li>Aggiornamento inventario degli assets gestiti</li>
</p>
                </div>
            </div>

            <div class="cv-section">
                <span class="cv-section-title">Installazione & Manutenzione</span>
                <div class="skill-container">
                    <span class="skill-tag">MS Windows Client e Servers</span>
                    <span class="skill-tag">Firewall Sonicwall Dell</span>
                    <span class="skill-tag">Firewall Cisco Firepower</span>
					<span class="skill-tag">Switch Cisco</span>
					<span class="skill-tag">Sistemi di virtualizzazione: ESX, VMware Server</span>
					<span class="skill-tag">Office 365 - Exchange Online - Sharepoint</span>
					<span class="skill-tag">Web servers (Linux, Apache, Mysql, PHP)</span>
					<span class="skill-tag">IBM iSeries</span>
					<span class="skill-tag">Microsoft SQL</span>
					<span class="skill-tag">Cisco VPN</span>
					<span class="skill-tag">Sistemi di sicurezza Sophos XDR</span>
					<span class="skill-tag">CyberSecurity Cynet</span>
					<span class="skill-tag">Telefonia VOIP Selta</span>
					<span class="skill-tag">Telefonia DECT Spectralink</span>
					<span class="skill-tag">Data Logger a radiofrequenza</span>
					<span class="skill-tag">Lettori Barcode</span>
					<span class="skill-tag">Controllo accessi</span>
					
					<div class="cv-section">
                <span class="cv-section-title">Principali competenze ed attività trasversali</span>
                <div class="cv-text">
                    <p>
<li>Assicurare l'informatizzazione della Società, nel rispetto di priorità e linee guida assegnate dalla Direzione, contribuendo alla definizione di politiche, budget, piano di investimenti/​costi di funzione</li>
<li>Garantire la continuità dei servizi erogati, la sicurezza e l'armonia delle varie strutture hardware/​software</li>
<li>Garantire la corretta gestione della rete aziendale, del server e delle reti informatiche sia dell'Area Amministrativa sia delle funzioni connesse al business dello stabilimento (Produzione, Supply Chain, Qualità, etc.)</li>
<li>Coordinare la progettazione e l'implementazione dei nuovi servizi, con l'obiettivo di assicurare la piena integrazione con i servizi già presenti</li>
<li>Assicurare l’ottimizzazione dei processi informativi, curandone l’aggiornamento e lo sviluppo nel rispetto della legge sulla Privacy ed in coerenza con l’adeguatezza delle soluzioni alle esigenze aziendali in termini sia di rapporto costi/​benefici sia di standard qualitativi</li>
<li>Curare la creazione, ​l’aggiornamento, ​la manutenzione di sistemi applicativi diretti a funzioni specifiche nel rispetto delle priorità e linee guida date, in coerenza con il sistema generale</li>
<li>Assicurare un livello di servizio e processi informativi ottimale al costo minimale</li>
<li>Garantire la costante funzionalità della rete di comunicazione direttamente e/​o con il supporto della sua struttura, in particolare dell’help-desk</li>
<li>Assicurare la valutazione di nuovi prodotti, l’ordine e l’installazione di nuove apparecchiature e garantirne il corretto funzionamento tra di loro</li>
<li>Garantire la formazione iniziale dell’utenza e la sua costante assistenza</li>
<li>Supportare l’utenza aziendale nell’individuazione dei fabbisogni e provvedere alla verifica di congruenza delle soluzioni identificate con quelle esistenti, tenendo conto dei trend tecnologici</li>
<li>Partecipare alle trattative economiche con i fornitori con i quali mantenere costanti rapporti per recepire informazioni in merito ai trend tecnologici.</li>  
</p>
                </div>
            </div>
</div>
</div>
</div>






        <span class="timeline-date-label">01/2007 – 05/2015</span>
        <div class="card">
            <h2 class="role">ICT System Administrator</h2>
            <span class="company-name"><b><a href="http://www.edisport.it/" target="_blank">Edisport Editoriale S.p.A.</a></b></span>
            <span class="company-desc">Casa Editrice nata nel 1914 con la fondazione della rivista "Motociclismo"</span>






   <div class="cv-section">
                <span class="cv-section-title">Principali competenze ed attività tecniche</span>
                <div class="cv-text">
                    <p>
<li>Gestione di tutto l'apparato ICT</li>
<li>Gestione della sicurezza degli accessi interni ed esterni alle risorse ICT</li>
<li>Interfaccia sia con gli utenti interni che con consulenti esterni per quanto riguarda il monitoring dei sistemi e l'indirizzo di problematiche che potessero insorgere</li>
<li>Amministrazione delle utenze in linea con le politiche di accesso vigenti in azienda</li>
<li>Attività di ottimizzazione dei processi informatici aziendali</li>
<li>Analisi di nuove problematiche o nuovi progetti</li>
<li>Creazione e manutenzione di procedure ICT</li>
<li>Progettazione struttura dati e reports della Business intelligence</li>
<li>Gestione e organizzazione dei database aziendali</li>
<li>Monitoraggio data recovery e prevenzione problematiche legate alla security IT</li>
<li>Coordinamento progetti</li>
<li>Monitoraggio giornaliero dei logs dei sistemi di produzione</li>
<li>Aggiornamento inventario degli assets gestiti</li>
</p>
                </div>
            </div>
			
			
			
			
			
			
			
			
			<div class="cv-section">
                <span class="cv-section-title">Installazione & Manutenzione</span>
                <div class="skill-container">
                    
<span class="skill-tag">MS Windows Client e Servers</span>
<span class="skill-tag">Web Servers Linux (Centos – Debian - Ubuntu)</span>
<span class="skill-tag">Firewall e Proxy Linux</span>
<span class="skill-tag">Sistemi di virtualizzazione: ESX, VMware Server</span>
<span class="skill-tag">Web servers (Linux, Apache, Mysql, PHP)</span>
<span class="skill-tag">Blade Servers IBM</span>
<span class="skill-tag">IBM AS/400</span>
<span class="skill-tag">Sistemi Editoriali (Adobe, Woodwing)</span>
<span class="skill-tag">IBM Lotus Domino</span>
<span class="skill-tag">Microsoft Exchange</span>
<span class="skill-tag">VPN (OpenVPN)</span>
<span class="skill-tag">Server FTP</span>
<span class="skill-tag">Appliance Symantec Antivirus-Antispam</span>
<span class="skill-tag">Barracuda Spam & Virus Firewall</span>
<span class="skill-tag">Telefonia VOIP Cisco</span>
<span class="skill-tag">Appliance NAS NetApp</span>
<span class="skill-tag">Barracuda Message Archiver</span>
<span class="skill-tag">Door & Security Intercoms</span>
					
					<div class="cv-section">
                <span class="cv-section-title">Principali competenze ed attività trasversali</span>
                <div class="cv-text">
                    <p>
<li>Coordinamento dell'attività di sviluppatori esterni e sistemisti</li>
<li>Attività di testing, improvement e reportistica sui progetti affrontati e sui risultati raggiunti</li>
<li>Progettazione e/o valutazione d'acquisto di hardware e software sulla base delle esigenze operative, delle dimensioni del progetto e del budget disponibile</li>
<li>Riduzione dell'incidenza dei costi di progetti IT e relativi alla telefonia</li>
<li>Superamento di piattaforme divenute obsolete per la gestione dei databases e web</li>
<li>Interfaccia continua con ogni livello di utenza aziendale ed esposizione diretta al management team</li>
<li>Delineare la strategia ICT di medio e lungo periodo</li>
<li>Gestione delle criticità</li>
<li>Pianificazione progettazione e gestione di attività di manutenzione proattivita di reti e servers</li>
</p>
                </div>
            </div>
</div>
</div>
</div>
			
			
			
			
			  <span class="timeline-date-label">12/2004 – 01/2007</span>
        <div class="card">
            <h2 class="role">IT Senior Consultant</h2>
            <span class="company-name"><b>IRPE S.p.A.</b></span>
            <span class="company-desc">Azienda ICT per la fornitura di servizi di outsourcing, consulenza, progettazione e gestione di architetture, applicazioni e sicurezza</span>
			
			
			
			
			
			<div class="cv-section">
                <span class="cv-section-title">Principali competenze ed attività tecniche</span>
                <div class="cv-text">
                    <p>Sistemista di rete specializzato nell’installazione ed amministrazione di n° 9 servers Lotus Domino in cluster con funzione di <b>mail server</b> e <b>application server</b> per un bacino di 5000 utenze, presso: Carrefour Italia S.p.A.</p>
<p>Collaborazione costante con fornitori software e con i servizi interni di Carrefour S.p.A. (personale italiano ed estero)</p>
<p>Gestione di un server Lotus Domino dedicato al BlackBerry Enterprise per garantire connettività wireless e la connettività della dirigenza</p>
<p>Amministrazione delle piattaforme Microsoft per la gestione dei domini, file server, software distribution e gestione backup.</p>
<p>Gestione intranet di gruppo e parte dei siti internet pubblicandone i contenuti in accordo con la divisione marketing e le società esterne
</p>
                </div>
            </div>
			
			
			</div>
			
			
			
					  <span class="timeline-date-label">02/2004 – 12/2004</span>
        <div class="card">
            <h2 class="role">IT Senior Consultant</h2>
            <span class="company-name"><b><a href="http://www.wiit.it/" target="_blank">WIIT S.p.A.</a></b></span>
            <span class="company-desc">Azienda ICT per la fornitura di servizi di outsourcing</span>
			
			
			
<div class="cv-section">
                <span class="cv-section-title">Principali competenze ed attività tecniche</span>
                <div class="cv-text">
                    <p>Sistemista di rete specializzato nell’installazione, amministrazione e presidio di servers Lotus Domino presso: Mediaset, Medusa Film e Alcantara con reperibilità 24h.</p>

                </div>
            </div>
			
			
			</div>










  <span class="timeline-date-label">04/2000 – 02/2004</span>
        <div class="card">
            <h2 class="role">IT Consultant</h2>
            <span class="company-name"><b><a href="https://www.soldionline.it/notizie/azioni-italia/tc-sistema-arriva-il-fallimento" target="_blank">TC Sistema S.p.A.</a></b></span>
            <span class="company-desc">Azienda ICT per la fornitura di servizi di outsourcing, consulenza, progettazione e gestione di architetture, applicazioni e sicurezza</span>
			
			
			
<div class="cv-section">
                <span class="cv-section-title">Principali competenze ed attività tecniche</span>
                <div class="cv-text">
                    <p>Sistemista di rete specializzato nell’installazione ed amministrazione di server Lotus Domino.</p>
<p>Docente di corsi Lotus Domino Administrator</p>
<p>Installazione ed amministrazione di ambienti Microsoft.</p>

                </div>
            </div>
			
			
			</div>












 <span class="timeline-date-label">09/1997 – 04/2000</span>
        <div class="card">
            <h2 class="role">Hardware Engineer</h2>
            <span class="company-name"><b><a href="https://www.soldionline.it/notizie/azioni-italia/tc-sistema-arriva-il-fallimento" target="_blank">TC Sistema S.p.A.</a></b></span>
            <span class="company-desc">Azienda ICT per la fornitura di servizi di outsourcing, consulenza, progettazione e gestione di architetture, applicazioni e sicurezza</span>
			
			
			
<div class="cv-section">
                <span class="cv-section-title">Principali competenze ed attività tecniche</span>
                <div class="cv-text">
                    <p>Tecnico Hardware specializzato in installazione, riparazione e manutenzione di PC, stampanti locali o di rete, servers (tecnico interno esterno presso clienti)</p>


                </div>
            </div>
			
			
			</div>

























					
					
                
            
       

        </div>


</body>



<center>
<a href="https://marzorati.co/contact/" class="btn btn-primary btn-lg" role="button">Contattami</a>
</center>
