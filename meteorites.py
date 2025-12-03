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

plt.figure(figsize=(10, 6))
plt.hist(masse, bins=50, edgecolor='black', log=True)
plt.xlabel("Massa (g)")
plt.ylabel("Frequenza (Scala Logaritmica)")
plt.title("Distribuzione delle Masse dei Meteoriti")
plt.grid(axis='y', alpha=0.75)
plt.show()