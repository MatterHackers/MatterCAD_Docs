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

Bild zu Pfad zeichnet die Umrisse eines Bildes nach, um 2D-Pfade zu erzeugen. Diese Pfade können anschließend extrudiert, rotiert oder mit jeder anderen Pfadoperation verwendet werden. Das eignet sich ideal, um Logos, Silhouetten und einfache Grafiken in 3D-Objekte umzuwandeln.

![20260324 075521 paste 20260324 075521](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-075521-paste-20260324-075521.jpg)


## Anwendung

1. Wählen Sie ein Bildobjekt in Ihrem Arbeitsbereich aus
2. Wenden Sie **Bild zu Pfad** aus dem Menü der Bild-Operationen an
3. Wählen Sie den Analysetyp und passen Sie den Auswahlbereich an

## Parameter

- **Analysetyp** - Wie das Bild für das Nachzeichnen analysiert wird:
  - **Transparenz** - Nachzeichnen anhand transparenter und deckender Bereiche (am besten für PNGs mit transparentem Hintergrund)
  - **Farben** - Nachzeichnen anhand von Farbbereichen
  - **Intensität** - Nachzeichnen anhand von Helligkeitswerten (am besten für die meisten Bilder)
- **Bereich auswählen** - Ein Histogramm-Regler zur Auswahl der Helligkeits-/Farbwerte, die in das Nachzeichnen einbezogen werden
- **Min. Oberfläche** - Mindestfläche, damit eine Pfadschleife berücksichtigt wird. Erhöhen Sie den Wert, um kleine Störartefakte herauszufiltern

## Tipps

- Saubere, kontrastreiche Bilder mit einfachen Formen funktionieren am besten
- Verwenden Sie den Modus Transparenz für PNG-Bilder mit transparentem Hintergrund
- Verwenden Sie den Modus Intensität für Fotografien und Bilder ohne Transparenz
- Wenden Sie nach dem Nachzeichnen [Linear extrudieren](../path/linear-extrude.md) an, um dem Pfad Höhe zu geben
- Erhöhen Sie Min. Oberfläche, um kleine unerwünschte Details aus dem Nachzeichnen zu entfernen

## Verwandte Themen

- [Bildkonverter](image-converter.md) - Erzeugt ein Höhenkarten-Relief anstelle flacher Pfade
- [Lithophanie](lithophane.md) - Erzeugt hinterleuchtete Bilddarstellungen
- [SVG-Objekt](../../primitives/svg-object.md) - Vektorgrafiken direkt importieren (kein Nachzeichnen nötig)
- [Linear extrudieren](../path/linear-extrude.md) - Gibt dem nachgezeichneten Pfad Höhe
