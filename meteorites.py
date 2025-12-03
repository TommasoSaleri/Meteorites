import matplotlib.pyplot as plt
import json

file_name = "meteorites.json"

with open(file_name, "r", encoding="utf8") as file:
    stringa = file.read()

#print(type(stringa))
dati_meteoriti = json.loads(stringa)
#print(type(dati_meteoriti))

#print(dati_meteoriti[0].keys())

masse = []
for elem in dati_meteoriti:
    try:
        masse.append(elem["mass"])
    except:
        continue

anni = []
for elem in dati_meteoriti:
    try:
        anni.append(elem["year"])
    except:
        continue

#print(masse)
#print(anni)

plt.figure(figsize=(10, 6))
plt.scatter(anni, masse, alpha=0.5)
plt.xlabel("Anno di Ritrovamento")
plt.ylabel("Massa (g)")
plt.title("Relazione tra Massa e Anno di Ritrovamento dei Meteoriti")
plt.grid(True)
plt.show()