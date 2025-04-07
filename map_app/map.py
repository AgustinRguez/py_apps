import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

data_stadium = pandas.read_csv("estadios.txt")
lon_stadium = list(data_stadium["long"])
lat_stadium = list(data_stadium["lat"])
club = list(data_stadium["club"])


argentina_map = folium.Map(location=[-34.66, -58.36], zoom_start=6)
fg_volcan = folium.FeatureGroup(name="Volcanes yankis")
fg_estadios = folium.FeatureGroup(name="Canchas de futbol argentino")
fg_poblacion = folium.FeatureGroup(name="Poblacion")

for lt, ln in zip(lat, lon):
    fg_volcan.add_child(folium.Circle(location=[lt, ln], popup="First marker", icon=folium.Icon("red")))

for stadium_lat, stadium_ln, cl in zip(lat_stadium, lon_stadium, club):
    fg_estadios.add_child(folium.Marker(location=[stadium_lat, stadium_ln], popup="Estadio de " + cl, icon=folium.Icon("green")))

fg_poblacion.add_child(folium.GeoJson(open("world.json", encoding="utf-8-sig").read(),
style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

argentina_map.add_child(fg_volcan)
argentina_map.add_child(fg_estadios)
argentina_map.add_child(fg_poblacion)
argentina_map.add_child(folium.LayerControl())

argentina_map.save("mapa.html")
