---
title: Sternpfad
articleKey: StarPathObject3D
parent: "2D Paths"
nav_order: 5
source_hash: 74d92e4171c452cd10069921636e45d7ef9dc70e
source_lang: en
---
# Sternpfad

Ein sternförmiger 2D-Pfad mit konfigurierbarer Anzahl von Zacken sowie Innen- und Außenradius. Verwenden Sie ihn zusammen mit [Linear Extrude](../operations/path/linear-extrude.md), um dreidimensionale Sternformen zu erzeugen.

<!-- Screenshot of a Star Path on the workspace -->
![20260506 080319 paste 20260506 080319](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080319-paste-20260506-080319.jpg)


## Parameter

- **Points** – Anzahl der Sternzacken
- **Outer Radius** – Abstand vom Mittelpunkt zur Spitze jeder Zacke
- **Inner Radius** – Abstand vom Mittelpunkt zu den Tälern zwischen den Zacken

## Tipps

- Das Verhältnis zwischen Inner Radius und Outer Radius bestimmt, wie „spitz“ der Stern ist. Ein kleiner Inner Radius erzeugt scharfe, ausgeprägte Zacken.
- Setzen Sie Points auf 5 für einen klassischen Stern, auf 6 für einen Davidstern oder auf höhere Werte für zahnradähnliche Formen
- Verwenden Sie [Smooth Path](../operations/path/smooth-path.md) auf einem Sternpfad, um abgerundete Sternformen zu erzeugen

## Verwandte Themen

- [Circle Path](circle-path.md) – Ein glatter Kreis
- [Gear 2D](../mechanical/gear-2d.md) – Ein echtes Zahnradprofil
- [Linear Extrude](../operations/path/linear-extrude.md) – Verleiht Pfaden Höhe
