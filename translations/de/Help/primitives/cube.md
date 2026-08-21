---
title: Würfel
articleKey: CubeObject3D
parent: "Primitives"
nav_order: 4
source_hash: a376a9c78d88d995f3c6ce21dd5098672d6c1dfb
source_lang: en
---
# Würfel

Eine rechteckige Kastenform mit einstellbarer Breite, Tiefe, Höhe und optional abgerundeten Kanten. Der Würfel ist eines der am häufigsten verwendeten Grundobjekte beim Erstellen von Konstruktionen.

<!--  Screenshot of a Cube primitive on the workspace -->
![20260318 183230 paste 20260318 183230](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183230-paste-20260318-183230.jpg)


## Parameter

- **Breite** - Größe entlang der X-Achse (Standard: 20mm)
- **Tiefe** - Größe entlang der Y-Achse (Standard: 20mm)
- **Höhe** - Größe entlang der Z-Achse (Standard: 20mm)
- **Rund** - Abgerundete Kanten aktivieren
- **Radius** - Größe der Abrundung (sichtbar, wenn Rund aktiviert ist)
- **Rundungssegmente** - Glattheit der Abrundung, mehr Segmente = weichere Kurven (sichtbar, wenn Rund aktiviert ist)

## Tipps

- Verwenden Sie einen Würfel als Ausgangspunkt für Kästen, Platten, Halterungen und Gehäuse
- Aktivieren Sie Rund für glatte, professionell wirkende Kanten
- Der Radius darf die Hälfte der kleinsten Abmessung nicht überschreiten
- Vereinen Sie einen Würfel mit [Subtrahieren](../operations/boolean/subtract.md), um rechteckige Aussparungen und Schlitze zu erzeugen

## Verwandt

- [Zylinder](cylinder.md) - Runde Säulenform
- [Pyramide](pyramid.md) - Sich verjüngende, vierseitige Form
- [Loch](hole.md) - Ein Würfel, der für die boolesche Subtraktion vorkonfiguriert ist
