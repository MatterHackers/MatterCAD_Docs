---
title: Linear Extrude
articleKey: LinearExtrudeObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cdfdb9cfe4c3339e70a23ddfb2f5071b1e8c5557
source_lang: en
---
# Linear Extrude

Linear Extrude verleiht einem 2D-Pfad Höhe und verwandelt eine flache Form in einen 3D-Körper. Dies ist die wichtigste Methode, um Pfade in 3D-Objekte umzuwandeln.

<!--  Before and after showing a 2D star path extruded into a 3D star -->
![20260506 100726 paste 20260506 100726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100726-paste-20260506-100726.jpg)


## Anwendung

1. Wählen Sie einen 2D-Pfad oder ein pfadbasiertes Objekt aus
2. Wenden Sie **Linear Extrude** aus dem Menü der Pfadoperationen an
3. Legen Sie die gewünschte Höhe fest

## Parameter

- **Height** – Höhe der Extrusion (Standard: 5 mm, Bereich: 0,1–50 mm)
- **Bevel Top** – Fügt der Oberseite der Extrusion eine abgeschrägte (abgerundete) Kante hinzu (Standard: aus)

### Fasenparameter (sichtbar, wenn Bevel Top aktiviert ist)

- **Style** – Das Profil der Fase (scharf oder abgerundet)
- **Radius** – Wie weit sich die Fase erstreckt (Standard: 3 mm)
- **Segments** – Glattheit der Fasenkurve (Standard: 9)

## Tipps

- Dies funktioniert mit jedem 2D-Pfad: [Circle](../../2d-paths/circle-path.md), [Box](../../2d-paths/box-path.md), [Star](../../2d-paths/star-path.md), [SVG](../../primitives/svg-object.md) und [Custom](../../2d-paths/custom-path.md)-Pfade
- Aktivieren Sie Bevel Top für ein hochwertigeres, professionelleres Erscheinungsbild
- Wenn Sie einen Pfad um eine Achse rotieren lassen möchten, anstatt ihn gerade nach oben zu extrudieren, siehe [Revolve](revolve.md)

## Verwandte Themen

- [Revolve](revolve.md) – Einen Pfad um eine Achse rotieren lassen
- [2D-Pfade](../../2d-paths/index.md) – Verfügbare Pfadformen
- [Text](../../primitives/text.md) – Text wird automatisch extrudiert
