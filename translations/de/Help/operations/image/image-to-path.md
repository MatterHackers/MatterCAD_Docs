---
title: Bild zu Pfad
articleKey: ImageToPathObject3D_2
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 0145587f635ede68bfc1df37b4f0d366a03d3a6c
source_lang: en
---
# Bild zu Pfad

„Bild zu Pfad“ verfolgt die Umrisse eines Bildes und erzeugt daraus 2D-Pfade. Diese Pfade lassen sich anschließend extrudieren, rotieren oder mit jeder anderen Pfadoperation weiterverarbeiten. Ideal, um Logos, Silhouetten und einfache Grafiken in 3D-Objekte umzuwandeln.

![20260324 075521 paste 20260324 075521](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-075521-paste-20260324-075521.jpg)


## Anwendung

1. Wählen Sie ein Bildobjekt in Ihrem Arbeitsbereich aus
2. Wenden Sie **Bild zu Pfad** aus dem Menü der Bildoperationen an
3. Wählen Sie den Analysetyp und passen Sie den Auswahlbereich an

## Parameter

- **Analysetyp** – Legt fest, wie das Bild für die Nachverfolgung analysiert wird:
  - **Transparenz** – Nachverfolgung anhand transparenter und deckender Bereiche (am besten für PNGs mit transparentem Hintergrund)
  - **Farben** – Nachverfolgung anhand von Farbbereichen
  - **Intensität** – Nachverfolgung anhand von Helligkeitsstufen (am besten für die meisten Bilder)
- **Bereich auswählen** – Ein Histogramm-Regler, mit dem Sie festlegen, welche Helligkeits- bzw. Farbwerte in die Nachverfolgung einbezogen werden
- **Min. Fläche** – Mindestfläche, damit eine Pfadschleife übernommen wird. Erhöhen Sie den Wert, um kleine Störartefakte herauszufiltern

## Tipps

- Am besten eignen sich klare, kontrastreiche Bilder mit einfachen Formen
- Verwenden Sie den Modus „Transparenz“ für PNG-Bilder mit transparentem Hintergrund
- Verwenden Sie den Modus „Intensität“ für Fotografien und Bilder ohne Transparenz
- Wenden Sie nach der Nachverfolgung [Lineare Extrusion](../path/linear-extrude.md) an, um dem Pfad Höhe zu geben
- Erhöhen Sie „Min. Fläche“, um kleine unerwünschte Details aus der Nachverfolgung zu entfernen

## Verwandte Themen

- [Bildkonverter](image-converter.md) – Erzeugt ein Höhenrelief anstelle flacher Pfade
- [Lithophanie](lithophane.md) – Erzeugt hinterleuchtete Bilddarstellungen
- [SVG-Objekt](../../primitives/svg-object.md) – Vektorgrafiken direkt importieren (keine Nachverfolgung nötig)
- [Lineare Extrusion](../path/linear-extrude.md) – Gibt dem nachverfolgten Pfad Höhe
