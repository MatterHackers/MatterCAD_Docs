---
title: Gewinde
articleKey: ThreadsObject3D_2
parent: "Mechanical Parts"
nav_order: 3
source_hash: 7d881b3293a508e102d3a4b845cdfd4eb9c34fa8
source_lang: en
---
# Gewinde

Erstellen Sie Schraubgewinde mit konfigurierbarem Durchmesser, Steigung und Gewindeprofil. Gewinde können als eigenständige Schrauben/Bolzen verwendet oder von anderen Objekten subtrahiert werden, um Gewindebohrungen zu erzeugen.

<!-- AUTO_IMAGE: type=from_thumbnail item=threads file=mechanical_threads -->
![mechanical_threads](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_threads.png)

## Verwendung

1. Fügen Sie **Gewinde** über die mechanischen Werkzeuge oder das Bedienfeld Grundkörper hinzu
2. Legen Sie Durchmesser, Steigung und Anzahl der Umdrehungen fest
3. Aktivieren Sie optional „Als Bohrung verwenden“, um Gewindebohrungen zu erstellen

## Parameter

### Verwendung

- **Als Bohrung verwenden** – Wenn aktiviert, wird das Gewinde mit zusätzlicher Toleranz für die Verwendung als subtrahierte Bohrung dimensioniert (Standard: aus)
- **Toleranz** – Zusätzliches Spiel für die Passung bei Verwendung als Bohrung (Standard: 0,2 mm, sichtbar, wenn „Als Bohrung verwenden“ aktiviert ist)

### Attribute

- **Durchmesser** – Der Außendurchmesser des Gewindeabschnitts (Standard: 10 mm)
- **Steigung** – Abstand zwischen den einzelnen Gewindegängen (Standard: 2 mm). Kleinere Steigung = feineres Gewinde
- **Gewindeskalierung** – Breite der Gewindegänge als Verhältnis zur Steigung (Standard: 1,0, Bereich: 0,1–1,0)
- **Umdrehungen** – Anzahl der vollständigen Gewindegänge (Standard: 10)

### Geometrie

- **Seiten** – Anzahl der Segmente entlang des Umfangs (Standard: 40). Mehr = glatter

### Spitzen (Gewindeenden)

- **Spitzenskalierung** – Wie stark die Gewindeenden verjüngt werden (Standard: 0, Bereich: 0–1). Werte über 0 erzeugen einen verjüngten Einlauf an den Enden
- **Spitzenwinkel** – Der Winkel, über den die Enden verjüngt werden (Standard: 90 Grad)

## Tipps

- So erstellen Sie eine Gewindebohrung: Aktivieren Sie „Als Bohrung verwenden“, positionieren Sie das Gewinde und [subtrahieren](../operations/boolean/subtract.md) Sie es von Ihrem Objekt
- Fügen Sie bei Verwendung als Bohrung eine Toleranz hinzu, damit die gedruckten Teile zusammenpassen
- Standard-Steigungen für metrische Gewinde: M3=0,5 mm, M4=0,7 mm, M5=0,8 mm, M6=1,0 mm, M8=1,25 mm, M10=1,5 mm
- Verwenden Sie die Spitzenskalierung, um einen Einlauf zu erzeugen, der das Ansetzen des Gewindes erleichtert

## Verwandte Themen

- [Zahnräder](gears.md) – Mechanische Zahnradformen erstellen
- [Zylinder](../primitives/cylinder.md) – Eine einfache runde Säule (ohne Gewinde)
- [Subtrahieren](../operations/boolean/subtract.md) – Gewinde aus anderen Objekten ausschneiden, um Bohrungen zu erzeugen
