---
title: Radiale Einschnürung
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: 95ef5847767e5cfcdbae9df9aaa1cb1727da2f5e
source_lang: en
---
# Radiale Einschnürung

Die Radiale Einschnürung komprimiert ein Objekt von einem Mittelpunkt aus nach innen, mit einer anpassbaren Profilkurve. Im Gegensatz zur normalen [Einschnüren](pinch.md)-Operation, die von hinten nach vorne wirkt, komprimiert die Radiale Einschnürung symmetrisch um eine Mittelachse.

<!--  Before and after showing an object with radial pinch applied, creating a waisted shape -->
![20260506 155741 paste 20260506 155741](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155741-paste-20260506-155741.jpg)

## Verwendung

1. Wählen Sie ein Objekt aus
2. Wenden Sie die Operation **Radiale Einschnürung** aus dem Menü Umformen an
3. Bearbeiten Sie das Pfadprofil, um festzulegen, wie stark die Einschnürung auf jeder Höhe ausfällt
4. Passen Sie die Anzahl der Schnitte für die Glättung an

## Parameter

- **Pfad** – Ein Profilkurven-Editor, der die Stärke der Einschnürung auf jeder Höhenebene festlegt. Bearbeiten Sie die Kurve, um eigene Einschnürungsprofile zu erstellen
- **Schnitte** – Anzahl der horizontalen Schnitte für eine gleichmäßige Einschnürung, gleichmäßig über die Höhe des Teils verteilt. Mehr Schnitte = glattere Ergebnisse

### Erweiterte Parameter

- **Einschnürungstyp** – Richtung der Kompression:
  - **Radial** – Gleichmäßige Kompression von allen Seiten zur Mitte hin
  - **X-Achse** – Kompression nur entlang der X-Achse
  - **Y-Achse** – Kompression nur entlang der Y-Achse
- **Drehversatz** – Verschiebt den Mittelpunkt des Einschnürungseffekts

## Tipps

- Verwenden Sie den Pfad-Editor, um Sanduhr-, Flaschen- oder vasenähnliche Formen zu erzeugen
- Die Radiale Einschnürung eignet sich ideal, um organische, abgerundete Formen aus zylindrischen Objekten zu erstellen
- Erhöhen Sie die Anzahl der Schnitte für glattere Kurven, insbesondere bei engen Einschnürungsprofilen

## Verwandte Themen

- [Einschnüren](pinch.md) – Einfache Kompression von hinten nach vorne
- [Verdrehen](twist.md) – Spiralförmige Drehung entlang der Höhe
- [Kurve](curve.md) – Biegen in einen Bogen
