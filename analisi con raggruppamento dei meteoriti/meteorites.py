import matplotlib.pyplot as plt
import json, folium
from folium.plugins import MarkerCluster

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
    if(elem["mass"] is None or elem["mass"]!=elem["mass"]):
        continue
    masse.append(elem["mass"])
    if(elem["year"] is None or elem["year"]!=elem["year"]):
        continue
    anni.append(elem["year"])
    if(elem["lat"] is None or elem["lat"]!=elem["lat"]):
        continue
    lat.append(float(elem["lat"]))
    if(elem["long"] is None or elem["long"]!=elem["long"]):
        continue
    long.append(float(elem["long"]))

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