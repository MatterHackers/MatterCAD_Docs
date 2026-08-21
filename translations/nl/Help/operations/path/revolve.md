---
title: Wentelen
articleKey: RevolveObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: a63ebb08d982178e0e59f0b9f07c3c0dca53148b
source_lang: en
---
# Wentelen

Wentelen draait een 2D-pad rond een as om een 3D-omwentelingslichaam te maken. Zo maak je vazen, kommen, wielen en andere rotatiesymmetrische objecten.

<!--  Before and after showing a profile path being revolved into a vase shape -->
![20260506 102004 paste 20260506 102004](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-102004-paste-20260506-102004.jpg)


## Gebruik

1. Selecteer een 2D-pad
2. Pas **Wentelen** toe vanuit het menu met Pad-bewerkingen
3. Pas het rotatiebereik, de aspositie en het aantal zijden aan

## Parameters

- **Rotatie** - Totale rotatiehoek voor de wenteling (standaard: 0, bereik: 0-360). Stel in op 360 voor een volledige omwenteling.
- **Aspositie** - Verschuiving van de rotatieas ten opzichte van het midden van het pad (standaard: 0, bereik: -30 tot 30). Positief verplaatst de as weg van het pad, waardoor een grotere opening ontstaat.
- **Starthoek** - Waar de omwenteling begint (standaard: 0)
- **Eindhoek** - Waar de omwenteling eindigt (standaard: 45). Stel in op 360 voor een volledige omwenteling.
- **Zijden** - Aantal segmenten rond de omwenteling (standaard: 30). Meer = gladder oppervlak.

## Tips

- Gebruik Aspositie om de binnendiameter van de gewentelde vorm te bepalen
- Stel Starthoek en Eindhoek in op minder dan 360 om gedeeltelijke omwentelingen te maken (bogen, goten)
- Teken een profielpad van je vaas- of komvorm en wentel dit voor perfecte symmetrie
- Een gewenteld [Cirkelpad](../../2d-paths/circle-path.md) levert een torus op

## Gerelateerd

- [Lineaire extrusie](linear-extrude.md) - Recht omhoog extruderen in plaats van wentelen
- [2D-paden](../../2d-paths/index.md) - Maak profielpaden om te wentelen
- [Torus](../../primitives/torus.md) - Een kant-en-klare gewentelde ringvorm
