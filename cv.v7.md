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
  .cv-wrapper {
    display: flex;
    justify-content: center;
    padding: 40px 20px;
    min-height: 100vh;
    background: #ffffff;
  }

  .cv-resume {
    --ink: #0f172a;
    --muted: #64748b;
    --faint: #94a3b8;
    --accent: #2563eb;
    --hairline: #e2e8f0;
    --bg: #ffffff;

    width: 100%;
    max-width: 820px;           /* ← più arioso e moderno */
    margin: 0 auto;
    padding: 60px 32px 80px;
    font-family: 'Montserrat', sans-serif;
    color: var(--ink);
    line-height: 1.65;
    background: var(--bg);
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05); /* opzionale: leggero rilievo */
    border-radius: 8px;
  }

  .cv-resume .mono {
    font-family: 'JetBrains Mono', ui-monospace, monospace;
  }

  .cv-resume a { color: inherit; }
  .cv-resume :focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 3px;
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
  .cv-section-eyebrow .ion { font-size: 14px; }

  .cv-skills, .cv-experience { margin-bottom: 64px; }

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
      grid-template-areas: "name value" "bar bar";
      row-gap: 6px;
    }
    .skill-name { grid-area: name; }
    .skill-value { grid-area: value; }
    .skill-track { grid-area: bar; }
  }

  /* ---------- Experience ---------- */
  .entry {
    padding: 36px 0;
    border-top: 1px solid var(--hairline);
  }
  .entry:first-of-type { border-top: 1px solid var(--hairline); }

  .entry-date {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    font-size: 12px;
    color: var(--faint);
    margin-bottom: 10px;
  }

  .entry-role {
    margin: 0 0 8px 0;
    font-weight: 800;
    color: var(--ink);
  }

  .entry-company {
    font-weight: 600;
    color: var(--accent);
    margin-bottom: 8px;
  }
  .entry-company a { text-decoration: none; }
  .entry-company a:hover { text-decoration: underline; }

  .entry-desc {
    font-style: italic;
    color: var(--muted);
    margin-bottom: 18px;
  }

  .entry-text p {
    margin-bottom: 12px;
    color: #334155;
    text-align: justify;
  }
  .entry-text p:last-child { margin-bottom: 0; }
  .entry-text b { color: var(--ink); font-weight: 700; }

  .entry-block { margin-top: 20px; }
  .entry-block-title {
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
  .entry-list li { margin-bottom: 6px; }

  .entry-stack {
    font-size: 14px;
    color: var(--muted);
    line-height: 1.9;
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
    transition: all 0.2s;
  }
  .cv-cta a:hover {
    border-color: var(--accent);
    color: var(--accent);
  }
</style>

<div class="cv-wrapper">
  <div class="cv-resume">
    <!-- Hero (se vuoi aggiungerlo in futuro) -->
    <!-- <div class="cv-hero"> ... </div> -->

    <!-- Skills -->
    <div class="cv-skills">
      <div class="cv-section-eyebrow"><i class="ion ion-ios-desktop"></i>Skills</div>
      <div class="skills-list">
        <!-- ... il tuo codice skills rimane identico ... -->
        <div class="skill-row" data-percent="97"><span class="skill-name">IT Leadership & Management</span><div class="skill-track"><div class="skill-fill"></div></div><span class="skill-value mono">97%</span></div>
        <div class="skill-row" data-percent="96"><span class="skill-name">Infrastructure & Cloud</span><div class="skill-track"><div class="skill-fill"></div></div><span class="skill-value mono">96%</span></div>
        <div class="skill-row" data-percent="95"><span class="skill-name">Cybersecurity & Networking</span><div class="skill-track"><div class="skill-fill"></div></div><span class="skill-value mono">95%</span></div>
        <div class="skill-row" data-percent="94"><span class="skill-name">Project Management</span><div class="skill-track"><div class="skill-fill"></div></div><span class="skill-value mono">94%</span></div>
        <div class="skill-row" data-percent="93"><span class="skill-name">Microsoft Technologies</span><div class="skill-track"><div class="skill-fill"></div></div><span class="skill-value mono">93%</span></div>
        <div class="skill-row" data-percent="98"><span class="skill-name">Problem Solving & Innovation</span><div class="skill-track"><div class="skill-fill"></div></div><span class="skill-value mono">98%</span></div>
      </div>
    </div>

    <!-- Experience -->
    <div class="cv-experience">
      <div class="cv-section-eyebrow"><i class="ion ion-ios-briefcase"></i>Professional Experience</div>
      
      <!-- Il resto del tuo codice delle esperienze rimane **identico** -->
      <!-- (ALFA, SIIT, EDISPORT, IRPE, WIIT, TC SISTEMA...) -->

    </div>

    <!-- CTA -->
    <div class="cv-cta">
      <a href="https://marzorati.co/contact/">Contattami</a>
    </div>
  </div>
</div>

<script>
  // Solo animazione delle skill bars (pulito e leggero)
  (function () {
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function setFill(row) {
      const percent = parseFloat(row.getAttribute('data-percent')) || 0;
      const fill = row.querySelector('.skill-fill');
      if (!fill) return;
      if (reduceMotion) fill.style.transition = 'none';
      requestAnimationFrame(() => fill.style.width = percent + '%');
    }

    const rows = document.querySelectorAll('.skill-row');
    if ('IntersectionObserver' in window) {
      const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            setFill(entry.target);
            observer.unobserve(entry.target);
          }
        });
      }, { threshold: 0.4 });
      rows.forEach(row => observer.observe(row));
    } else {
      rows.forEach(setFill);
    }
  })();
</script>