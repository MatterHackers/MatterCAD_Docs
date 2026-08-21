---
title: Zylinder
articleKey: CylinderObject3D
parent: "Primitives"
nav_order: 5
source_hash: ab8394a14de799f83dc9c39eb86b8eaf2aab37b7
source_lang: en
---
# Zylinder

Eine runde Säulenform mit konfigurierbarem Durchmesser, konfigurierbarer Höhe und einstellbarer Anzahl von Seiten. Der Zylinder ist unverzichtbar für das Erstellen von Stiften, Stäben, Bohrungen und runden Formelementen.

<!--  Screenshot of a Cylinder primitive on the workspace -->
![20260318 183248 paste 20260318 183248](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183248-paste-20260318-183248.jpg)


## Parameter

- **Durchmesser** - Die Breite über den Zylinder hinweg (Standard: 20 mm)
- **Höhe** - Wie hoch der Zylinder ist (Standard: 20 mm)
- **Seiten** - Anzahl der Segmente entlang des Umfangs (Standard: 40). Niedrigere Werte erzeugen polygonale Formen (z. B. 6 für ein Sechseck)

### Erweiterte Parameter

Aktivieren Sie den Modus **Erweitert**, um auf zusätzliche Einstellungen zuzugreifen:

- **Durchmesser oben** - Legen Sie einen abweichenden Durchmesser für die Oberseite des Zylinders fest, um konische oder kegelstumpfförmige Formen zu erzeugen (Standard: entspricht Durchmesser)
- **Startwinkel** - Winkel, bei dem der Zylinder beginnt (Standard: 0). Verwenden Sie ihn zusammen mit Endwinkel, um Teilzylinder zu erstellen
- **Endwinkel** - Winkel, bei dem der Zylinder endet (Standard: 360). Werte kleiner als 360 ergeben tortenstückförmige Formen

## Tipps

- Setzen Sie Seiten auf einen niedrigen Wert, um regelmäßige Polygone zu erzeugen -- 6 für Sechsecke, 8 für Achtecke usw.
- Verwenden Sie unterschiedliche Werte für Durchmesser und Durchmesser oben, um Kegelstümpfe und konische Formen zu erstellen
- Legen Sie Startwinkel und Endwinkel fest, um tortenstück- oder bogenförmige Formen zu erzeugen
- Zylinder eignen sich hervorragend als Schneidwerkzeuge, um mit [Subtrahieren](../operations/boolean/subtract.md) runde Bohrungen zu erstellen

## Verwandte Themen

- [Kegel](cone.md) - Ein Zylinder, der spitz zuläuft
- [Halbzylinder](half-cylinder.md) - Ein längs halbierter Zylinder
- [Ring](ring.md) - Ein hohler Zylinder (Rohr)
