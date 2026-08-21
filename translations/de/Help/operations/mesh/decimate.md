---
title: Reduzieren
articleKey: DecimateObject3D
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 58a2573b968808e98203832142fa8bacf7a9cf99
source_lang: en
---
# Reduzieren (Dezimieren)

Reduzieren verringert die Polygonanzahl eines Netzes und erhält dabei die Gesamtform. Das ist nützlich, um sehr detaillierte Modelle zu vereinfachen, die Dateigröße zu verringern und Operationen an komplexer Geometrie zu beschleunigen.

![20260324 080430 paste 20260324 080430](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080430-paste-20260324-080430.jpg)


## Verwendung

1. Wählen Sie ein Objekt aus
2. Wenden Sie die Operation **Reduzieren** aus dem Menü Netz an
3. Wählen Sie Ihr Ziel (Anzahl oder Prozentsatz) und passen Sie es an

## Parameter

- **Modus** - Legt fest, wie das Ziel angegeben wird:
  - **Prozent** - Einen Prozentsatz der ursprünglichen Polygone beibehalten (Standard: 50 %)
  - **Anzahl** - Eine bestimmte Polygonanzahl anstreben
- **Polygonanzahl der Quelle** - Ursprüngliche Anzahl der Polygone (schreibgeschützt)
- **Zielprozentsatz** - Prozentsatz der beizubehaltenden Polygone (sichtbar im Modus Prozent)
- **Zielanzahl** - Exakte Anzahl der beizubehaltenden Polygone (sichtbar im Modus Anzahl)
- **Anzahl nach prozentualer Reduzierung** - Endgültige Polygonanzahl nach der prozentualen Reduzierung (schreibgeschützt)
- **Oberfläche beibehalten** - Projiziert die Punkte zurück auf die ursprüngliche Oberfläche für höhere Genauigkeit (langsamer, aber näher an der ursprünglichen Form)

## Tipps

- Eine Reduzierung um 50 % erhält die visuelle Qualität in der Regel gut
- Aktivieren Sie Oberfläche beibehalten, wenn Genauigkeit wichtiger ist als Geschwindigkeit
- Eine geringere Polygonanzahl beschleunigt boolesche Operationen an komplexen importierten Modellen
- Sehr niedrige Polygonanzahlen verschlechtern die Form sichtbar -- prüfen Sie das Ergebnis, bevor Sie es übernehmen

## Verwandte Themen

- [Reparieren](repair.md) - Netzprobleme beheben
