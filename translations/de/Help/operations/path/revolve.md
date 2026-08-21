---
title: Rotieren
articleKey: RevolveObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: a63ebb08d982178e0e59f0b9f07c3c0dca53148b
source_lang: en
---
# Rotieren

Rotieren dreht einen 2D-Pfad um eine Achse und erzeugt so einen 3D-Rotationskörper. Auf diese Weise erstellen Sie Vasen, Schalen, Räder und andere rotationssymmetrische Objekte.

<!--  Before and after showing a profile path being revolved into a vase shape -->
![20260506 102004 paste 20260506 102004](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-102004-paste-20260506-102004.jpg)


## Verwendung

1. Wählen Sie einen 2D-Pfad aus
2. Wenden Sie **Rotieren** aus dem Menü der Pfad-Operationen an
3. Passen Sie den Drehbereich, die Achsenposition und die Anzahl der Seiten an

## Parameter

- **Drehung** – Gesamter Drehwinkel für die Rotation (Standard: 0, Bereich: 0–360). Setzen Sie den Wert auf 360 für eine vollständige Umdrehung.
- **Achsenposition** – Versatz der Drehachse gegenüber der Pfadmitte (Standard: 0, Bereich: -30 bis 30). Positive Werte verschieben die Achse vom Pfad weg und erzeugen eine größere Öffnung.
- **Startwinkel** – Wo die Rotation beginnt (Standard: 0)
- **Endwinkel** – Wo die Rotation endet (Standard: 45). Setzen Sie den Wert auf 360 für eine vollständige Umdrehung.
- **Seiten** – Anzahl der Segmente entlang der Rotation (Standard: 30). Mehr = glattere Oberfläche.

## Tipps

- Steuern Sie mit der Achsenposition den Innendurchmesser der rotierten Form
- Setzen Sie Startwinkel und Endwinkel auf weniger als 360, um Teilrotationen zu erzeugen (Bögen, Rinnen)
- Zeichnen Sie einen Profilpfad Ihrer Vasen- oder Schalenform und rotieren Sie ihn anschließend für perfekte Symmetrie
- Ein rotierter [Kreis-Pfad](../../2d-paths/circle-path.md) ergibt einen Torus

## Verwandte Themen

- [Linear extrudieren](linear-extrude.md) – Gerade nach oben extrudieren statt zu rotieren
- [2D-Pfade](../../2d-paths/index.md) – Profilpfade zum Rotieren erstellen
- [Torus](../../primitives/torus.md) – Eine fertige rotierte Ringform
