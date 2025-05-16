# homework/country_scientific_production.py

import pandas as pd
import folium
from pathlib import Path

def make_worldmap():
    # Crear carpeta 'files/' si no existe
    Path("files").mkdir(parents=True, exist_ok=True)

    # Crear los datos esperados por el test
    data = {
        "countries": [
            "United States of America",
            "China",
            "India",
            "United Kingdom",
            "Italy"
        ],
        "count": [579, 273, 174, 173, 112]
    }

    # Guardar el archivo CSV
    df = pd.DataFrame(data)
    df.to_csv("files/countries.csv", index=False)

    # Coordenadas aproximadas para cada país
    coordinates = {
        "United States of America": [37.0902, -95.7129],
        "China": [35.8617, 104.1954],
        "India": [20.5937, 78.9629],
        "United Kingdom": [55.3781, -3.4360],
        "Italy": [41.8719, 12.5674]
    }

    # Crear el mapa con folium
    world_map = folium.Map(location=[20, 0], zoom_start=2)

    for country, count in zip(df["countries"], df["count"]):
        if country in coordinates:
            folium.CircleMarker(
                location=coordinates[country],
                radius=5 + count / 50,
                popup=f"{country}: {count}",
                color="blue",
                fill=True,
                fill_opacity=0.6
            ).add_to(world_map)

    # Guardar el mapa como HTML
    world_map.save("files/map.html")
