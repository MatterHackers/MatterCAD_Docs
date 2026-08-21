---
title: Domande frequenti
nav_order: 101
source_hash: 929ea9e89d3f5008996615341418ba715d3f6075
source_lang: en
---
# Perché i miei oggetti hanno una scala errata?
- I file STL non memorizzano le informazioni sulle unità di misura. MatterCAD prevede dimensioni STL in millimetri, mentre la maggior parte dei software CAD esporta nelle proprie unità native (in genere pollici). Questo causa discrepanze di scala durante l'importazione dei progetti.

- La soluzione migliore è configurare il software di progettazione in modo che esporti i file STL in millimetri. Ad esempio, in SolidWorks, usa il pulsante Opzioni nella finestra di dialogo Salva con nome per impostare i parametri di esportazione STL.

- In alternativa, puoi ridimensionare il pezzo all'interno di MatterCAD. Nella Vista 3D, accedi alla modalità Modifica e seleziona SCALA dalla barra degli strumenti a destra. Usa il menu a discesa per i fattori di conversione più comuni oppure inserisci dimensioni specifiche nei campi degli assi.

# Come si cancellano i dati dell'applicazione?

- Se la reinstallazione non risolve un problema, potrebbe essere necessario eliminare i dati memorizzati da MatterCAD. Questi dati rimangono anche dopo la disinstallazione. Per ripristinare completamente le impostazioni predefinite, rimuovi la cartella dell'applicazione. Puoi anche rinominare temporaneamente il file di database SQLite (MatterCAD.db) per verificare se sono le impostazioni a causare problemi.
![20260318 194137 paste 20260318 194137](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194137-paste-20260318-194137.jpg)

![20260318 194200 paste 20260318 194200](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194200-paste-20260318-194200.jpg)

![20260318 194218 paste 20260318 194218](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-194218-paste-20260318-194218.jpg)


- Windows
  - La libreria utente e le impostazioni sono memorizzate in C:\Users\{user}\AppData\Local\MatterCAD.
