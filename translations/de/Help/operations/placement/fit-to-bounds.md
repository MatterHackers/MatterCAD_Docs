---
title: An Grenzen anpassen
articleKey: FitToBoundsObject3D_4
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: 91b9c917cb636f28403c291a4d56f22bf6758b70
source_lang: en
---
# An Grenzen anpassen

An Grenzen anpassen skaliert ein Objekt so, dass es in die angegebenen Maße für Breite, Tiefe und Höhe passt. Sie können steuern, wie das Objekt innerhalb der Zielgrenzen gestreckt und ausgerichtet wird.

<!--  Screenshot showing an object being fit to specific bounding dimensions -->
![20260506 154930 paste 20260506 154930](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154930-paste-20260506-154930.jpg)

## Verwendung

1. Wählen Sie ein Objekt aus
2. Wenden Sie die Operation **An Grenzen anpassen** aus dem Menü Platzierung an
3. Geben Sie die Zielmaße ein
4. Wählen Sie die Proportionssperre und das Streckverhalten

## Parameter

- **Proportionen sperren** – Wie die Proportionen eingeschränkt werden:
  - **Keine** – Jede Achse kann unabhängig eingestellt werden
  - **X & Y** – Breite und Tiefe sind aneinander gekoppelt
  - **X, Y & Z** – Gleichmäßige Skalierung auf allen Achsen
- **Breite** – Zielbreite (X-Dimension)
- **Tiefe** – Zieltiefe (Y-Dimension)
- **Höhe** – Zielhöhe (Z-Dimension)

### Wenn Proportionen sperren auf X & Y oder X, Y & Z steht

- **Strecken** – Wie das Objekt eingepasst wird:
  - **Innen** – Verkleinern, sodass das Objekt vollständig in die Grenzen passt (kann Lücken lassen)
  - **Erweitern** – Vergrößern, um die Grenzen auszufüllen (kann in einigen Dimensionen überstehen)

### Wenn Proportionen sperren auf Keine steht

Jede Achse hat ihre eigenen Einstellungen:

- **Strecken** – Innen oder Erweitern pro Achse
- **Ausrichten** – Wo innerhalb der Grenzen positioniert wird (Min, Mitte, Max)

## Tipps

- Verwenden Sie dies, um importierte Modelle auf exakte Zielmaße zu bringen
- Sperren Sie alle Proportionen für eine gleichmäßige Skalierung, die die ursprüngliche Form beibehält
- Nutzen Sie die Steuerung pro Achse, wenn Sie eine bestimmte Breite einhalten müssen, die übrigen Dimensionen aber unwichtig sind

## Verwandte Themen

- [Skalieren](../transform/scale.md) – Nach Verhältnis oder Prozentwert statt auf eine Zielgröße skalieren
- [An Zylinder anpassen](fit-to-cylinder.md) – In eine zylindrische Begrenzung einpassen
- [Ausrichten](align.md) – Objekte relativ zueinander positionieren
