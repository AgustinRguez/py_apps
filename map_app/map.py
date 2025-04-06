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
fg = folium.FeatureGroup("argentina Maps")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="First marker", icon=folium.Icon("blue")))

for stadium_lat, stadium_ln, cl in zip(lat_stadium, lon_stadium, club):
    fg.add_child(folium.Marker(location=[stadium_lat, stadium_ln], popup="Estadio de " + cl, icon=folium.Icon("blue")))

argentina_map.add_child(fg)
argentina_map.save("argentina_map1.html")
