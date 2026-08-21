---
title: Riduci
articleKey: DecimateObject3D
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 58a2573b968808e98203832142fa8bacf7a9cf99
source_lang: en
---
# Riduci (Decimazione)

Riduci abbassa il numero di poligoni di una mesh preservandone la forma complessiva. È utile per semplificare modelli molto dettagliati, ridurre le dimensioni del file e velocizzare le operazioni su geometrie complesse.

![20260324 080430 paste 20260324 080430](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080430-paste-20260324-080430.jpg)


## Come si usa

1. Seleziona un oggetto
2. Applica l'operazione **Riduci** dal menu Mesh
3. Scegli il tuo obiettivo (quantità o percentuale) e regolalo

## Parametri

- **Modalità** - Scegli come specificare l'obiettivo:
  - **Percentuale** - Mantieni una percentuale dei poligoni originali (predefinito: 50%)
  - **Quantità** - Punta a un numero specifico di poligoni
- **Numero di poligoni di origine** - Numero originale di poligoni (sola lettura)
- **Percentuale target** - Percentuale di poligoni da mantenere (visibile in modalità Percentuale)
- **Numero target** - Numero esatto di poligoni da mantenere (visibile in modalità Quantità)
- **Quantità dopo riduzione percentuale** - Numero finale di poligoni dopo la riduzione percentuale (sola lettura)
- **Mantieni superficie** - Proietta i vertici sulla superficie originale per una maggiore precisione (più lento ma più fedele alla forma originale)

## Suggerimenti

- Una riduzione del 50% di solito preserva bene la qualità visiva
- Attiva Mantieni superficie quando la precisione conta più della velocità
- Ridurre il numero di poligoni velocizza le operazioni booleane sui modelli importati complessi
- Un numero di poligoni molto basso degrada visibilmente la forma: controlla il risultato prima di confermare

## Correlati

- [Ripara](repair.md) - Correggi i problemi della mesh
