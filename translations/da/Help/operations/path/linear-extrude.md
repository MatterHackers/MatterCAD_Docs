---
title: Lineær ekstrudering
articleKey: LinearExtrudeObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cdfdb9cfe4c3339e70a23ddfb2f5071b1e8c5557
source_lang: en
---
# Lineær ekstrudering

Lineær ekstrudering giver en 2D-sti højde og forvandler en flad form til et 3D-emne. Dette er den primære måde at konvertere stier til 3D-objekter på.

<!--  Before and after showing a 2D star path extruded into a 3D star -->
![20260506 100726 paste 20260506 100726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100726-paste-20260506-100726.jpg)


## Sådan bruges den

1. Vælg en 2D-sti eller et stibaseret objekt
2. Anvend **Lineær ekstrudering** fra menuen med Sti-handlinger
3. Angiv den ønskede højde

## Parametre

- **Højde** - Hvor høj ekstruderingen er (standard: 5mm, interval: 0,1-50mm)
- **Fas top** - Tilføj en faset (afrundet) kant øverst på ekstruderingen (standard: fra)

### Fas-parametre (synlige når Fas top er aktiveret)

- **Stil** - Fasens profilstil (Skarp eller afrundet)
- **Radius** - Hvor bredt fasen strækker sig (standard: 3mm)
- **Segmenter** - Hvor jævn faskurven er (standard: 9)

## Tips

- Dette virker med enhver 2D-sti: [Cirkel](../../2d-paths/circle-path.md), [Kasse](../../2d-paths/box-path.md), [Stjerne](../../2d-paths/star-path.md), [SVG](../../primitives/svg-object.md) og [Brugerdefineret](../../2d-paths/custom-path.md) stier
- Aktivér Fas top for et mere forfinet, professionelt udseende
- Hvis du vil rotere en sti omkring en akse i stedet for at ekstrudere lige op, se [Roter profil](revolve.md)

## Relateret

- [Roter profil](revolve.md) - Drej en sti omkring en akse
- [2D-stier](../../2d-paths/index.md) - Tilgængelige stiformer
- [Tekst](../../primitives/text.md) - Tekst ekstruderes automatisk
