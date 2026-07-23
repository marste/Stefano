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
<!-- JetBrains Mono -->
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

  /* ---------- Section eyebrow ---------- */
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

  /* ---------- Skills ---------- */
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

  /* ---------- Experience ---------- */
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

  /* ========== MOBILE ========== */
  @media (max-width: 640px) {
    .entry {
      grid-template-columns: 1fr;
      gap: 18px;
    }

    /* Date + Role sulla stessa riga */
    .entry-header {
      display: flex;
      align-items: baseline;
      gap: 12px;
      flex-wrap: wrap;
      margin-bottom: 8px;
    }

    .entry-date {
      display: flex;
      align-items: baseline;
      gap: 6px;
      padding-top: 0;
      margin-bottom: 0;
      flex-shrink: 0;
    }

    .entry-date .date-from {
      font-weight: 700;
      color: var(--ink);
    }

    .entry-date .date-to {
      font-size: 13px;
      color: var(--faint);
    }

    .entry-role {
      margin: 0;
      flex: 1;
      font-size: 1.1em;
    }

    .entry-date span {
      display: inline;
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
  <!-- Skills -->
  <div class="cv-skills">
    <div class="cv-section-eyebrow"><i class="ion ion-ios-desktop"></i>Skills</div>
    <div class="skills-list">
      <div class="skill-row" data-percent="97">
        <span class="skill-name">IT Leadership & Management</span>
        <div class="skill-track"><div class="skill-fill"></div></div>
        <span class="skill-value mono">97%</span>
      </div>
      <!-- ... altri skill (rimasti invariati) ... -->
    </div>
  </div>

  <!-- Experience -->
  <div class="cv-experience">
    <div class="cv-section-eyebrow"><i class="ion ion-ios-briefcase"></i>Professional Experience</div>

    <!-- ALFA -->
    <div class="entry">
      <div class="entry-header">
        <div class="entry-date mono"><span class="date-from">07/2023</span><span class="date-to">→ oggi</span></div>
        <h3 class="entry-role">IT Manager</h3>
      </div>
      <div class="entry-body">
        <div class="entry-company"><a href="http://www.alfavarese.it/" target="_blank" rel="noopener">ALFA S.r.l.</a></div>
        <div class="entry-desc">Società pubblica costituita nel giugno 2015 che gestisce il Servizio Idrico Integrato della Provincia di Varese.</div>
        <!-- resto invariato -->
        <div class="entry-text">
          <p>Nel corso della mia esperienza...</p>
          <!-- ... tutto il testo ... -->
        </div>
        <div class="entry-block">
          <span class="entry-block-title mono">Tech Stack</span>
          <div class="entry-stack mono">Cybersecurity · Infrastructure · Budget Management</div>
        </div>
      </div>
    </div>

    <!-- SIIT -->
    <div class="entry">
      <div class="entry-header">
        <div class="entry-date mono"><span class="date-from">05/2015</span><span class="date-to">→ 07/2023</span></div>
        <h3 class="entry-role">IT Manager</h3>
      </div>
      <div class="entry-body">
        <div class="entry-company"><a href="http://www.siitgroup.com/" target="_blank" rel="noopener">S.I.I.T. S.r.l.</a></div>
        <div class="entry-desc">Azienda leader partner per lo sviluppo e produzione di specialità medicinali e integratori alimentari.</div>
        <!-- resto invariato -->
        <div class="entry-block">
          <span class="entry-block-title mono">Competenze Tecniche</span>
          <ul class="entry-list"> ... </ul>
        </div>
        <!-- altri blocchi ... -->
      </div>
    </div>

    <!-- EDISPORT -->
    <div class="entry">
      <div class="entry-header">
        <div class="entry-date mono"><span class="date-from">01/2007</span><span class="date-to">→ 05/2015</span></div>
        <h3 class="entry-role">ICT System Administrator</h3>
      </div>
      <div class="entry-body">
        <div class="entry-company"><a href="http://www.edisport.it/" target="_blank" rel="noopener">Edisport Editoriale S.p.A.</a></div>
        <div class="entry-desc">Casa Editrice nata nel 1914 con la fondazione della rivista "Motociclismo".</div>
        <!-- resto invariato -->
      </div>
    </div>

    <!-- IRPE -->
    <div class="entry">
      <div class="entry-header">
        <div class="entry-date mono"><span class="date-from">12/2004</span><span class="date-to">→ 01/2007</span></div>
        <h3 class="entry-role">IT Senior Consultant</h3>
      </div>
      <div class="entry-body">
        <div class="entry-company">IRPE S.p.A.</div>
        <div class="entry-desc">Azienda ICT per la fornitura di servizi di outsourcing...</div>
        <div class="entry-text"> ... </div>
      </div>
    </div>

    <!-- WIIT -->
    <div class="entry">
      <div class="entry-header">
        <div class="entry-date mono"><span class="date-from">02/2004</span><span class="date-to">→ 12/2004</span></div>
        <h3 class="entry-role">IT Senior Consultant</h3>
      </div>
      <div class="entry-body">
        <div class="entry-company"><a href="https://wiit.cloud/" target="_blank" rel="noopener">WIIT S.p.A.</a></div>
        <div class="entry-desc">Azienda ICT per la fornitura di servizi di outsourcing.</div>
        <div class="entry-text"> ... </div>
      </div>
    </div>

    <!-- TC SISTEMA - IT Consultant -->
    <div class="entry">
      <div class="entry-header">
        <div class="entry-date mono"><span class="date-from">04/2000</span><span class="date-to">→ 02/2004</span></div>
        <h3 class="entry-role">IT Consultant</h3>
      </div>
      <div class="entry-body">
        <div class="entry-company"><a href="https://www.soldionline.it/notizie/azioni-italia/tc-sistema-arriva-il-fallimento" target="_blank" rel="noopener">TC Sistema S.p.A.</a></div>
        <div class="entry-desc">Azienda ICT per la fornitura di servizi di outsourcing...</div>
        <div class="entry-text"> ... </div>
      </div>
    </div>

    <!-- TC SISTEMA - Hardware Engineer -->
    <div class="entry">
      <div class="entry-header">
        <div class="entry-date mono"><span class="date-from">09/1997</span><span class="date-to">→ 04/2000</span></div>
        <h3 class="entry-role">Hardware Engineer</h3>
      </div>
      <div class="entry-body">
        <div class="entry-company"><a href="https://www.soldionline.it/notizie/azioni-italia/tc-sistema-arriva-il-fallimento" target="_blank" rel="noopener">TC Sistema S.p.A.</a></div>
        <div class="entry-desc">Azienda ICT per la fornitura di servizi di outsourcing...</div>
        <div class="entry-text"> ... </div>
      </div>
    </div>
  </div>

  <!-- CTA -->
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
    if (reduceMotion) fill.style.transition = 'none';
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