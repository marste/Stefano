---
layout: page
title: Curriculum Vitae
permalink: /curriculum-vitae/
image: 'https://marzorati.co/img/cv.png'
share-img: 'https://marzorati.co/img/cv.png'
published: true
---

<!-- Ionicons -->
<link href="https://unpkg.com/ionicons@4.2.2/dist/css/ionicons.min.css" rel="stylesheet">
<!-- JetBrains Mono - solo per date, etichette e dati tecnici -->
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">

<style>
  .cv-resume {
    --ink: #0f172a;
    --muted: #64748b;
    --faint: #94a3b8;
    --accent: #2563eb;
    --hairline: #e2e8f0;
    --bg: #ffffff;

    max-width: 720px;
    margin: 0 auto;
    padding: 60px 24px 80px;
    font-family: 'Montserrat', sans-serif;
    color: var(--ink);
    line-height: 1.65;
    background: var(--bg);
  }

  .cv-resume .mono {
    font-family: 'JetBrains Mono', ui-monospace, monospace;
  }

  .cv-resume a {
    color: inherit;
  }

  .cv-resume :focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 3px;
  }

  /* ---------- Hero ---------- */

  .cv-hero {
    margin-bottom: 64px;
  }

  .cv-eyebrow {
    display: block;
    font-size: 12px;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--faint);
    margin-bottom: 14px;
  }

  .cv-hero h1 {
    margin: 0 0 10px 0;
    font-size: 2.1em;
    font-weight: 800;
    letter-spacing: -0.02em;
    color: var(--ink);
  }

  .cv-hero p {
    margin: 0;
    color: var(--muted);
    max-width: 46ch;
  }

  /* ---------- Section eyebrow (shared) ---------- */

  .cv-section-eyebrow {
    display: flex;
    align-items: center;
    gap: 8px;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--faint);
    margin-bottom: 28px;
  }

  .cv-section-eyebrow .ion {
    font-size: 14px;
  }

  .cv-skills,
  .cv-experience {
    margin-bottom: 64px;
  }

  /* ---------- Skills (bar list) ---------- */

  .skill-row {
    display: grid;
    grid-template-columns: 200px 1fr 46px;
    align-items: center;
    gap: 18px;
    padding: 11px 0;
  }

  .skill-name {
    font-size: 14px;
    font-weight: 600;
    color: var(--ink);
  }

  .skill-track {
    height: 3px;
    background: var(--hairline);
    border-radius: 2px;
    overflow: hidden;
  }

  .skill-fill {
    height: 100%;
    width: 0%;
    background: var(--accent);
    transition: width 1s cubic-bezier(0.16, 1, 0.3, 1);
  }

  .skill-value {
    font-size: 12px;
    color: var(--muted);
    text-align: right;
    font-variant-numeric: tabular-nums;
  }

  @media (max-width: 560px) {
    .skill-row {
      grid-template-columns: 1fr 40px;
      grid-template-areas:
        "name value"
        "bar bar";
      row-gap: 6px;
    }
    .skill-name { grid-area: name; }
    .skill-value { grid-area: value; }
    .skill-track { grid-area: bar; }
  }

  /* ---------- Experience (log style) ---------- */

  .entry {
    display: grid;
    grid-template-columns: 128px 1fr;
    gap: 32px;
    padding: 36px 0;
    border-top: 1px solid var(--hairline);
  }

  .entry:first-of-type {
    border-top: 1px solid var(--hairline);
  }

  .entry-date {
    display: flex;
	font-size: 14px;
    flex-direction: column;
    gap: 2px;
    color: var(--faint);
    line-height: 1.6;
    padding-top: 2px;
  }

  .entry-date span {
    display: block;
  }

  .entry-role {
    margin: 0 0 8px 0;
    font-weight: 800;
	text-align: left;
    color: var(--ink);
  }

  .entry-company {
    font-weight: 600;
    color: var(--accent);
    margin-bottom: 8px;
  }

  .entry-company a {
    text-decoration: none;
  }

  .entry-company a:hover {
    text-decoration: underline;
  }

  .entry-desc {
    font-style: italic;
    color: var(--muted);
    margin: 0 0 18px 0;
  }

  .entry-text p {
    margin: 0 0 12px 0;
    color: #334155;
    text-align: justify;
  }

  .entry-text p:last-child {
    margin-bottom: 0;
  }

  .entry-text b {
    color: var(--ink);
    font-weight: 700;
  }

  .entry-block {
    margin-top: 20px;
  }

  .entry-block-title {
    display: block;
    font-size: 15px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--faint);
    margin-bottom: 10px;
  }

  .entry-list {
    margin: 0;
    padding-left: 18px;
    color: #334155;
  }

  .entry-list li {
    margin-bottom: 6px;
  }

  .entry-stack {
    font-size: 14px;
    color: var(--muted);
    line-height: 1.9;
  }

  @media (max-width: 640px) {
    .entry {
      grid-template-columns: 1fr;
      gap: 18px;
    }

    .entry-date {
      flex-direction: row;
      flex-wrap: wrap;
      gap: 6px;
      padding-top: 0;
      margin-bottom: 4px;
    }

    .entry-date span {
      display: inline;
    }

    .entry-body {
      display: block;
    }

    .entry-role {
      margin-top: 2px;
    }
  }

  /* ---------- CTA ---------- */

  .cv-cta {
    text-align: center;
    margin-top: 56px;
  }

  .cv-cta a {
    display: inline-block;
    padding: 13px 32px;
    font-size: 14px;
    font-weight: 600;
    color: var(--ink);
    border: 1px solid var(--hairline);
    border-radius: 4px;
    text-decoration: none;
    transition: border-color 0.2s, color 0.2s;
  }

  .cv-cta a:hover {
    border-color: var(--accent);
    color: var(--accent);
  }
