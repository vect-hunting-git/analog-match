import pandas as pd
import folium

moon = pd.read_csv("ranking_moon.csv", index_col="Site")
mars = pd.read_csv("ranking_mars.csv", index_col="Site")

# Site coordinates (latitude, longitude), from the sources in evidence.csv
# Svalbard pin is at Longyearbyen, approximate; check against the Longyearbyen Wikipedia page.
coords = {
    "Devon Island": (75.25, -88.0),
    "Dry Valleys": (-77.4667, 162.5167),
    "Svalbard": (78.22, 15.65),
    "Mauna Kea": (19.8206, -155.4681),
    "Atacama": (-24.5, -69.25),
}


def color_for(score):
    if score >= 3.5:
        return "green"
    if score >= 3.0:
        return "orange"
    return "red"


m = folium.Map(
    location=[20, 0],
    zoom_start=2,
    min_zoom=2,
    tiles=None,
    max_bounds=True,
    min_lat=-85, max_lat=85, min_lon=-180, max_lon=180,
)
folium.TileLayer(
    tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
    attr="Tiles &copy; Esri, Maxar, Earthstar Geographics",
    no_wrap=True,
).add_to(m)

for site, (lat, lon) in coords.items():
    moon_score = moon.loc[site, "Total"]
    mars_score = mars.loc[site, "Total"]
    avg = (moon_score + mars_score) / 2

    popup_html = (
        f"<b>{site}</b><br>"
        f"Moon south pole score: {moon_score:.2f}<br>"
        f"Mars score: {mars_score:.2f}<br>"
        f"Average (both): {avg:.2f}"
    )

    folium.CircleMarker(
        location=(lat, lon),
        radius=10 + avg * 2,
        color=color_for(avg),
        fill=True,
        fill_color=color_for(avg),
        fill_opacity=0.7,
        popup=folium.Popup(popup_html, max_width=250),
        tooltip=f"{site}: avg {avg:.2f}",
    ).add_to(m)

legend_html = """
<div style="position: fixed; bottom: 30px; left: 30px; z-index: 9999;
 background: white; padding: 10px; border: 1px solid grey; font-size: 13px;">
<b>Average Moon + Mars score</b><br>
<span style="color:green;">&#9679;</span> 3.5 or higher<br>
<span style="color:orange;">&#9679;</span> 3.0 to 3.49<br>
<span style="color:red;">&#9679;</span> below 3.0
</div>
"""
m.get_root().html.add_child(folium.Element(legend_html))

m.save("analog_map.html")
print("Saved analog_map.html. Open it in your browser.")