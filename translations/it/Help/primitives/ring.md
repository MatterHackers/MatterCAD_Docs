---
title: Anello
articleKey: RingObject3D
parent: "Primitives"
nav_order: 13
source_hash: fd16c400f3d8c8af13416ab57ddd8407e761d93a
source_lang: en
---
# Anello

Un cilindro cavo (tubo) con diametri interno ed esterno indipendenti e un'altezza specificata. Noto anche come forma a tubo o condotto.

<!--  Screenshot of a Ring primitive on the workspace -->
![20260318 183848 paste 20260318 183848](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183848-paste-20260318-183848.jpg)


## Parametri

- **Diametro esterno** - La larghezza esterna dell'anello (predefinito: 20mm)
- **Diametro interno** - Il diametro del centro cavo (predefinito: 15mm)
- **Altezza** - Quanto è alto l'anello (predefinito: 5mm)
- **Lati** - Numero di segmenti attorno al perimetro (predefinito: 40)

### Parametri avanzati

Attiva la modalità **Avanzate** per ulteriori controlli:

- **Angolo iniziale** - Angolo in cui inizia l'anello (predefinito: 0)
- **Angolo finale** - Angolo in cui termina l'anello (predefinito: 360). Imposta un valore inferiore a 360 per un anello parziale
- **Arrotonda** - Aggiunge l'arrotondamento ai bordi (Nessuno, Su o Giù)
- **Direzione** - Arrotonda verso il bordo interno o esterno (visibile quando Arrotonda è attivo)
- **Segmenti arrotondamento** - Levigatezza dell'arrotondamento (visibile quando Arrotonda è attivo)

## Suggerimenti

- Lo spessore della parete è pari a (Diametro esterno - Diametro interno) / 2
- Usalo per rondelle, distanziali, boccole e caratteristiche a forma di tubo
- Imposta un'altezza elevata per i tubi o ridotta per rondelle piatte
- Usa l'Angolo iniziale e l'Angolo finale per forme ad anello parziale come le clip a C

## Correlati

- [Torus](torus.md) - Un anello a forma di ciambella con sezione trasversale circolare
- [Cilindro](cylinder.md) - Una colonna circolare piena (senza centro cavo)
