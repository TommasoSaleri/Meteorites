import matplotlib.pyplot as plt
import json

file_name = "meteorites.json"

with open(file_name, "r", encoding="utf8") as file:
    stringa = file.read()

#print(type(stringa))
dati_meteoriti = json.loads(stringa)
#print(type(dati_meteoriti))

print(dati_meteoriti[0].keys())

for elem in range(0, 5):
    print(dati_meteoriti[elem],"\n")

masse = []
anni = []
for elem in dati_meteoriti:
    try:
        masse.append(elem["mass"])
        anni.append(elem["year"])
    except:
        continue

#print(masse)
#print(anni)

plt.figure(figsize=(10, 6))
plt.hist(masse, bins=15, edgecolor='black', log=True)
plt.xlabel("Massa (g)")
plt.ylabel("Frequenza (Scala Logaritmica)")
plt.title("Distribuzione delle Masse dei Meteoriti")
plt.grid(axis='y', alpha=0.75)
plt.show()