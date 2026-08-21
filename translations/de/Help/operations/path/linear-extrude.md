---
title: Linear extrudieren
articleKey: LinearExtrudeObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cdfdb9cfe4c3339e70a23ddfb2f5071b1e8c5557
source_lang: en
---
# Linear extrudieren

Linear extrudieren verleiht einem 2D-Pfad Höhe und verwandelt so eine flache Form in einen 3D-Körper. Dies ist die wichtigste Methode, um Pfade in 3D-Objekte umzuwandeln.

<!--  Before and after showing a 2D star path extruded into a 3D star -->
![20260506 100726 paste 20260506 100726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100726-paste-20260506-100726.jpg)


## Verwendung

1. Wählen Sie einen 2D-Pfad oder ein pfadbasiertes Objekt aus
2. Wenden Sie **Linear extrudieren** aus dem Menü der Pfad-Operationen an
3. Legen Sie die gewünschte Höhe fest

## Parameter

- **Höhe** - Wie hoch die Extrusion ist (Standard: 5 mm, Bereich: 0,1-50 mm)
- **Fase oben** - Fügt der Oberseite der Extrusion eine abgeschrägte (abgerundete) Kante hinzu (Standard: aus)

### Fasen-Parameter (sichtbar, wenn Fase oben aktiviert ist)

- **Stil** - Das Profil der Fase (Scharf oder abgerundet)
- **Radius** - Wie weit sich die Fase erstreckt (Standard: 3 mm)
- **Segmente** - Glattheit der Fasenkurve (Standard: 9)

## Tipps

- Dies funktioniert mit jedem 2D-Pfad: [Kreis](../../2d-paths/circle-path.md), [Box](../../2d-paths/box-path.md), [Stern](../../2d-paths/star-path.md), [SVG](../../primitives/svg-object.md) und [Benutzerdefiniert](../../2d-paths/custom-path.md)-Pfaden
- Aktivieren Sie Fase oben für ein feineres, professionelleres Aussehen
- Um einen Pfad um eine Achse zu drehen, anstatt ihn gerade nach oben zu extrudieren, siehe [Rotieren](revolve.md)

## Verwandte Themen

- [Rotieren](revolve.md) - Einen Pfad um eine Achse drehen
- [2D-Pfade](../../2d-paths/index.md) - Verfügbare Pfadformen
- [Text](../../primitives/text.md) - Text wird automatisch extrudiert
