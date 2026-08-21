---
title: Toro
articleKey: TorusObject3D
parent: "Primitives"
nav_order: 17
source_hash: aaec1652de4d6713bd01a707964cf4985d3fb5f6
source_lang: en
---
# Toro

Un anello a forma di ciambella con controllo indipendente sulla dimensione complessiva e sullo spessore della sezione trasversale dell'anello.

<!--  Screenshot of a Torus primitive on the workspace -->
![20260318 184240 paste 20260318 184240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184240-paste-20260318-184240.jpg)


## Parametri

- **Diametro esterno** - La larghezza complessiva del toro (predefinito: 20mm)
- **Diametro interno** - Il diametro del foro centrale (predefinito: 10mm)
- **Lati** - Numero di segmenti attorno all'anello principale (predefinito: 40)

### Parametri avanzati

Attiva la modalità **Avanzate** per ulteriori controlli:

- **Angolo iniziale** - Angolo in cui inizia il toro (predefinito: 0)
- **Angolo finale** - Angolo in cui termina il toro (predefinito: 360). Imposta un valore inferiore a 360 per ottenere un anello aperto o un arco
- **Lati anello** - Numero di segmenti attorno alla sezione trasversale dell'anello (predefinito: 15). Più elevato = profilo del tubo più liscio
- **Angolo di fase anello** - Ruota il profilo della sezione trasversale (predefinito: 0)

## Suggerimenti

- Lo spessore del tubo dell'anello è determinato dalla differenza tra Diametro esterno e Diametro interno
- Usa l'Angolo iniziale e l'Angolo finale per creare segmenti di anello aperti, archi o forme a C
- Utile per creare O-ring, maniglie, anelli decorativi e curve di tubazioni

## Correlati

- [Anello](ring.md) - Un cilindro cavo a pareti diritte (tubo)
- [Sfera](sphere.md) - Una forma sferica piena
- [Semisfera](half-sphere.md) - Una forma a cupola
