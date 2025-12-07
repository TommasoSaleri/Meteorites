## Descrizione del problema

Il dataset contiene circa **45.000 meteorit**i, ognuno con coordinate geografiche.
La generazione delle mappe con **Folium** può risultare molto pesante quando ogni meteorite viene rappresentato come **Marker singolo**.

L’esecuzione degli script Python termina correttamente e produce tutti i file previsti, ma:

* **l’utilizzo di 45.000 marker singoli causa tempi di caricamento estremamente lunghi**
* il browser deve gestire decine di migliaia di elementi HTML
* la mappa risultante può **non caricarsi** oppure **bloccarsi** al primo movimento

---

### Mappe con Heatmap

Entrambi gli script generano una mappa di calore.
La heatmap è leggera e può essere visualizzata senza differenze tra i due file Python.

---

### Analisi con raggruppamento dei meteoriti

Lo script nella cartella **“analisi con raggruppamento dei meteoriti”** utilizza un sistema di cluster per aggregare i punti sulla mappa.
Questo permette di:

* visualizzare i meteoriti in modo fluido
* espandere i gruppi tramite zoom
* analizzare le singole cadute senza blocchi del browser

Questa è la versione consigliata per l’analisi dettagliata.

---

### Analisi con meteoriti singoli

Lo script nella cartella **“analisi con meteoriti singoli”** produce due mappe:

* una con marker singoli
* una mappa di calore

La mappa con marker singoli non utilizza alcun raggruppamento, quindi il browser deve caricare **45.000+ elementi**.
Il risultato previsto è:

* caricamento estremamente lento o mancato
* blocco della pagina al primo spostamento
* utilizzo praticamente impossibile

Per questi motivi l’uso di questa mappa non è raccomandato.
