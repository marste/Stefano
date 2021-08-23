---
layout: page
title: Meteo Lombardia
permalink: /meteo-lombardia/
image: 'https://marzorati.co/img/meteo.png'
share-img: 'https://marzorati.co/img/meteo.png'
---
<center><iframe src="https://astrogeo.va.it/meteo/widget/widget.php?colore=blu&temperatura=true" style="width:320px;height:440px; border:none"></iframe></center>

   <button class="button button_header"></button>

	<div class="container">
        <a href="meteo/"><img src="/data/bollettino/mappa_meteo_oggi_gen.jpg?t=1629694527" id="meteomap" alt="Mappa meteo Centro Geofisico Prealpino"></a>
	</div>

	<div class="row">
            <div class="column"><button class="button button_select" id="button_oggi" onclick="cambia_mappa('oggi')">Lunedì</button></div>
            <div class="column"><button class="button button_select" id="button_domani" onclick="cambia_mappa('domani')">Martedì</button></div>
            <div class="column"><button class="button button_select" id="button_dopodomani" onclick="cambia_mappa('dopodomani')">Mercoledì</button></div>

        </div>
        <p class="credit">dettagli su <a href="">astrogeo.va.it</a></p> 

        <script>
        function cambia_mappa(giorno){
            document.getElementById("meteomap").src="/data/bollettino/mappa_meteo_"+giorno+"_gen.jpg?t=1629694527"
            
            k=['oggi', 'domani', 'dopodomani']
            for( i=0; i<3; i++ ){
                document.getElementById("button_"+ k[i]).style.textDecoration = 'none';
                            }

            document.getElementById("button_"+giorno).style.textDecoration = 'underline';
                    }

        cambia_mappa('oggi')        </script>