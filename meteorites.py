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