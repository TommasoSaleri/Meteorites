import matplotlib.pyplot as plt
import json, folium
from folium.plugins import MarkerCluster
from folium.plugins import HeatMap

file_name = "meteorites.json"

with open(file_name, "r", encoding="utf8") as file:
    stringa = file.read()

#print(type(stringa))
dati_meteoriti = json.loads(stringa)
#print(type(dati_meteoriti))

print(dati_meteoriti[0].keys(),"\n")

for elem in range(0, 5):
    print(dati_meteoriti[elem],"\n")

masse = []
anni = []
lat = []
long = []

for elem in dati_meteoriti:
    massa = elem["mass"]
    anno = elem["year"]
    lat_uno = elem["lat"]
    long_uno = elem["long"]
    if(not(massa is None or massa!=massa)):
        masse.append(massa)
    if(not(anno is None or anno!=anno)):
        anni.append(anno)
    if(not(lat is None or lat_uno!=lat_uno)):
        lat.append(float(lat_uno))
    if(not(long_uno is None or long_uno!=long_uno)):
        long.append(float(long_uno))

#print(masse)
#print(anni)

plt.figure(figsize=(10, 6))
plt.hist(masse, bins=15, edgecolor='black', log=True)
plt.xlabel("Massa (g)")
plt.ylabel("Frequenza (Scala Logaritmica)")
plt.title("Distribuzione delle Masse dei Meteoriti")
plt.grid(axis='y', alpha=0.75)
plt.show()

lat_media = sum(lat) / len(lat)
long_media = sum(long) / len(long)
print(lat_media, long_media)

m = folium.Map(location = [lat_media, long_media], zoom_start = 2, tiles='CartoDB Positron')
marker_cluster = MarkerCluster().add_to(m)

for elem in dati_meteoriti:
    if elem["lat"] is None or elem["lat"] != elem["lat"] or elem["long"] is None or elem["long"] != elem["long"]:
        continue
    folium.Marker(
        location=[float(elem["lat"]), float(elem["long"])],
        popup=elem["name"],
        icon=folium.Icon(color='orange', icon_color="white", icon="meteor", prefix="fa")
    ).add_to(marker_cluster)

m.save("meteorites.html")

coordinate = []
for elem in dati_meteoriti:
    lat = elem["lat"]
    long = elem["long"]
    if(lat is None or lat!=lat or long is None or long!=long):
        continue
    coordinate.append([lat, long])

mappa_calore = folium.Map(location = [lat_media, long_media], zoom_start = 2)
HeatMap(coordinate).add_to(mappa_calore)
mappa_calore.save("meteorites-heatmap.html")