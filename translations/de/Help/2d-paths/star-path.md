---
title: Stern-Pfad
articleKey: StarPathObject3D
parent: "2D Paths"
nav_order: 5
source_hash: 74d92e4171c452cd10069921636e45d7ef9dc70e
source_lang: en
---
# Stern-Pfad

Ein sternförmiger 2D-Pfad mit konfigurierbarer Anzahl von Punkten sowie Innen- und Außenradius. Verwenden Sie ihn zusammen mit [Linear extrudieren](../operations/path/linear-extrude.md), um 3D-Sternformen zu erstellen.

<!-- Screenshot of a Star Path on the workspace -->
![20260506 080319 paste 20260506 080319](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080319-paste-20260506-080319.jpg)


## Parameter

- **Punkte** - Anzahl der Sternzacken
- **Außenradius** - Abstand vom Mittelpunkt zur Spitze jeder Zacke
- **Innenradius** - Abstand vom Mittelpunkt zu den Tälern zwischen den Zacken

## Tipps

- Das Verhältnis zwischen Innen- und Außenradius bestimmt, wie „spitz“ der Stern ist. Ein kleiner Innenradius erzeugt scharfe, ausgeprägte Zacken.
- Setzen Sie Punkte auf 5 für einen klassischen Stern, auf 6 für einen Davidstern oder auf höhere Werte für zahnradähnliche Formen
- Verwenden Sie [Pfad glätten](../operations/path/smooth-path.md) auf einem Stern-Pfad, um abgerundete Sternformen zu erzeugen

## Verwandte Themen

- [Kreis-Pfad](circle-path.md) - Ein glatter Kreis
- [Zahnrad 2D](../mechanical/gear-2d.md) - Ein echtes Zahnradprofil
- [Linear extrudieren](../operations/path/linear-extrude.md) - Pfaden Höhe geben
