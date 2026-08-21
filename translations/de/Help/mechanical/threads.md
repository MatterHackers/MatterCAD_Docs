---
title: Gewindegänge
articleKey: ThreadsObject3D_2
parent: "Mechanical Parts"
nav_order: 3
source_hash: 7d881b3293a508e102d3a4b845cdfd4eb9c34fa8
source_lang: en
---
# Gewindegänge

Erstellen Sie Schraubengewinde mit konfigurierbarem Durchmesser, konfigurierbarer Steigung und Gewindeprofil. Gewindegänge können als eigenständige Bolzen/Schrauben verwendet oder von anderen Objekten subtrahiert werden, um Gewindelöcher zu erzeugen.

<!-- AUTO_IMAGE: type=from_thumbnail item=threads file=mechanical_threads -->
![mechanical_threads](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_threads.png)

## Verwendung

1. Fügen Sie **Gewindegänge** über die Werkzeuge unter Mechanisch oder das Bedienfeld Primitive hinzu
2. Legen Sie Durchmesser, Steigung und die Anzahl der Drehungen fest
3. Aktivieren Sie optional „Als Loch verwenden“, um Gewindelöcher zu erzeugen

## Parameter

### Verwendung

- **Als Loch verwenden** – Wenn aktiviert, werden die Gewindegänge mit zusätzlicher Toleranz für die Verwendung als subtrahiertes Loch dimensioniert (Standard: aus)
- **Toleranz** – Zusätzliches Spiel für die Passung bei Verwendung als Loch (Standard: 0,2 mm, sichtbar, wenn Als Loch verwenden aktiviert ist)

### Attribute

- **Durchmesser** – Der Außendurchmesser des Gewindeabschnitts (Standard: 10 mm)
- **Steigung** – Abstand zwischen den einzelnen Gewindegängen (Standard: 2 mm). Kleinere Steigung = feineres Gewinde
- **Gewindeskalierung** – Breite der Gewindegänge im Verhältnis zur Steigung (Standard: 1,0, Bereich: 0,1–1,0)
- **Drehungen** – Anzahl der vollständigen Gewindeumdrehungen (Standard: 10)

### Geometrie

- **Seiten** – Anzahl der Segmente entlang des Umfangs (Standard: 40). Mehr = glatter

### Spitzen (Gewindeenden)

- **Spitzenskalierung** – Wie stark die Gewindeenden verjüngt werden (Standard: 0, Bereich: 0–1). Werte über 0 erzeugen einen verjüngten Einlauf an den Enden
- **Spitzenwinkel** – Der Winkel, über den die Spitzen verjüngt werden (Standard: 90 Grad)

## Tipps

- So erstellen Sie ein Gewindeloch: Aktivieren Sie „Als Loch verwenden“, positionieren Sie die Gewindegänge und wenden Sie [Subtrahieren](../operations/boolean/subtract.md) auf Ihr Objekt an
- Fügen Sie bei Verwendung als Loch eine Toleranz hinzu, damit die gedruckten Teile zusammenpassen
- Standard-Steigungen für metrische Gewinde: M3=0,5 mm, M4=0,7 mm, M5=0,8 mm, M6=1,0 mm, M8=1,25 mm, M10=1,5 mm
- Verwenden Sie die Spitzenskalierung, um einen Einlauf zu erzeugen, der das Ansetzen des Gewindes erleichtert

## Verwandte Themen

- [Zahnräder](gears.md) – Mechanische Zahnradformen erstellen
- [Zylinder](../primitives/cylinder.md) – Eine einfache runde Säule (ohne Gewinde)
- [Subtrahieren](../operations/boolean/subtract.md) – Gewindegänge aus anderen Objekten ausschneiden, um Löcher zu erzeugen
