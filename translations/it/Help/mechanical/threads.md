---
title: Filetti
articleKey: ThreadsObject3D_2
parent: "Mechanical Parts"
nav_order: 3
source_hash: 7d881b3293a508e102d3a4b845cdfd4eb9c34fa8
source_lang: en
---
# Filetti

Crea filettature con diametro, passo e profilo del filetto configurabili. I filetti possono essere usati come bulloni/viti autonomi oppure sottratti da altri oggetti per creare fori filettati.

<!-- AUTO_IMAGE: type=from_thumbnail item=threads file=mechanical_threads -->
![mechanical_threads](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_threads.png)

## Come si usa

1. Aggiungi **Filetti** dagli strumenti Meccanico o dal pannello Primitive
2. Imposta il diametro, il passo e il numero di rotazioni
3. Facoltativamente attiva "Usa come foro" per creare fori filettati

## Parametri

### Utilizzo

- **Usa come foro** - Se attivo, i filetti vengono dimensionati con una tolleranza aggiuntiva per l'uso come foro sottratto (predefinito: disattivato)
- **Tolleranza** - Gioco aggiuntivo per l'accoppiamento quando viene usato come foro (predefinito: 0,2 mm, visibile quando Usa come foro è attivo)

### Attributi

- **Diametro** - Il diametro esterno della sezione filettata (predefinito: 10 mm)
- **Passo** - Distanza tra ogni giro di filetto (predefinito: 2 mm). Passo più piccolo = filetti più fini
- **Scala filetto** - Larghezza dei filetti come rapporto rispetto al passo (predefinito: 1.0, intervallo: 0.1-1.0)
- **Rotazioni** - Numero di giri completi del filetto (predefinito: 10)

### Geometria

- **Lati** - Numero di segmenti lungo il perimetro (predefinito: 40). Di più = più liscio

### Punte (estremità del filetto)

- **Scala punta** - Quanto rastremare le estremità del filetto (predefinito: 0, intervallo: 0-1). Imposta un valore superiore a 0 per creare un imbocco rastremato alle estremità
- **Angolo punta** - L'angolo lungo il quale rastremare le punte (predefinito: 90 gradi)

## Suggerimenti

- Per creare un foro filettato: attiva "Usa come foro", posiziona i filetti e usa [Sottrai](../operations/boolean/subtract.md) sul tuo oggetto
- Aggiungi una Tolleranza quando usi il filetto come foro per garantire che le parti stampate si accoppino correttamente
- Passi standard delle filettature metriche: M3=0,5 mm, M4=0,7 mm, M5=0,8 mm, M6=1,0 mm, M8=1,25 mm, M10=1,5 mm
- Usa Scala punta per creare un imbocco che faciliti l'avvitamento iniziale

## Correlati

- [Ingranaggio](gears.md) - Crea forme di ingranaggi meccanici
- [Cilindro](../primitives/cylinder.md) - Una semplice colonna cilindrica (senza filetti)
- [Sottrai](../operations/boolean/subtract.md) - Taglia i filetti da altri oggetti per creare fori
