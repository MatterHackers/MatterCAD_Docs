---
title: Bol
articleKey: SphereObject3D
parent: "Primitives"
nav_order: 14
source_hash: c227e98ac116c3481bb2af73c55801de84e70b1e
source_lang: en
---
# Bol

Een ronde balvorm met instelbare diameter en detailniveau.

<!--  Screenshot of a Sphere primitive on the workspace -->
![20260318 183909 paste 20260318 183909](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183909-paste-20260318-183909.jpg)


## Parameters

- **Diameter** - De breedte over de bol (standaard: 20mm)
- **Zijden** - Aantal segmenten rond de omtrek (standaard: 40). Meer zijden = gladder oppervlak

### Geavanceerde parameters

Schakel de modus **Geavanceerd** in voor extra instellingen:

- **Starthoek** - Hoek waar het booloppervlak begint (standaard: 0)
- **Eindhoek** - Hoek waar het booloppervlak eindigt (standaard: 360). Stel minder dan 360 in voor gedeeltelijke bolvormen
- **Breedtegraadzijden** - Aantal segmenten van boven naar beneden (standaard: 30). Meer = gladdere polen

## Tips

- Voor 3D-printen zijn 40 zijden meestal voldoende. Hogere waarden geven gladdere oppervlakken, maar grotere bestanden
- Gebruik de Starthoek en Eindhoek om gedeeltelijke bolvormen te maken, zoals schalen of koepels
- Combineer met [Aftrekken](../operations/boolean/subtract.md) om bolvormige holtes te maken

## Gerelateerd

- [Halve bol](half-sphere.md) - Alleen de bovenste halve bol
- [Torus](torus.md) - Een donutvorm
