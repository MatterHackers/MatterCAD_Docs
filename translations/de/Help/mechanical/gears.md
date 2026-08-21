---
title: Zahnräder
articleKey: GearObject3D
parent: "Mechanical Parts"
nav_order: 2
source_hash: 23098f94da8cd032e0617fbf346621504446347f
source_lang: en
---
# Zahnräder

Erstellen Sie 3D-Zahnräder mit vollständig konfigurierbarer Zahngeometrie. MatterCAD erzeugt korrekte Evolventen-Zahnprofile, die einwandfrei mit anderen Zahnrädern gleichen Moduls und gleichen Eingriffswinkels kämmen.

<!-- AUTO_IMAGE: type=from_thumbnail item=gear file=mechanical_gears -->
![mechanical_gears](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_gears.png)

## Verwendung

1. Fügen Sie ein **Zahnrad** über die Werkzeuge unter Mechanisch oder das Panel Primitive hinzu
2. Legen Sie die Zähnezahl und weitere Parameter fest
3. Das Zahnradprofil wird automatisch erzeugt

## Parameter

### Merkmale

- **Zahnradtyp** - Außenverzahntes Zahnrad oder Zahnstange (gerade Stange mit Zähnen)
- **Höhe** - Dicke des Zahnrads (Extrusionshöhe)
- **Zähnezahl** - Anzahl der Zähne am Umfang des Zahnrads (Standard: 30, Bereich: 4-60)
- **Teilkreisteilung** - Der Bogenabstand zwischen den Zähnen entlang des Teilkreises (Bereich: 3-30). Sie bestimmt die Gesamtgröße.
- **Mittellochdurchmesser** - Durchmesser der zentralen Wellenbohrung (Standard: 4 mm, 0 für kein Loch). Nur bei außenverzahnten Zahnrädern.
- **Außenkantenbreite** - Breite des Rands außerhalb der Innenverzahnung
- **Zähnezahl Innenrad** - Zähnezahl des kämmenden innenverzahnten Zahnrads

### Erweitert

- **Eingriffswinkel** - Der Winkel der Zahnkontaktfläche (übliche Werte: 14,5, 20 oder 25 Grad). Alle miteinander kämmenden Zahnräder müssen denselben Eingriffswinkel verwenden.
- **Spiel** - Minimaler Abstand zwischen Zahnkopf und Zahnlücke des Gegenrads
- **Umkehrspiel** - Minimaler Abstand zwischen kämmenden Zahnradzähnen, um ein Klemmen zu verhindern

### Zahnraddaten (schreibgeschützt)

- **Teilkreisradius** - Der Radius, an dem die Zahnräder miteinander kämmen
- **Außendurchmesser** - Der Gesamtdurchmesser bis zu den Zahnköpfen

## Tipps

- Zwei Zahnräder kämmen korrekt, wenn sie dieselbe Teilkreisteilung und denselben Eingriffswinkel haben
- Verwenden Sie die Werte für den Teilkreisradius, um kämmende Zahnräder korrekt zu positionieren -- der Abstand zwischen den Zahnradmittelpunkten sollte der Summe ihrer Teilkreisradien entsprechen
- Fügen Sie bei 3D-gedruckten Zahnrädern Umkehrspiel hinzu, um Drucktoleranzen auszugleichen
- Für 2D-Zahnradprofile (zur Verwendung mit Extrudieren) siehe [Zahnrad 2D](gear-2d.md)

## Verwandte Themen

- [Zahnrad 2D](gear-2d.md) - 2D-Zahnradpfad für Pfadoperationen
- [Gewindegänge](threads.md) - Gewindemerkmale erstellen
