---
title: Kurve
articleKey: CurveObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 6adde5da3bb469384f59eb5e9dfe5cb642b3eec5
source_lang: en
---
# Kurve

Kurve biegt ein gerades Objekt in eine Bogen- oder Kreisform. Sie können die Biegung steuern, indem Sie entweder einen Winkel oder einen Durchmesser angeben, um den das Objekt gewickelt wird.

<!--  Before and after showing a straight bar being curved into an arc -->
![20260506 155243 paste 20260506 155243](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155243-paste-20260506-155243.jpg)

## Verwendung

1. Wählen Sie ein Objekt aus
2. Wenden Sie den Vorgang **Kurve** aus dem Menü Umformen an
3. Wählen Sie zwischen dem Biegetyp Winkel oder Durchmesser
4. Passen Sie die Parameter an, bis die gewünschte Krümmung erreicht ist

## Parameter

- **Biegetyp** – Wählen Sie zwischen:
  - **Winkel** – Den Biegewinkel direkt angeben (1–360 Grad)
  - **Durchmesser** – Den Durchmesser des Kreises angeben, um den das Teil gewickelt wird
- **Biegerichtung** – Nach oben biegen oder Nach unten biegen
- **Startprozent** – An welcher Stelle entlang des Objekts die Biegung beginnt (0–100 %)
- **Netz teilen** – Teilt das Netz für glatte Kurven (Standard: ein)
- **Min. Seiten pro Umdrehung** – Mindestanzahl der Netzsegmente pro vollständiger Umdrehung. Höhere Werte = glattere Kurven

### Erweiterte Parameter

- **Startbiegung in Prozent** – Prozentsatz von links, an dem die Biegung beginnt
- **Endbiegung in Prozent** – Prozentsatz von links, an dem die Biegung endet

## Tipps

- Verwenden Sie Kurve, um aus geraden Ausgangsformen Bögen, Ringe und gebogene Halterungen zu erstellen
- Ein Winkel von 360 wickelt das Objekt zu einem vollständigen Ring
- Erhöhen Sie Min. Seiten pro Umdrehung für glattere Ergebnisse bei engen Biegungen
- Das Objekt wird entlang seiner Länge (X-Achse) gebogen

## Verwandte Themen

- [Verdrehen](twist.md) – Entlang der Höhe drehen statt biegen
- [Torus](../../primitives/torus.md) – Eine fertige Ringform
