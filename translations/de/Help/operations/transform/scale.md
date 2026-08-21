---
title: Skalieren
articleKey: ScaleObject3D_3
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b3b5419c3db29550b2544bb6aca91ca3ce6fa715
source_lang: en
---
# Skalieren

Skalieren ändert die Größe eines Objekts mit präziser Kontrolle über Abmessungen, Proportionen und Einheitenumrechnung. Sie können gleichmäßig skalieren, bestimmte Achsen miteinander sperren oder jede Achse unabhängig verändern.

<!--  Screenshot showing the Scale operation properties with dimension fields and lock proportion options -->
![20260506 160759 paste 20260506 160759](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160759-paste-20260506-160759.jpg)

## Verwendung

1. Wählen Sie ein Objekt aus
2. Wenden Sie die Operation **Skalieren** aus dem Menü Transformieren an
3. Wählen Sie Ihre Skalierungsmethode und geben Sie die gewünschten Werte ein

Sie können Objekte auch im Ansichtsfenster skalieren, indem Sie die Skalierungsgriffe an den Ecken eines ausgewählten Objekts anklicken und ziehen.

## Parameter

### Skalierungstyp

Wählen Sie eine Voreinstellung oder eine benutzerdefinierte Skalierung:

- **Benutzerdefiniert** – Geben Sie eigene Abmessungen oder Prozentwerte ein
- **Zoll in mm** – Multiplikation mit 25,4 (Umrechnung von imperial in metrisch)
- **mm in Zoll** – Multiplikation mit 0,0393 (Umrechnung von metrisch in imperial)
- **mm in cm** – Multiplikation mit 0,1
- **cm in mm** – Multiplikation mit 10

### Skalierungsmethode (Modus Benutzerdefiniert)

- **Direkt** – Geben Sie die gewünschte Breite, Tiefe und Höhe in Millimetern ein
- **Prozentsatz** – Geben Sie Breite, Tiefe und Höhe als Prozentwerte der ursprünglichen Größe ein

### Proportionen sperren

- **Keine (Frei skalieren)** – Jede Achse wird unabhängig skaliert
- **X & Y** – Breite und Tiefe sind miteinander gesperrt; die Höhe wird unabhängig skaliert
- **X, Y & Z** – Alle drei Achsen werden gleichmäßig zusammen skaliert

### Abmessungen

- **Breite** – Größe entlang der X-Achse
- **Tiefe** – Größe entlang der Y-Achse
- **Höhe** – Größe entlang der Z-Achse

## Tipps

- Verwenden Sie „Zoll in mm“, wenn Sie eine STL-Datei importiert haben, die in Zoll konstruiert wurde und zu klein erscheint
- Setzen Sie Proportionen sperren auf X, Y & Z für eine gleichmäßige Skalierung – die Änderung einer Abmessung aktualisiert alle anderen
- Die Basisposition des Objekts bleibt beim Skalieren erhalten, sodass es auf der Arbeitsfläche stehen bleibt
- Sie können exakte Werte für präzise Größen eingeben oder die Schieberegler für schnelle Anpassungen verwenden

## Verwandte Themen

- [Verschieben](translate.md) – Ein Objekt verschieben
- [Drehen](rotate.md) – Ein Objekt drehen
- [An Grenzen anpassen](../placement/fit-to-bounds.md) – Auf eine bestimmte Größe skalieren
