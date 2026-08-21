---
title: Novità
nav_order: 105
source_hash: 172343b8320204d2b0ec52419324f0efd2be95a1
source_lang: en
---
# MatterCAD 2.2026.8

# Novità

* **Modifica figli**
  * Fai doppio clic su un oggetto qualsiasi per entrarci e modificare le parti che lo compongono, direttamente sul piano
  * Un percorso di navigazione mostra dove ti trovi — fai clic su un livello qualsiasi per richiudere le tue modifiche
  * ![MatterCAD 2.2026.8](https://www.matterhackers.com/r/qgG4VA)

* **Un unico utensile booleano**
  * Combina, Sottrai, Interseca e Sottrai e Sostituisci sono ora un'unica operazione — cambia modalità con un clic invece di eliminare e riapplicare
  <!-- Boolean property panel showing the four-icon operation row with Subtract selected. ~500x350px -->
  * ![One Boolean Tool](https://matterhackers.github.io/MatterCAD_Docs/assets/20260810-181041-paste-20260810-181041.jpg)

* **Operazioni booleane che funzionano e basta**
  * Un nuovo motore è più veloce e riesce anche con mesh che prima fallivano
  * Combina ripara automaticamente le parti con fori e indica il nome di ciò che non è riuscito a unire; Taglio con piano ora produce un solido stagno e stampabile

* **Modifica dei percorsi 2D migliorata**
  * Modalità dei punti, simmetria Specchia in tempo reale, aggancio alla griglia, selezione con trascinamento ed Esc per annullare un trascinamento
  <!-- Turn on Mirror, drag a point and watch its partner follow, then drag it onto the axis to merge. ~700x450px -->
  * ![Path Edit](https://www.matterhackers.com/r/yQwWXB)

## Miglioramenti

* **Navigazione** — Premi Z con un percorso 2D selezionato per una vista di modifica dall'alto
* **Testo più nitido** — Il rendering del testo sub-pixel è ora attivo automaticamente quando il display lo supporta
* **Modellazione** — Estrusione lineare può smussare il bordo inferiore con stile, raggio e numero di segmenti propri

## Principali correzioni di bug

* **Affidabilità del salvataggio** — Un salvataggio non riuscito non può più danneggiare il file che stava sostituendo e segnala l'errore
* **Libreria cloud** — Salvando su disco un elemento del cloud ne viene mantenuto il nome della scheda, e la scheda sopravvive a un riavvio
* **Caricamento dei file** — Corretto il problema per cui le parti 3MF venivano scartate silenziosamente durante il caricamento
* **Modifica dei percorsi** — Corretto un arresto anomalo durante l'eliminazione di un punto di curva e il ripristino della modalità scelta da parte dei punti di giunzione
* **Attività in background** — Il pulsante Arresta di un'attività in esecuzione ora è cliccabile e annulla davvero l'operazione

## Puoi consultare le note di rilascio complete [Qui](release-notes.md).
