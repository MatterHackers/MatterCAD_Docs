---
title: Sfera
articleKey: SphereObject3D
parent: "Primitives"
nav_order: 14
source_hash: c227e98ac116c3481bb2af73c55801de84e70b1e
source_lang: en
---
# Sfera

Una forma sferica con diametro e livello di dettaglio regolabili.

<!--  Screenshot of a Sphere primitive on the workspace -->
![20260318 183909 paste 20260318 183909](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183909-paste-20260318-183909.jpg)


## Parametri

- **Diametro** - La larghezza della sfera (predefinito: 20mm)
- **Lati** - Numero di segmenti lungo il perimetro (predefinito: 40). Più lati = superficie più liscia

### Parametri avanzati

Attiva la modalità **Avanzate** per ulteriori controlli:

- **Angolo iniziale** - Angolo in cui inizia la superficie della sfera (predefinito: 0)
- **Angolo finale** - Angolo in cui termina la superficie della sfera (predefinito: 360). Imposta un valore inferiore a 360 per ottenere sfere parziali
- **Lati di latitudine** - Numero di segmenti dall'alto verso il basso (predefinito: 30). Più segmenti = poli più lisci

## Suggerimenti

- Per la stampa 3D, 40 lati sono di solito sufficienti. Valori più alti creano superfici più lisce ma file più grandi
- Usa l'Angolo iniziale e l'Angolo finale per creare forme sferiche parziali come ciotole o cupole
- Combina con [Sottrai](../operations/boolean/subtract.md) per creare cavità sferiche

## Correlati

- [Semisfera](half-sphere.md) - Solo l'emisfero superiore
- [Toro](torus.md) - Una forma a ciambella
