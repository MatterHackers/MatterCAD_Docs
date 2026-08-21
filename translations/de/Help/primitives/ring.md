---
title: Ring
articleKey: RingObject3D
parent: "Primitives"
nav_order: 13
source_hash: fd16c400f3d8c8af13416ab57ddd8407e761d93a
source_lang: en
---
# Ring

Ein hohler Zylinder (Rohr) mit unabhängigem Innen- und Außendurchmesser sowie einer festgelegten Höhe. Auch als Rohr- oder Schlauchform bekannt.

<!--  Screenshot of a Ring primitive on the workspace -->
![20260318 183848 paste 20260318 183848](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183848-paste-20260318-183848.jpg)


## Parameter

- **Außendurchmesser** - Die äußere Breite des Rings (Standard: 20mm)
- **Innendurchmesser** - Der Durchmesser der hohlen Mitte (Standard: 15mm)
- **Höhe** - Wie hoch der Ring ist (Standard: 5mm)
- **Seiten** - Anzahl der Segmente entlang des Umfangs (Standard: 40)

### Erweiterte Parameter

Aktivieren Sie den Modus **Erweitert** für zusätzliche Einstellungen:

- **Startwinkel** - Winkel, bei dem der Ring beginnt (Standard: 0)
- **Endwinkel** - Winkel, bei dem der Ring endet (Standard: 360). Werte unter 360 ergeben einen Teilring
- **Rund** - Fügt den Kanten eine Rundung hinzu (Keine, Oben oder Unten)
- **Richtung** - Rundung zur inneren oder äußeren Kante hin (sichtbar, wenn Rund aktiviert ist)
- **Rundungssegmente** - Glattheit der Rundung (sichtbar, wenn Rund aktiviert ist)

## Tipps

- Die Wandstärke entspricht (Außendurchmesser - Innendurchmesser) / 2
- Verwenden Sie dies für Unterlegscheiben, Abstandshalter, Buchsen und rohrartige Elemente
- Wählen Sie eine große Höhe für Rohre oder eine geringe für flache Unterlegscheiben
- Verwenden Sie Startwinkel und Endwinkel für Teilringformen wie C-Clips

## Verwandte Themen

- [Torus](torus.md) - Ein donutförmiger Ring mit rundem Querschnitt
- [Zylinder](cylinder.md) - Eine massive runde Säule (ohne hohle Mitte)
