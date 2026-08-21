---
title: Torus
articleKey: TorusObject3D
parent: "Primitives"
nav_order: 17
source_hash: aaec1652de4d6713bd01a707964cf4985d3fb5f6
source_lang: en
---
# Torus

Een donutvormige ring met onafhankelijke controle over de totale grootte en de dikte van de ringdoorsnede.

<!--  Screenshot of a Torus primitive on the workspace -->
![20260318 184240 paste 20260318 184240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184240-paste-20260318-184240.jpg)


## Parameters

- **Buitendiameter** - De totale breedte van de torus (standaard: 20mm)
- **Binnendiameter** - De diameter van het gat in het midden (standaard: 10mm)
- **Zijden** - Aantal segmenten rondom de hoofdring (standaard: 40)

### Geavanceerde parameters

Schakel de modus **Geavanceerd** in voor extra instellingen:

- **Starthoek** - Hoek waar de torus begint (standaard: 0)
- **Eindhoek** - Hoek waar de torus eindigt (standaard: 360). Stel lager dan 360 in voor een open ring of boog
- **Ringzijden** - Aantal segmenten rondom de doorsnede van de ring (standaard: 15). Meer = vloeiender buisprofiel
- **Fasehoek ring** - Roteert het doorsnedeprofiel (standaard: 0)

## Tips

- De dikte van de ringbuis wordt bepaald door het verschil tussen Buitendiameter en Binnendiameter
- Gebruik de Starthoek en Eindhoek om open ringsegmenten, bogen of C-vormen te maken
- Handig voor het maken van O-ringen, handgrepen, decoratieve ringen en pijpbochten

## Gerelateerd

- [Ring](ring.md) - Een holle cilinder met rechte wanden (buis)
- [Bol](sphere.md) - Een massieve bolvorm
- [Halve bol](half-sphere.md) - Een koepelvorm
