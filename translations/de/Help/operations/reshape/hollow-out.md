---
title: Aushöhlen
articleKey: HollowOutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cc2c5555723ecfe77475fef9e7a2090cdf760204
source_lang: en
---
# Aushöhlen

Aushöhlen erzeugt aus einem massiven Objekt eine hohle Schale, indem die Oberfläche nach innen versetzt wird. Das Ergebnis ist eine dünnwandige Version der ursprünglichen Form.

<!--  Cross-section view showing a solid object hollowed out with visible wall thickness -->
![20260506 155412 paste 20260506 155412](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155412-paste-20260506-155412.jpg)

## Verwendung

1. Wählen Sie ein massives Objekt aus
2. Wenden Sie die Operation **Aushöhlen** aus dem Menü Umformen an
3. Legen Sie die gewünschte Wandstärke fest

## Parameter

- **Abstand** – Die Wandstärke in Millimetern (Standard: 2 mm). So dick wird die resultierende Schale.
- **Anzahl Zellen** – Auflösung des Aushöhlungsalgorithmus (Standard: 64). Höhere Werte erzeugen glattere Innenflächen, benötigen jedoch mehr Rechenzeit.

## Tipps

- Aushöhlen eignet sich für Gehäuse, Behälter, Vasen und leichte Bauteile
- Eine Wandstärke von 1–2 mm ist für die meisten 3D-gedruckten Teile üblich
- Erhöhen Sie Anzahl Zellen, wenn die Innenfläche rau oder stufig wirkt
- Beim Aushöhlen entsteht ein offener Boden – kombinieren Sie es mit einem [Würfel](../../primitives/cube.md), wenn Sie eine geschlossene Grundfläche benötigen
- Bei komplexen Formen kann die Berechnung einige Sekunden dauern

## Verwandte Themen

- [Ebenenschnitt](plane-cut.md) – Ein Objekt auf einer bestimmten Höhe ausschneiden
- [Subtrahieren](../boolean/subtract.md) – Material manuell abtragen
