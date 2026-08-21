---
title: Curve
articleKey: CurveObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 6adde5da3bb469384f59eb5e9dfe5cb642b3eec5
source_lang: en
---
# Curve

Curve biegt ein gerades Objekt in eine bogen- oder kreisförmige Form. Die Biegung lässt sich entweder über einen Winkel oder über einen Durchmesser steuern, um den das Objekt gewickelt wird.

<!--  Before and after showing a straight bar being curved into an arc -->
![20260506 155243 paste 20260506 155243](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155243-paste-20260506-155243.jpg)

## Verwendung

1. Wählen Sie ein Objekt aus
2. Wenden Sie die Operation **Curve** aus dem Menü Reshape an
3. Wählen Sie zwischen dem Biegungstyp Winkel oder Durchmesser
4. Passen Sie die Parameter an, bis die gewünschte Krümmung erreicht ist

## Parameter

- **Biegungstyp** – Auswahl zwischen:
  - **Winkel** – Den Biegewinkel direkt angeben (1–360 Grad)
  - **Durchmesser** – Den Durchmesser des Kreises angeben, um den das Teil gewickelt wird
- **Biegerichtung** – Nach oben oder nach unten biegen
- **Startprozentsatz** – An welcher Stelle entlang des Objekts die Biegung beginnt (0–100 %)
- **Netz unterteilen** – Unterteilt das Netz für weiche Kurven (Standard: ein)
- **Mindestanzahl Seiten pro Umdrehung** – Minimale Anzahl der Netzsegmente pro vollständiger Umdrehung. Höhere Werte = weichere Kurven

### Erweiterte Parameter

- **Biegestart in Prozent** – Prozentwert von links, an dem die Biegung beginnt
- **Biegeende in Prozent** – Prozentwert von links, an dem die Biegung endet

## Tipps

- Verwenden Sie Curve, um aus geraden Grundformen Bögen, Ringe und gebogene Halterungen zu erzeugen
- Ein Winkel von 360 wickelt das Objekt zu einem vollständigen Ring
- Erhöhen Sie die Mindestanzahl Seiten pro Umdrehung für weichere Ergebnisse bei engen Biegungen
- Das Objekt wird entlang seiner Länge (X-Achse) gebogen

## Verwandte Themen

- [Twist](twist.md) – Entlang der Höhe drehen statt biegen
- [Torus](../../primitives/torus.md) – Eine fertige Ringform
