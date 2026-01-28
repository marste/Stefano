---
layout: page
title: Curriculum Vitae
permalink: /aaa/
---

    <style>
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
            background-color: #fff;
        }
        header {
            border-bottom: 2px solid #eee;
            padding-bottom: 20px;
            margin-bottom: 40px;
        }
        h1 { margin: 0; font-size: 2.5rem; color: #000; }
        h2 { 
            font-size: 1.2rem; 
            text-transform: uppercase; 
            letter-spacing: 1px; 
            color: #666; 
            margin-top: 40px;
            border-bottom: 1px solid #eee;
            padding-bottom: 5px;
        }
        .contact-info { margin-top: 10px; color: #777; }
        .contact-info a { color: #007bff; text-decoration: none; }
        
        .entry { margin-bottom: 30px; }
        .entry-header { display: flex; justify-content: space-between; align-items: baseline; }
        .entry-title { font-weight: bold; font-size: 1.1rem; }
        .entry-date { color: #888; font-size: 0.9rem; min-width: 120px; text-align: right; }
        .entry-location { font-style: italic; color: #555; }
        
        ul { padding-left: 20px; margin-top: 10px; }
        li { margin-bottom: 5px; }

        @media (max-width: 600px) {
            .entry-header { flex-direction: column; }
            .entry-date { text-align: left; margin-top: 5px; }
        }
    </style>

<body>

    <header>
        <h1>Il Tuo Nome</h1>
        <div class="contact-info">
            Email: <a href="mailto:tuo@email.it">tuo@email.it</a> | 
            GitHub: <a href="https://github.com/tuo-user">@tuo-user</a> | 
            Web: <a href="{{ site.url }}">{{ site.url }}</a>
        </div>
    </header>

    <section>
        <h2>Esperienza Professionale</h2>
        
        <div class="entry">
            <div class="entry-header">
                <span class="entry-title">Senior Software Engineer @ Azienda Tech</span>
                <span class="entry-date">2020 — Presente</span>
            </div>
            <div class="entry-location">Milano, Italia</div>
            <ul>
                <li>Sviluppo di infrastrutture scalabili in Python e Go.</li>
                <li>Gestione di un team di 5 persone e coordinamento sprint.</li>
            </ul>
        </div>

        <div class="entry">
            <div class="entry-header">
                <span class="entry-title">Junior Developer @ Startup Innovativa</span>
                <span class="entry-date">2018 — 2020</span>
            </div>
            <div class="entry-location">Remoto</div>
            <ul>
                <li>Implementazione di feature frontend con React.</li>
                <li>Ottimizzazione delle performance del database.</li>
            </ul>
        </div>
    </section>

    <section>
        <h2>Istruzione</h2>
        <div class="entry">
            <div class="entry-header">
                <span class="entry-title">Laurea Magistrale in Informatica</span>
                <span class="entry-date">2016 — 2018</span>
            </div>
            <div class="entry-location">Università degli Studi di...</div>
        </div>
    </section>

    <section>
        <h2>Competenze</h2>
        <p><strong>Linguaggi:</strong> Python, JavaScript (ES6+), C++, SQL.</p>
        <p><strong>Tecnologie:</strong> Docker, AWS, Git, Jekyll, React.</p>
    </section>

</body>
