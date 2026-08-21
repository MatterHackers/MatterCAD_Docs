---
title: Ring
articleKey: RingObject3D
parent: "Primitives"
nav_order: 13
source_hash: fd16c400f3d8c8af13416ab57ddd8407e761d93a
source_lang: en
---
# Ring

Ein hohler Zylinder (Rohr) mit unabhängigem Innen- und Außendurchmesser und einer festgelegten Höhe. Auch als Rohr- oder Schlauchform bekannt.

<!--  Screenshot of a Ring primitive on the workspace -->
![20260318 183848 paste 20260318 183848](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183848-paste-20260318-183848.jpg)


## Parameter

- **Außendurchmesser** – Die Außenbreite des Rings (Standard: 20 mm)
- **Innendurchmesser** – Der Durchmesser der hohlen Mitte (Standard: 15 mm)
- **Höhe** – Wie hoch der Ring ist (Standard: 5 mm)
- **Seiten** – Anzahl der Segmente entlang des Umfangs (Standard: 40)

### Erweiterte Parameter

Aktivieren Sie den Modus **Erweitert** für zusätzliche Einstellungen:

- **Startwinkel** – Winkel, bei dem der Ring beginnt (Standard: 0)
- **Endwinkel** – Winkel, bei dem der Ring endet (Standard: 360). Werte kleiner als 360 ergeben einen Teilring
- **Abrundung** – Fügt den Kanten eine Rundung hinzu (Keine, Oben oder Unten)
- **Richtung** – Rundung zur Innen- oder Außenkante hin (sichtbar, wenn Abrundung aktiviert ist)
- **Rundungssegmente** – Glattheit der Rundung (sichtbar, wenn Abrundung aktiviert ist)

## Tipps

- Die Wandstärke entspricht (Außendurchmesser − Innendurchmesser) / 2
- Verwenden Sie diese Form für Unterlegscheiben, Distanzstücke, Buchsen und rohrartige Elemente
- Wählen Sie eine große Höhe für Rohre oder eine geringe Höhe für flache Unterlegscheiben
- Verwenden Sie Start- und Endwinkel für teilweise Ringformen wie C-Clips

## Verwandte Themen

- [Torus](torus.md) – Ein donutförmiger Ring mit rundem Querschnitt
- [Zylinder](cylinder.md) – Eine massive runde Säule (ohne hohle Mitte)
