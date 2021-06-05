import folium
import pandas as pd

volcanoes = pd.read_csv("Volcanoes_USA.txt")
lat = list(volcanoes["LAT"])
lon = list(volcanoes["LON"])
elev = list(volcanoes["ELEV"])
name = list(volcanoes['NAME'])


def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "blue"
    else:
        return "red"


map_one = folium.Map(location=(38.58, -99.09), zoom_start=6, tiles="OpenStreetMap")
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    fgv.add_child(folium.CircleMarker(location=(lt, ln), radius=6, popup=folium.Popup("Elevation: " + str(el)),
                                      tooltip=nm, parse_html=True, fill_opacity=0.7, fill="True",
                                      color="grey", fill_color=color_producer(el)))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open("115 world.json", "r", encoding='utf-8-sig').read(),
                             style_function=lambda x: {"fillColor": 'green' if x['properties']['POP2005'] < 1000000
                             else 'orange' if 1000000 <= x['properties']['POP2005'] < 2000000 else "red"}))

map_one.add_child(fgv)
map_one.add_child(fgp)
map_one.add_child(folium.LayerControl())
map_one.save("map1.html")
