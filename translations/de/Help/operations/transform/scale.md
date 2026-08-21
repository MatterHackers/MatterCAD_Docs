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

Mit Skalieren ändern Sie die Größe eines Objekts mit präziser Kontrolle über Abmessungen, Proportionen und Einheitenumrechnung. Sie können gleichmäßig skalieren, bestimmte Achsen aneinander koppeln oder jede Achse unabhängig anpassen.

<!--  Screenshot showing the Scale operation properties with dimension fields and lock proportion options -->
![20260506 160759 paste 20260506 160759](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160759-paste-20260506-160759.jpg)

## Anwendung

1. Wählen Sie ein Objekt aus
2. Wenden Sie die Operation **Skalieren** aus dem Menü Transformieren an
3. Wählen Sie die gewünschte Skalierungsmethode und geben Sie die gewünschten Werte ein

Sie können Objekte auch direkt im Ansichtsfenster skalieren, indem Sie die Skalierungsanfasser an den Ecken eines ausgewählten Objekts anklicken und ziehen.

## Parameter

### Skalierungstyp

Wählen Sie eine Voreinstellung oder eine benutzerdefinierte Skalierung:

- **Benutzerdefiniert** – Eigene Abmessungen oder Prozentwerte eingeben
- **Zoll zu mm** – Multiplikation mit 25,4 (imperiale in metrische Einheiten umrechnen)
- **mm zu Zoll** – Multiplikation mit 0,0393 (metrische in imperiale Einheiten umrechnen)
- **mm zu cm** – Multiplikation mit 0,1
- **cm zu mm** – Multiplikation mit 10

### Skalierungsmethode (Modus Benutzerdefiniert)

- **Direkt** – Geben Sie die gewünschte Breite, Tiefe und Höhe in Millimetern ein
- **Prozentual** – Geben Sie Breite, Tiefe und Höhe als Prozentwerte der ursprünglichen Größe ein

### Proportionen sperren

- **Keine (frei skalieren)** – Jede Achse wird unabhängig skaliert
- **X & Y** – Breite und Tiefe sind aneinander gekoppelt; die Höhe wird unabhängig skaliert
- **X, Y & Z** – Alle drei Achsen werden gleichmäßig zusammen skaliert

### Abmessungen

- **Breite** – Größe entlang der X-Achse
- **Tiefe** – Größe entlang der Y-Achse
- **Höhe** – Größe entlang der Z-Achse

## Tipps

- Verwenden Sie „Zoll zu mm“, wenn Sie eine STL-Datei importiert haben, die in Zoll konstruiert wurde und zu klein erscheint
- Setzen Sie Proportionen sperren auf X, Y & Z für eine gleichmäßige Skalierung – die Änderung einer Abmessung aktualisiert alle übrigen
- Die Basisposition des Objekts bleibt beim Skalieren erhalten, sodass es auf der Arbeitsfläche stehen bleibt
- Sie können exakte Werte für präzise Größen eingeben oder die Schieberegler für schnelle Anpassungen verwenden

## Verwandte Themen

- [Verschieben](translate.md) – Ein Objekt bewegen
- [Drehen](rotate.md) – Ein Objekt rotieren
- [An Grenzen anpassen](../placement/fit-to-bounds.md) – Auf eine bestimmte Größe einpassen
