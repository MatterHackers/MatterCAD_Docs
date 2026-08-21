---
title: Kugel
articleKey: SphereObject3D
parent: "Primitives"
nav_order: 14
source_hash: c227e98ac116c3481bb2af73c55801de84e70b1e
source_lang: en
---
# Kugel

Eine runde Kugelform mit einstellbarem Durchmesser und Detailgrad.

<!--  Screenshot of a Sphere primitive on the workspace -->
![20260318 183909 paste 20260318 183909](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183909-paste-20260318-183909.jpg)


## Parameter

- **Durchmesser** - Die Breite über die Kugel hinweg (Standard: 20 mm)
- **Seiten** - Anzahl der Segmente entlang des Umfangs (Standard: 40). Mehr Seiten = glattere Oberfläche

### Erweiterte Parameter

Aktivieren Sie den Modus **Erweitert** für zusätzliche Einstellungen:

- **Startwinkel** - Winkel, an dem die Kugeloberfläche beginnt (Standard: 0)
- **Endwinkel** - Winkel, an dem die Kugeloberfläche endet (Standard: 360). Werte unter 360 erzeugen Teilkugelformen
- **Breitengrad-Segmente** - Anzahl der Segmente von oben nach unten (Standard: 30). Mehr = glattere Pole

## Tipps

- Für den 3D-Druck sind 40 Seiten in der Regel ausreichend. Höhere Werte erzeugen glattere Oberflächen, aber größere Dateien
- Verwenden Sie Start- und Endwinkel, um Teilkugelformen wie Schalen oder Kuppeln zu erstellen
- Kombinieren Sie die Kugel mit [Subtrahieren](../operations/boolean/subtract.md), um kugelförmige Hohlräume zu erzeugen

## Verwandte Themen

- [Halbkugel](half-sphere.md) - Nur die obere Hemisphäre
- [Torus](torus.md) - Eine Donut-Form
