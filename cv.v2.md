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

<style>
  .skills {
    max-width: 1280px;
    margin: 0 auto 50px auto;
    padding: 0 20px;
  }

  .skill-title.section-title {
    text-align: center;
    font-weight: 800;
    letter-spacing: -0.02em;
    margin-bottom: 40px;
  }

  .skill-title.section-title .ion {
    color: var(--primary-color, #2563eb);
    margin-right: 10px;
  }

  .chart-box {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 40px;
  }

  .chart-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 140px;
  }

  @media screen and (min-width: 576px) {
    .chart-item {
      flex-basis: 33.333%;
    }
  }

  .chart {
    position: relative;
    width: 120px;
    height: 120px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    background: conic-gradient(var(--primary-color, #2563eb) 0deg, var(--line-color, #e2e8f0) 0deg);
    transition: background 0.3s ease-out;
  }

  .chart::before {
    content: '';
    position: absolute;
    width: 92px;
    height: 92px;
    border-radius: 50%;
    background: var(--card-bg, #ffffff);
  }

  .chart .percent {
    position: relative;
    z-index: 2;
    font-weight: 800;
    font-size: 1.3em;
    color: var(--text-main, #0f172a);
  }

  .chart .percent::after {
    content: '';
  }

  .chart-title {
    margin-top: 14px;
    text-align: center;
    font-weight: 600;
    color: var(--text-muted, #64748b);
  }

  @media (max-width: 600px) {
    .chart-box {
      gap: 25px;
    }
    .chart-item {
      width: 110px;
    }
    .chart {
      width: 100px;
      height: 100px;
    }
    .chart::before {
      width: 76px;
      height: 76px;
    }
  }
</style>

<!-- begin skills -->
<div class="skills">
  
  <div class="chart-box">
  
    
    <div class="chart-item">
      <div class="chart" data-percent="90"><span class="percent">97</span>%</div>
      <span class="chart-title">IT Leadership & Management</span>
    </div>
    
  
    
    <div class="chart-item">
      <div class="chart" data-percent="95"><span class="percent">96</span>%</div>
      <span class="chart-title">Infrastructure & Cloud</span>
    </div>
    
  
    
    <div class="chart-item">
      <div class="chart" data-percent="60"><span class="percent">95</span>%</div>
      <span class="chart-title">Cybersecurity & Networking</span>
    </div>
    
  
    
    <div class="chart-item">
      <div class="chart" data-percent="80"><span class="percent">94</span>%</div>
      <span class="chart-title">Project Management</span>
    </div>
    
  
    
    <div class="chart-item">
      <div class="chart" data-percent="85"><span class="percent">93</span>%</div>
      <span class="chart-title">Microsoft Technologies</span>
    </div>
    
  
    
    <div class="chart-item">
      <div class="chart" data-percent="70"><span class="percent">97</span>%</div>
      <span class="chart-title">Problem Solving & Innovation</span>
    </div>
    
  
  </div>
</div>
<!-- end skills -->

<script>
(function () {
  function animateChart(chartEl) {
    var target = parseFloat(chartEl.getAttribute('data-percent')) || 0;
    var percentSpan = chartEl.querySelector('.percent');
    var displayTarget = percentSpan ? parseFloat(percentSpan.textContent) || target : target;
    var duration = 1400;
    var start = null;

    function easeOutCubic(t) {
      return 1 - Math.pow(1 - t, 3);
    }

    function step(timestamp) {
      if (!start) start = timestamp;
      var progress = Math.min((timestamp - start) / duration, 1);
      var eased = easeOutCubic(progress);
      var currentDeg = target * 3.6 * eased;
      var currentPercent = Math.round(displayTarget * eased);

      chartEl.style.background =
        'conic-gradient(var(--primary-color, #2563eb) ' + currentDeg + 'deg, var(--line-color, #e2e8f0) 0deg)';

      if (percentSpan) {
        percentSpan.textContent = currentPercent;
      }

      if (progress < 1) {
        window.requestAnimationFrame(step);
      }
    }

    window.requestAnimationFrame(step);
  }

  function initCharts() {
    var charts = document.querySelectorAll('.chart-box .chart');
    if (!charts.length) return;

    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            animateChart(entry.target);
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.4 });

      charts.forEach(function (chart) {
        observer.observe(chart);
      });
    } else {
      charts.forEach(animateChart);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initCharts);
  } else {
    initCharts();
  }
})();
</script>

<style>
  :root {
    --primary-color: #2563eb;
    --primary-light: #dbeafe;
    --line-color: #e2e8f0;
    --card-bg: #ffffff;
    --text-main: #0f172a;
    --text-muted: #64748b;
    --border-default: #e2e8f0;
  }

  /* ===========================
     CV PAGE (isolata dal tema)
     =========================== */
	 
	.cv-fullwidth{
	width: 100%;
	max-width: 100%;
	margin: 0;
	padding: 0;
	}

  .cv-page {
    font-family: 'Montserrat', sans-serif;
    background: var(--bg-color);
    color: var(--text-main);
    line-height: 1.65;
    padding: 20px 0;
  }

  .cv-container {
    max-width: 1280px;
    margin: 0 auto;
    width: 100%;
    padding: 0 20px;
  }

  /* Titoli */
  .cv-title {
    text-align: center;
    margin-bottom: 50px;
  }

  .cv-title h2 {
    margin: 0;
    font-weight: 800;
    letter-spacing: -0.02em;
  }

  .cv-subtitle {
    margin-top: 10px;
    color: var(--text-muted);
    
  }

  /* Timeline */
  .timeline {
    position: relative;
    padding-left: 40px;
  }

  .timeline::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 3px;
    background: var(--line-color);
  }

  .timeline-date-label {
    position: relative;
    font-weight: 700;
    color: var(--primary-color);
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

  /* Card */
  .card {
    background: var(--card-bg);
    border: 1px solid var(--border-default);
    border-radius: 12px;
    padding: 30px;
    margin-bottom: 50px;
    position: relative;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    transition: all 0.25s ease-in-out;
  }

  .card:hover {
    transform: translateY(-5px);
    border-color: var(--primary-color);
    box-shadow: 0 12px 20px -5px rgba(37, 99, 235, 0.15);
  }

  .role {
    
    font-weight: 800;
    color: var(--text-main);
    margin: 0;
  }

  .company-name {
	color: var(--primary-color);
    font-weight: 700;
    margin-top: 6px;
    display: block;
	text-align: center;
  }

  .company-name a {
	color: inherit;
    text-decoration: none;
  }

  .company-desc {
    color: var(--text-muted);
    font-weight: 400;
    display: block;
    margin-top: 4px;
    font-style: italic;
	font-size: 0.8em;
  }

  .cv-section {
    margin-top: 22px;
  }

  .cv-section-title {
    display: block;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--text-muted);
    letter-spacing: 0.05em;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid #f1f5f9;
  }

  /* Testo */
  .cv-text {
    color: #334155;
    text-align: justify;
  }

  .cv-text p {
    margin: 0 0 12px 0;
  }

  .cv-text b,
  .cv-text strong {
    color: var(--text-main);
    font-weight: 700;
  }

  /* Liste */
  .cv-list {
    margin: 0;
    padding-left: 18px;
  }

  .cv-list li {
    margin-bottom: 8px;
  }

  /* Skill tags */
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
    color: var(--text-main);
    transition: background 0.2s;
  }

  .card:hover .skill-tag {
    background: #ffffff;
    border-color: var(--primary-light);
  }

  /* CTA */
  .cv-cta {
    text-align: center;
    margin-top: 30px;
  }

  /* Mobile */
  @media (max-width: 600px) {
    .role {
      
    }

    .timeline {
      padding-left: 30px;
    }

    .timeline-date-label::before {
      left: -36px;
    }

    .card {
      padding: 20px;
    }
  }
