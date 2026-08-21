---
title: Pfad aufblasen
articleKey: InflatePathObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: c0e11d3d24c5f832f797cde4d392e26a4694733d
source_lang: en
---
# Pfad aufblasen

Pfad aufblasen dehnt einen 2D-Pfad nach außen aus, sodass die Form größer wird, ihre Gesamtgestalt aber erhalten bleibt. Das entspricht einem gleichmäßigen Versatz aller Kanten.

<!--  Before and after showing a path inflated outward -->
![20260506 100652 paste 20260506 100652](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100652-paste-20260506-100652.jpg)


## Anwendung

1. Wählen Sie einen 2D-Pfad aus
2. Wenden Sie **Pfad aufblasen** aus dem Menü der Pfad-Operationen an
3. Passen Sie den Aufblas-Betrag an

## Eine offene Linie aufblasen

Mit Aufblasen machen Sie aus einer Linie eine Form. Deaktivieren Sie **Geschlossen** bei einem [Benutzerdefinierten Pfad](../../2d-paths/custom-path.md), um eine offene Linie zu zeichnen, und blasen Sie diese anschließend auf: Das Ergebnis ist ein gefülltes Band, das zu beiden Seiten der Linie so breit ist wie der eingestellte Betrag. Von da an lässt es sich wie jeder andere Pfad extrudieren.

**Stil** legt fest, wie die beiden Enden der Linie abgeschlossen und wie ihre Ecken verbunden werden:

- **Flach** schließt das Band an jedem Endpunkt gerade ab
- **Rund** fügt hinter jedem Endpunkt einen Halbkreis an
- **Scharf** fügt hinter jedem Endpunkt ein Quadrat an

Eine offene Linie hat kein Inneres, in das sie schrumpfen könnte, daher bliebe bei einem Betrag von null oder einem negativen Wert überhaupt nichts übrig. Wenn der Pfad *vollständig* offen ist, hebt Aufblasen den Wert auf eine kleine positive Zahl an und schreibt den angepassten Wert zurück in das Feld, damit Sie sehen, was passiert ist.

Ein Pfad, der offene und geschlossene Konturen mischt, wird nicht angepasst: Die geschlossenen Konturen schrumpfen wie gewohnt, die offenen entfallen einfach. Geschlossene Pfade schrumpfen bei negativen Werten weiterhin genau wie bisher.

## Tipps

- Verwenden Sie negative Werte, um den Pfad nach innen zu schrumpfen, statt ihn auszudehnen
- Aufblasen eignet sich gut, um Toleranzversätze um Formen herum zu erzeugen
- Kombinieren Sie es mit [Umrisspfad](outline-path.md), um Ränder mit bestimmten Breiten zu erstellen

## Verwandte Themen

- [Umrisspfad](outline-path.md) – Einen Umriss aus einem Pfad erstellen
- [Randpfad](border-path.md) – Einen Randversatz hinzufügen
- [Pfad glätten](smooth-path.md) – Die Ecken eines Pfads abrunden
