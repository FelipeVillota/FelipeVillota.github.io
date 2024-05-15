---
date: 2024-01-15
layout: post
title: Missing people in Colombia 
subtitle: 
description: Sí vamos
image: https://felipevillota.com/wp-content/uploads/2024/05/Captura-de-pantalla-548.png
optimized_image: 
category: project
tags:
  - map
  - leaflet
  - GIS
  - R
author: Felipe Villota 
---

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Map</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <style>
        #map { height: 600px; width: 100%; }
    </style>
</head>
<body>
    <h1>Interactive Map of Missing Persons in Colombia</h1>
    <div id="map"></div>
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script>
        var map = L.map('map').setView([51.505, -0.09], 13);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        }).addTo(map);
    </script>
</body>
</html>


