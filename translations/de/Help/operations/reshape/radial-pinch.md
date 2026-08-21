---
title: Radiale Einschnürung
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: 95ef5847767e5cfcdbae9df9aaa1cb1727da2f5e
source_lang: en
---
# Radiale Einschnürung

Die radiale Einschnürung staucht ein Objekt von einem Mittelpunkt aus nach innen – mit einer anpassbaren Profilkurve. Anders als die normale [Einschnürung](pinch.md), die von hinten nach vorne wirkt, staucht die radiale Einschnürung symmetrisch um eine Mittelachse.

<!--  Before and after showing an object with radial pinch applied, creating a waisted shape -->
![20260506 155741 paste 20260506 155741](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155741-paste-20260506-155741.jpg)

## Verwendung

1. Wählen Sie ein Objekt aus
2. Wenden Sie die Operation **Radiale Einschnürung** aus dem Menü „Umformen“ an
3. Bearbeiten Sie das Pfadprofil, um festzulegen, wie stark die Einschnürung auf jeder Höhe ausfällt
4. Passen Sie die Anzahl der Schnitte für ein glatteres Ergebnis an

## Parameter

- **Pfad** – Ein Profilkurven-Editor, der den Grad der Einschnürung auf jeder Höhenebene festlegt. Bearbeiten Sie die Kurve, um eigene Einschnürungsprofile zu erstellen
- **Schnitte** – Anzahl der horizontalen Schnitte für eine gleichmäßige Einschnürung, gleichmäßig über die Höhe des Bauteils verteilt. Mehr Schnitte = glattere Ergebnisse

### Erweiterte Parameter

- **Einschnürungstyp** – Richtung der Stauchung:
  - **Radial** – Gleichmäßige Stauchung von allen Seiten zur Mitte hin
  - **X-Achse** – Stauchung nur entlang der X-Achse
  - **Y-Achse** – Stauchung nur entlang der Y-Achse
- **Rotationsversatz** – Verschiebt den Mittelpunkt des Einschnürungseffekts

## Tipps

- Verwenden Sie den Pfad-Editor, um Sanduhr-, Flaschen- oder vasenartige Formen zu erzeugen
- Die radiale Einschnürung eignet sich ideal, um aus zylindrischen Objekten organische, abgerundete Formen zu erstellen
- Erhöhen Sie die Anzahl der Schnitte für glattere Kurven, insbesondere bei stark ausgeprägten Einschnürungsprofilen

## Verwandte Themen

- [Einschnürung](pinch.md) – Einfache Stauchung von hinten nach vorne
- [Verdrehung](twist.md) – Spiralförmige Drehung über die Höhe
- [Krümmung](curve.md) – Biegen zu einem Bogen