</style>

<div class="cv-resume">

  <!-- ---------- Hero ---------- -->
 

  <!-- ---------- Skills ---------- -->
  <div class="cv-skills">
    <div class="cv-section-eyebrow"><i class="ion ion-ios-desktop"></i> Competenze</div>

    <div class="skills-list">
      <div class="skill-row" data-percent="97">
        <span class="skill-name">IT Leadership & Management</span>
        <div class="skill-track"><div class="skill-fill"></div></div>
        <span class="skill-value mono">97%</span>
      </div>
      <div class="skill-row" data-percent="96">
        <span class="skill-name">Infrastructure & Cloud</span>
        <div class="skill-track"><div class="skill-fill"></div></div>
        <span class="skill-value mono">96%</span>
      </div>
      <div class="skill-row" data-percent="95">
        <span class="skill-name">Cybersecurity & Networking</span>
        <div class="skill-track"><div class="skill-fill"></div></div>
        <span class="skill-value mono">95%</span>
      </div>
      <div class="skill-row" data-percent="94">
        <span class="skill-name">Project Management</span>
        <div class="skill-track"><div class="skill-fill"></div></div>
        <span class="skill-value mono">94%</span>
      </div>
      <div class="skill-row" data-percent="93">
        <span class="skill-name">Microsoft Technologies</span>
        <div class="skill-track"><div class="skill-fill"></div></div>
        <span class="skill-value mono">93%</span>
      </div>
      <div class="skill-row" data-percent="98">
        <span class="skill-name">Problem Solving & Innovation</span>
        <div class="skill-track"><div class="skill-fill"></div></div>
        <span class="skill-value mono">98%</span>
      </div>
    </div>
  </div>

  <!-- ---------- Experience ---------- -->
  <div class="cv-experience">
    <div class="cv-section-eyebrow"><i class="ion ion-ios-briefcase"></i> Esperienza</div>

    <!-- ALFA -->
    <div class="entry">
      <div class="entry-date mono"><span class="date-from">07/2023</span><span class="date-to">→ oggi</span></div>
      <div class="entry-body">
        <h3 class="entry-role">IT Manager</h3>
        <div class="entry-company"><a href="http://www.alfavarese.it/" target="_blank" rel="noopener">ALFA S.r.l.</a></div>
        <div class="entry-desc">Società pubblica costituita nel giugno 2015 che gestisce il Servizio Idrico Integrato della Provincia di Varese.</div>

        <div class="entry-text">
          <p>Nel corso della mia esperienza, mi sono occupato di <b>migliorare i processi aziendali</b> attraverso l'implementazione di strategie mirate, che hanno permesso di ridurre le inefficienze e aumentare significativamente la produttività del team.</p>
          <p>Ho avuto la <b>responsabilità completa della gestione delle infrastrutture IT</b>, assicurando la massima continuità operativa e guidando il costante aggiornamento tecnologico. In questo contesto, ho sviluppato e gestito <b>ambienti virtualizzati</b> per ottimizzare l'utilizzo delle risorse hardware, migliorando così la scalabilità e la flessibilità dell'intero ecosistema IT.</p>
          <p>Un aspetto a cui ho sempre dedicato grande attenzione è la <b>cybersecurity</b>. Ho implementato soluzioni di sicurezza per proteggere i dati aziendali, concentrandomi sia sulla prevenzione proattiva delle minacce che sulla gestione delle vulnerabilità.</p>
          <p>Ho guidato con successo un <b>team IT multidisciplinare</b>, promuovendo una cultura di forte collaborazione e crescita professionale. La mia attività ha incluso la <b>gestione dell'infrastruttura di rete</b>, garantendo una connettività sicura e affidabile tra tutti i siti aziendali.</p>
          <p>Nel quotidiano, ho applicato le mie capacità di <b>problem solving</b> per risolvere situazioni complesse legate all'infrastruttura e ai processi, assicurando sempre il ripristino rapido delle operazioni critiche. Queste competenze sono state fondamentali anche nella <b>gestione di progetti IT</b> end-to-end, che ho portato a termine rispettando tempi, budget e obiettivi, con un costante focus sulla qualità e sulla soddisfazione degli stakeholder.</p>
          <p>A livello di pianificazione, ho <b>collaborato con vari dipartimenti</b> per anticipare le esigenze future, gestire il rifornimento e garantire la continuità operativa. Sul fronte economico e contrattuale, ho <b>gestito e negoziato contratti</b> con fornitori e partner, ottenendo condizioni vantaggiose, e mi sono occupato della <b>stesura e del monitoraggio del budget IT</b>, assicurando un uso efficiente delle risorse. Queste attività sono parte integrante di un più ampio lavoro di <b>pianificazione strategica</b> e definizione di budget e previsioni per il dipartimento IT.</p>
        </div>

        <div class="entry-block">
          <span class="entry-block-title mono">Tech Stack</span>
          <div class="entry-stack mono">Cybersecurity · Infrastructure · Budget Management</div>
        </div>
      </div>
    </div>

    <!-- SIIT -->
    <div class="entry">
      <div class="entry-date mono"><span class="date-from">05/2015</span><span class="date-to">→ 07/2023</span></div>
      <div class="entry-body">
        <h3 class="entry-role">IT Manager</h3>
        <div class="entry-company"><a href="http://www.siitgroup.com/" target="_blank" rel="noopener">S.I.I.T. S.r.l.</a></div>
        <div class="entry-desc">Azienda leader partner per lo sviluppo e produzione di specialità medicinali e integratori alimentari.</div>

        <div class="entry-block">
          <span class="entry-block-title mono">Attività tecniche</span>
          <ul class="entry-list">
            <li>Gestione di tutto l'apparato ICT</li>
            <li>Gestione della sicurezza degli accessi interni ed esterni alle risorse ICT</li>
            <li>Gestione della sicurezza degli accessi interni ed esterni dei vari plant industriali</li>
            <li>Interfaccia con utenti interni e consulenti esterni per monitoring e gestione problematiche</li>
            <li>Amministrazione delle utenze in linea con le politiche di accesso vigenti</li>
            <li>Ottimizzazione dei processi informatici aziendali</li>
            <li>Analisi di nuove problematiche o nuovi progetti</li>
            <li>Creazione e manutenzione di procedure ICT</li>
            <li>Gestione e organizzazione dei database aziendali</li>
            <li>Monitoraggio data recovery e prevenzione problematiche legate alla security IT</li>
            <li>Coordinamento progetti</li>
            <li>Monitoraggio giornaliero dei logs dei sistemi di produzione</li>
            <li>Aggiornamento inventario degli assets gestiti</li>
          </ul>
        </div>

        
        <div class="entry-block">
          <span class="entry-block-title mono">Attività trasversali</span>
          <ul class="entry-list">
            <li>Definizione di politiche ICT, budget e piani di investimento/costi di funzione</li>
            <li>Continuità dei servizi erogati, sicurezza e armonia delle strutture hardware/software</li>
            <li>Gestione rete aziendale e infrastruttura server per area amministrativa e funzioni business</li>
            <li>Coordinamento progettazione e implementazione nuovi servizi, integrandoli con quelli esistenti</li>
            <li>Ottimizzazione processi informativi e compliance Privacy</li>
            <li>Creazione, aggiornamento e manutenzione di sistemi applicativi</li>
            <li>Ottimizzazione livello di servizio al costo minimale</li>
            <li>Gestione help-desk e supporto alla struttura interna</li>
            <li>Valutazione, ordine e installazione nuove apparecchiature e integrazione</li>
            <li>Formazione iniziale e assistenza continua agli utenti</li>
            <li>Supporto ai fabbisogni e valutazione congruenza soluzioni con trend tecnologici</li>
            <li>Partecipazione alle trattative economiche con i fornitori</li>
          </ul>
        </div>
	
		<div class="entry-block">
          <span class="entry-block-title mono">Tech Stack</span>
          <div class="entry-stack mono">MS Windows Client e Servers · Firewall Sonicwall Dell · Firewall Cisco Firepower · Switch Cisco · ESX / VMware Server · Office 365 / Exchange Online / SharePoint · Linux / Apache / MySQL / PHP · IBM iSeries · Microsoft SQL · Cisco VPN · Sophos XDR · Cynet Cybersecurity · Telefonia VOIP Selta · Telefonia DECT Spectralink · Data Logger RF · Lettori Barcode · Controllo accessi</div>
        </div>	
	</div>
    </div>

    <!-- EDISPORT -->
    <div class="entry">
      <div class="entry-date mono"><span class="date-from">01/2007</span><span class="date-to">→ 05/2015</span></div>
      <div class="entry-body">
        <h3 class="entry-role">ICT System Administrator</h3>
        <div class="entry-company"><a href="http://www.edisport.it/" target="_blank" rel="noopener">Edisport Editoriale S.p.A.</a></div>
        <div class="entry-desc">Casa Editrice nata nel 1914 con la fondazione della rivista "Motociclismo".</div>

        <div class="entry-block">
          <span class="entry-block-title mono">Attività tecniche</span>
          <ul class="entry-list">
            <li>Gestione di tutto l'apparato ICT</li>
            <li>Gestione della sicurezza degli accessi interni ed esterni alle risorse ICT</li>
            <li>Interfaccia con utenti interni e consulenti esterni per monitoring e gestione problematiche</li>
            <li>Amministrazione delle utenze in linea con le politiche di accesso vigenti</li>
            <li>Ottimizzazione dei processi informatici aziendali</li>
            <li>Analisi di nuove problematiche o nuovi progetti</li>
            <li>Creazione e manutenzione di procedure ICT</li>
            <li>Progettazione struttura dati e reportistica Business Intelligence</li>
            <li>Gestione e organizzazione dei database aziendali</li>
            <li>Monitoraggio data recovery e prevenzione problematiche legate alla security IT</li>
            <li>Coordinamento progetti</li>
            <li>Monitoraggio giornaliero dei logs dei sistemi di produzione</li>
            <li>Aggiornamento inventario degli assets gestiti</li>
          </ul>
        </div>

        

        <div class="entry-block">
          <span class="entry-block-title mono">Attività trasversali</span>
          <ul class="entry-list">
            <li>Coordinamento dell'attività di sviluppatori esterni e sistemisti</li>
            <li>Testing, improvement e reportistica sui progetti affrontati e risultati</li>
            <li>Valutazione e acquisto hardware/software in base a esigenze, progetto e budget</li>
            <li>Riduzione dell'incidenza dei costi di progetti IT e telefonia</li>
            <li>Superamento di piattaforme obsolete per database e web</li>
            <li>Interfaccia continua con ogni livello di utenza e management</li>
            <li>Definizione strategia ICT di medio e lungo periodo</li>
            <li>Gestione criticità</li>
            <li>Pianificazione manutenzione proattiva reti e server</li>
          </ul>
        </div>
		
		<div class="entry-block">
          <span class="entry-block-title mono">TECH STACK</span>
          <div class="entry-stack mono">MS Windows Client e Servers · Web Servers Linux (CentOS / Debian / Ubuntu) · Firewall & Proxy Linux · ESX / VMware Server · Apache / MySQL / PHP · Blade Servers IBM · IBM AS/400 · Sistemi Editoriali (Adobe, Woodwing) · IBM Lotus Domino (ora HCL Domino) · Microsoft Exchange · VPN (OpenVPN) · Server FTP · Appliance Symantec Antivirus-Antispam · Barracuda Spam & Virus Firewall · Telefonia VOIP Cisco · Appliance NAS NetApp · Barracuda Message Archiver · Door & Security Intercoms</div>
        </div>
      </div>
    </div>

    <!-- IRPE -->
    <div class="entry">
      <div class="entry-date mono"><span class="date-from">12/2004</span><span class="date-to">→ 01/2007</span></div>
      <div class="entry-body">
        <h3 class="entry-role">IT Senior Consultant</h3>
        <div class="entry-company">IRPE S.p.A.</div>
        <div class="entry-desc">Azienda ICT per la fornitura di servizi di outsourcing, consulenza, progettazione e gestione di architetture, applicazioni e sicurezza.</div>

        <div class="entry-text">
        <p>Sistemista infrastrutturale specializzato nella progettazione, installazione, configurazione e amministrazione di ambienti IBM Lotus Domino (oggi HCL Domino) in architettura cluster, con funzioni di mail server e application server a supporto di circa 5.000 utenti presso Carrefour Italia S.p.A.
		Gestione operativa dell’infrastruttura Domino, garantendo continuità del servizio, monitoraggio, troubleshooting e supporto agli utenti aziendali, in collaborazione con fornitori software e con i team IT interni nazionali e internazionali.
		Amministrazione della piattaforma BlackBerry Enterprise Server integrata con Domino per l’erogazione di servizi di mobilità e connettività wireless a supporto del management aziendale.
		Gestione di ambienti Microsoft enterprise, inclusi servizi di dominio, file server, distribuzione software e sistemi di backup.
		Amministrazione della intranet aziendale di gruppo e gestione operativa di contenuti web, collaborando con le funzioni Marketing e con società esterne per la pubblicazione e l’aggiornamento dei contenuti digitali.
		</p>
        </div>
      </div>
    </div>

    <!-- WIIT -->
    <div class="entry">
      <div class="entry-date mono"><span class="date-from">02/2004</span><span class="date-to">→ 12/2004</span></div>
      <div class="entry-body">
        <h3 class="entry-role">IT Senior Consultant</h3>
        <div class="entry-company"><a href="http://www.wiit.it/" target="_blank" rel="noopener">WIIT S.p.A.</a></div>
        <div class="entry-desc">Azienda ICT per la fornitura di servizi di outsourcing.</div>

        <div class="entry-text">
          <p>Sistemista di rete specializzato nell’installazione, configurazione, amministrazione e gestione operativa di ambienti server IBM Lotus Domino in contesti enterprise. Attività di presidio tecnico, monitoraggio, troubleshooting e supporto infrastrutturale presso importanti realtà aziendali tra cui Mediaset, Medusa Film e Alcantara.</p>
        </div>
      </div>
    </div>

    <!-- TC SISTEMA - IT Consultant -->
    <div class="entry">
      <div class="entry-date mono"><span class="date-from">04/2000</span><span class="date-to">→ 02/2004</span></div>
      <div class="entry-body">
        <h3 class="entry-role">IT Consultant</h3>
        <div class="entry-company"><a href="https://www.soldionline.it/notizie/azioni-italia/tc-sistema-arriva-il-fallimento" target="_blank" rel="noopener">TC Sistema S.p.A.</a></div>
        <div class="entry-desc">Azienda ICT per la fornitura di servizi di outsourcing, consulenza, progettazione e gestione di architetture, applicazioni e sicurezza.</div>

        <div class="entry-text">
          <p>Sistemista infrastrutturale specializzato nella gestione di ambienti server IBM Lotus Domino e Microsoft, con esperienza nell’installazione, configurazione e amministrazione di sistemi enterprise. Attività di docenza su IBM Lotus Domino Administrator e supporto tecnico alla gestione di infrastrutture IT aziendali.</p>
        </div>
      </div>
    </div>

    <!-- TC SISTEMA - Hardware Engineer -->
    <div class="entry">
      <div class="entry-date mono"><span class="date-from">09/1997</span><span class="date-to">→ 04/2000</span></div>
      <div class="entry-body">
        <h3 class="entry-role">Hardware Engineer</h3>
        <div class="entry-company"><a href="https://www.soldionline.it/notizie/azioni-italia/tc-sistema-arriva-il-fallimento" target="_blank" rel="noopener">TC Sistema S.p.A.</a></div>
        <div class="entry-desc">Azienda ICT per la fornitura di servizi di outsourcing, consulenza, progettazione e gestione di architetture, applicazioni e sicurezza.</div>

        <div class="entry-text">
          <p>Tecnico Hardware specializzato nella configurazione, installazione, diagnostica e manutenzione di sistemi client/server, notebook, infrastrutture di stampa di rete (Network Printers e Multi-Function Printers) e periferiche IT, con attività svolte sia presso la struttura interna sia in assistenza on-site presso clienti.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- ---------- CTA ---------- -->
  <div class="cv-cta">
    <a href="https://marzorati.co/contact/">Contattami</a>
  </div>

</div>

<script>
(function () {
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function setFill(row) {
    var percent = parseFloat(row.getAttribute('data-percent')) || 0;
    var fill = row.querySelector('.skill-fill');
    if (!fill) return;
    if (reduceMotion) {
      fill.style.transition = 'none';
    }
    // next frame so the transition actually fires
    requestAnimationFrame(function () {
      fill.style.width = percent + '%';
    });
  }

  function init() {
    var rows = document.querySelectorAll('.skill-row');
    if (!rows.length) return;

    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            setFill(entry.target);
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.4 });

      rows.forEach(function (row) { observer.observe(row); });
    } else {
      rows.forEach(setFill);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
</script>
