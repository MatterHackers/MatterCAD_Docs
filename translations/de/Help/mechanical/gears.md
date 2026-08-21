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

1. Fügen Sie ein **Zahnrad** aus den mechanischen Werkzeugen oder dem Bedienfeld „Grundkörper“ hinzu
2. Legen Sie die Zähnezahl und weitere Parameter fest
3. Das Zahnprofil wird automatisch erzeugt

## Parameter

### Merkmale

- **Zahnradtyp** – Außenverzahntes Zahnrad oder Zahnstange (gerade Leiste mit Zähnen)
- **Höhe** – Dicke des Zahnrads (Extrusionshöhe)
- **Zähnezahl** – Anzahl der Zähne am Umfang des Zahnrads (Standard: 30, Bereich: 4–60)
- **Umfangsteilung** – Der Bogenabstand zwischen den Zähnen entlang des Teilkreises (Bereich: 3–30). Sie bestimmt die Gesamtgröße.
- **Durchmesser der Mittelbohrung** – Durchmesser der zentralen Wellenbohrung (Standard: 4 mm, 0 für keine Bohrung). Nur bei außenverzahnten Zahnrädern.
- **Breite des Außenrands** – Breite des Rands außerhalb der Innenverzahnung
- **Zähnezahl des Innenzahnrads** – Zähnezahl des kämmenden innenverzahnten Zahnrads

### Erweitert

- **Eingriffswinkel** – Der Winkel der Zahnkontaktfläche (übliche Werte: 14,5, 20 oder 25 Grad). Alle kämmenden Zahnräder müssen denselben Eingriffswinkel verwenden.
- **Kopfspiel** – Minimaler Abstand zwischen Zahnkopf und Zahnlücke des Gegenrads
- **Flankenspiel** – Minimaler Abstand zwischen kämmenden Zahnflanken, um ein Klemmen zu verhindern

### Zahnraddaten (schreibgeschützt)

- **Teilkreisradius** – Der Radius, an dem die Zahnräder miteinander kämmen
- **Außendurchmesser** – Der Gesamtdurchmesser bis zu den Zahnköpfen

## Tipps

- Zwei Zahnräder kämmen korrekt, wenn sie dieselbe Umfangsteilung und denselben Eingriffswinkel haben
- Verwenden Sie die Werte für den Teilkreisradius, um kämmende Zahnräder korrekt zu positionieren – der Abstand zwischen den Zahnradmittelpunkten sollte der Summe ihrer Teilkreisradien entsprechen
- Fügen Sie bei 3D-gedruckten Zahnrädern Flankenspiel hinzu, um Drucktoleranzen auszugleichen
- Für 2D-Zahnradprofile (zur Verwendung mit Extrudieren) siehe [Zahnrad 2D](gear-2d.md)

## Verwandte Themen

- [Zahnrad 2D](gear-2d.md) – 2D-Zahnradpfad für Pfadoperationen
- [Gewinde](threads.md) – Gewindeelemente erstellen
