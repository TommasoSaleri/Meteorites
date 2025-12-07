I file Python generano diverse mappe a partire da circa 45.000 meteoriti.
Il problema principale nasce quando si prova a inserire tutti questi punti come Marker sulla mappa Folium.
Folium riesce comunque a creare i file, ma il browser poi deve caricare più di 45.000 elementi grafici:
questo causa attese molto lunghe, caricamenti che vanno a buon fine solo raramente e, quasi sempre, il blocco completo della pagina appena ci si muove sulla mappa.

Entrambi gli script producono una mappa di calore.
Questa funziona senza problemi, perché la heatmap gestisce i dati in modo molto più leggero.

Lo script nella cartella “analisi con raggruppamento dei meteoriti” adotta un sistema che raggruppa i punti sulla mappa.
Questo approccio permette di:
  caricare la mappa velocemente;
  zoomare per vedere i meteoriti singolarmente;
  esplorare i dati senza rallentamenti;
È la versione più pratica se si vuole analizzare la caduta dei singoli meteoriti.

Lo script nella cartella “analisi con meteoriti singoli” crea comunque due mappe (marker singoli + heatmap), ma la mappa con i singoli marker non effettua alcun raggruppamento.
Il risultato è prevedibile:
  più di 45.000 marker da caricare;
  caricamento molto difficile o impossibile;
  blocco del browser appena si interagisce con la mappa;
Per questo motivo è sconsigliato utilizzare la mappa con i marker singoli.