</style>

<div class="cv-page">
  <div class="cv-container">

    <div class="timeline">

      <!-- =======================
           ALFA
           ======================= -->
      <span class="timeline-date-label">07/2023 – OGGI</span>

      <div class="card">
        <h2 class="role">IT Manager</h2>

        <span class="company-name">
          <a href="http://www.alfavarese.it/" target="_blank" rel="noopener">ALFA S.r.l.</a>
        </span>

        <span class="company-desc">
          Società pubblica costituita nel giugno 2015 che gestisce il Servizio Idrico Integrato della Provincia di Varese.
        </span>

        <div class="cv-section">
          <span class="cv-section-title">Principali competenze ed attività trasversali</span>

          <div class="cv-text">
            <p>
              Nel corso della mia esperienza, mi sono occupato di <b>migliorare i processi aziendali</b> attraverso
              l'implementazione di strategie mirate, che hanno permesso di ridurre le inefficienze e aumentare
              significativamente la produttività del team.
            </p>

            <p>
              Ho avuto la <b>responsabilità completa della gestione delle infrastrutture IT</b>, assicurando la massima
              continuità operativa e guidando il costante aggiornamento tecnologico. In questo contesto, ho sviluppato e
              gestito <b>ambienti virtualizzati</b> per ottimizzare l'utilizzo delle risorse hardware, migliorando così la
              scalabilità e la flessibilità dell'intero ecosistema IT.
            </p>

            <p>
              Un aspetto a cui ho sempre dedicato grande attenzione è la <b>cybersecurity</b>. Ho implementato soluzioni di
              sicurezza per proteggere i dati aziendali, concentrandomi sia sulla prevenzione proattiva delle minacce che
              sulla gestione delle vulnerabilità.
            </p>

            <p>
              Ho guidato con successo un <b>team IT multidisciplinare</b>, promuovendo una cultura di forte collaborazione e
              crescita professionale. La mia attività ha incluso la <b>gestione dell'infrastruttura di rete</b>,
              garantendo una connettività sicura e affidabile tra tutti i siti aziendali.
            </p>

            <p>
              Nel quotidiano, ho applicato le mie capacità di <b>problem solving</b> per risolvere situazioni complesse
              legate all'infrastruttura e ai processi, assicurando sempre il ripristino rapido delle operazioni critiche.
              Queste competenze sono state fondamentali anche nella <b>gestione di progetti IT</b> end-to-end, che ho
              portato a termine rispettando tempi, budget e obiettivi, con un costante focus sulla qualità e sulla
              soddisfazione degli stakeholder.
            </p>

            <p>
              A livello di pianificazione, ho <b>collaborato con vari dipartimenti</b> per anticipare le esigenze future,
              gestire il rifornimento e garantire la continuità operativa. Sul fronte economico e contrattuale, ho
              <b>gestito e negoziato contratti</b> con fornitori e partner, ottenendo condizioni vantaggiose, e mi sono
              occupato della <b>stesura e del monitoraggio del budget IT</b>, assicurando un uso efficiente delle risorse.
              Queste attività sono parte integrante di un più ampio lavoro di <b>pianificazione strategica</b> e
              definizione di budget e previsioni per il dipartimento IT.
            </p>
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

      <!-- =======================
           SIIT
           ======================= -->
      <span class="timeline-date-label">05/2015 – 07/2023</span>

      <div class="card">
        <h2 class="role">IT Manager</h2>

        <span class="company-name">
          <a href="http://www.siitgroup.com/" target="_blank" rel="noopener">S.I.I.T. S.r.l.</a>
        </span>

        <span class="company-desc">
          Azienda leader partner per lo sviluppo e produzione di specialità medicinali e integratori alimentari.
        </span>

        <div class="cv-section">
          <span class="cv-section-title">Principali competenze ed attività tecniche</span>

          <div class="cv-text">
            <ul class="cv-list">
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
        </div>

        <div class="cv-section">
          <span class="cv-section-title">Installazione &amp; Manutenzione</span>

          <div class="skill-container">
            <span class="skill-tag">MS Windows Client e Servers</span>
            <span class="skill-tag">Firewall Sonicwall Dell</span>
            <span class="skill-tag">Firewall Cisco Firepower</span>
            <span class="skill-tag">Switch Cisco</span>
            <span class="skill-tag">ESX / VMware Server</span>
            <span class="skill-tag">Office 365 / Exchange Online / SharePoint</span>
            <span class="skill-tag">Linux / Apache / MySQL / PHP</span>
            <span class="skill-tag">IBM iSeries</span>
            <span class="skill-tag">Microsoft SQL</span>
            <span class="skill-tag">Cisco VPN</span>
            <span class="skill-tag">Sophos XDR</span>
            <span class="skill-tag">Cynet Cybersecurity</span>
            <span class="skill-tag">Telefonia VOIP Selta</span>
            <span class="skill-tag">Telefonia DECT Spectralink</span>
            <span class="skill-tag">Data Logger RF</span>
            <span class="skill-tag">Lettori Barcode</span>
            <span class="skill-tag">Controllo accessi</span>
          </div>
        </div>

        <div class="cv-section">
          <span class="cv-section-title">Principali competenze ed attività trasversali</span>

          <div class="cv-text">
            <ul class="cv-list">
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
        </div>
      </div>

      <!-- =======================
           EDISPORT
           ======================= -->
      <span class="timeline-date-label">01/2007 – 05/2015</span>

      <div class="card">
        <h2 class="role">ICT System Administrator</h2>

        <span class="company-name">
          <a href="http://www.edisport.it/" target="_blank" rel="noopener">Edisport Editoriale S.p.A.</a>
        </span>

        <span class="company-desc">
          Casa Editrice nata nel 1914 con la fondazione della rivista "Motociclismo"
        </span>

        <div class="cv-section">
          <span class="cv-section-title">Principali competenze ed attività tecniche</span>

          <div class="cv-text">
            <ul class="cv-list">
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
        </div>

        <div class="cv-section">
          <span class="cv-section-title">Installazione &amp; Manutenzione</span>

          <div class="skill-container">
            <span class="skill-tag">MS Windows Client e Servers</span>
            <span class="skill-tag">Web Servers Linux (CentOS / Debian / Ubuntu)</span>
            <span class="skill-tag">Firewall &amp; Proxy Linux</span>
            <span class="skill-tag">ESX / VMware Server</span>
            <span class="skill-tag">Apache / MySQL / PHP</span>
            <span class="skill-tag">Blade Servers IBM</span>
            <span class="skill-tag">IBM AS/400</span>
            <span class="skill-tag">Sistemi Editoriali (Adobe, Woodwing)</span>
            <span class="skill-tag">IBM Lotus Domino (ora HCL Domino)</span>
            <span class="skill-tag">Microsoft Exchange</span>
            <span class="skill-tag">VPN (OpenVPN)</span>
            <span class="skill-tag">Server FTP</span>
            <span class="skill-tag">Appliance Symantec Antivirus-Antispam</span>
            <span class="skill-tag">Barracuda Spam &amp; Virus Firewall</span>
            <span class="skill-tag">Telefonia VOIP Cisco</span>
            <span class="skill-tag">Appliance NAS NetApp</span>
            <span class="skill-tag">Barracuda Message Archiver</span>
            <span class="skill-tag">Door &amp; Security Intercoms</span>
          </div>
        </div>

        <div class="cv-section">
          <span class="cv-section-title">Principali competenze ed attività trasversali</span>

          <div class="cv-text">
            <ul class="cv-list">
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
        </div>
      </div>

      <!-- =======================
           IRPE
           ======================= -->
      <span class="timeline-date-label">12/2004 – 01/2007</span>

      <div class="card">
        <h2 class="role">IT Senior Consultant</h2>

        <span class="company-name">
          <b>IRPE S.p.A.</b>
        </span>

        <span class="company-desc">
          Azienda ICT per la fornitura di servizi di outsourcing, consulenza, progettazione e gestione di architetture, applicazioni e sicurezza
        </span>

        <div class="cv-section">
          <span class="cv-section-title">Principali competenze ed attività tecniche</span>

          <div class="cv-text">
            <p>
              Sistemista di rete specializzato nell’installazione ed amministrazione di <b>Server IBM Lotus Domino (ora HCL Domino)</b> in cluster con funzione di
              <b>mail server</b> e <b>application server</b> per un bacino di 5000 utenze, presso: <b>Carrefour Italia S.p.A.</b>
            </p>
            <p>
              Collaborazione costante con fornitori software e con i servizi interni di Carrefour S.p.A. (personale italiano ed estero).
            </p>
            <p>
              Gestione di un server IBM Lotus Domino dedicato al <b>BlackBerry Enterprise</b> per garantire connettività wireless alla dirigenza.
            </p>
            <p>
              Amministrazione piattaforme Microsoft per gestione domini, file server, software distribution e backup.
            </p>
            <p>
              Gestione intranet di gruppo e parte dei siti internet pubblicandone i contenuti in accordo con marketing e società esterne.
            </p>
          </div>
        </div>
      </div>

      <!-- =======================
           WIIT
           ======================= -->
      <span class="timeline-date-label">02/2004 – 12/2004</span>

      <div class="card">
        <h2 class="role">IT Senior Consultant</h2>

        <span class="company-name">
          <a href="http://www.wiit.it/" target="_blank" rel="noopener">WIIT S.p.A.</a>
        </span>

        <span class="company-desc">
          Azienda ICT per la fornitura di servizi di outsourcing
        </span>

        <div class="cv-section">
          <span class="cv-section-title">Principali competenze ed attività tecniche</span>

          <div class="cv-text">
            <p>
              Sistemista di rete specializzato nell’installazione, amministrazione e presidio di server IBM Lotus Domino presso:
              Mediaset, Medusa Film e Alcantara.
            </p>
          </div>
        </div>
      </div>

      <!-- =======================
           TC SISTEMA (IT Consultant)
           ======================= -->
      <span class="timeline-date-label">04/2000 – 02/2004</span>

      <div class="card">
        <h2 class="role">IT Consultant</h2>

        <span class="company-name">
          <a href="https://www.soldionline.it/notizie/azioni-italia/tc-sistema-arriva-il-fallimento" target="_blank" rel="noopener">
            TC Sistema S.p.A.
          </a>
        </span>

        <span class="company-desc">
          Azienda ICT per la fornitura di servizi di outsourcing, consulenza, progettazione e gestione di architetture, applicazioni e sicurezza
        </span>

        <div class="cv-section">
          <span class="cv-section-title">Principali competenze ed attività tecniche</span>

          <div class="cv-text">
            <p>Sistemista di rete specializzato nell’installazione ed amministrazione di server IBM Lotus Domino.</p>
            <p>Docente di corsi IBM Lotus Domino Administrator.</p>
            <p>Installazione ed amministrazione di ambienti Microsoft.</p>
          </div>
        </div>
      </div>

      <!-- =======================
           TC SISTEMA (Hardware Engineer)
           ======================= -->
      <span class="timeline-date-label">09/1997 – 04/2000</span>

      <div class="card">
        <h2 class="role">Hardware Engineer</h2>

        <span class="company-name">
          <a href="https://www.soldionline.it/notizie/azioni-italia/tc-sistema-arriva-il-fallimento" target="_blank" rel="noopener">
            TC Sistema S.p.A.
          </a>
        </span>

        <span class="company-desc">
          Azienda ICT per la fornitura di servizi di outsourcing, consulenza, progettazione e gestione di architetture, applicazioni e sicurezza
        </span>

        <div class="cv-section">
          <span class="cv-section-title">Principali competenze ed attività tecniche</span>

          <div class="cv-text">
            <p>
              Tecnico Hardware specializzato in installazione, riparazione e manutenzione di PC, stampanti locali o di rete, server
              (tecnico interno/esterno presso clienti).
            </p>
          </div>
        </div>
      </div>

    </div>

    <div class="cv-cta">
      <a href="https://marzorati.co/contact/" class="btn btn-primary btn-lg" role="button">Contattami</a>
    </div>

  </div>
</div>
