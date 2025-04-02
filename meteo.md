---
layout: page
title: Meteo Rescaldina
permalink: /meteo/
image: 'https://marzorati.co/img/meteo.png'
share-img: 'https://marzorati.co/img/meteo.png'
---
<center>

<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gray-100 flex flex-col items-center p-6">
    <div class="bg-white shadow-lg rounded-lg p-6 max-w-2xl w-full">
        <h1 class="text-2xl font-bold text-center text-blue-600 mb-4">Previsioni Meteo Rescaldina</h1>
        <div id="weather" class="text-center"></div>
    </div>

    <script>
        const apiKey = "65513a3eb3ea4269946134346250204";
        const weatherDiv = document.getElementById("weather");

        async function fetchWeather() {
            weatherDiv.innerHTML = "<p class='text-gray-600'>Caricamento...</p>";
            try {
                const response = await fetch(`https://api.weatherapi.com/v1/forecast.json?key=${apiKey}&q=Rescaldina,IT&days=7&lang=it`);
                const data = await response.json();
                displayWeather(data);
            } catch (error) {
                weatherDiv.innerHTML = "<p class='text-red-500'>Errore nel caricamento dei dati.</p>";
            }
        }

        function displayWeather(data) {
            if (!data || !data.forecast) {
                weatherDiv.innerHTML = "<p class='text-red-500'>Dati non disponibili.</p>";
                return;
            }
            let html = `<h2 class='text-xl font-semibold text-blue-500 mb-2'>${data.location.name}</h2>`;
            html += "<div class='grid grid-cols-2 gap-4'>";
            data.forecast.forecastday.forEach(day => {
                html += `
                    <div class='bg-gray-200 p-4 rounded shadow'>
                        <p class='font-bold'>${new Date(day.date).toLocaleDateString('it-IT', { weekday: 'long', day: 'numeric', month: 'long' })}</p>
                        <img src="${day.day.condition.icon}" alt="${day.day.condition.text}" class='mx-auto'>
                        <p>${day.day.condition.text}</p>
                        <p class='text-2xl font-bold text-gray-700'>🌡 Max: ${day.day.maxtemp_c}°C | Min: ${day.day.mintemp_c}°C</p>
                    </div>`;
            });
            html += "</div>";
            weatherDiv.innerHTML = html;
        }

        fetchWeather();
    </script>
</body>
</html>



</center>