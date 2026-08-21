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

Lineær ekstrudering gir en 2D-bane høyde og gjør en flat form om til et 3D-legeme. Dette er den viktigste måten å gjøre baner om til 3D-objekter på.

<!--  Before and after showing a 2D star path extruded into a 3D star -->
![20260506 100726 paste 20260506 100726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100726-paste-20260506-100726.jpg)


## Slik bruker du den

1. Velg en 2D-bane eller et banebasert objekt
2. Bruk **Lineær ekstrudering** fra menyen med Bane-operasjoner
3. Angi ønsket høyde

## Parametere

- **Høyde** - Hvor høy ekstruderingen er (standard: 5 mm, område: 0,1-50 mm)
- **Fas topp** - Legg til en faset (avrundet) kant øverst på ekstruderingen (standard: av)

### Fas-parametere (synlige når Fas topp er aktivert)

- **Stil** - Profilstilen på fasen (Skarp eller avrundet)
- **Radius** - Hvor bredt fasen strekker seg (standard: 3 mm)
- **Segmenter** - Hvor glatt faskurven er (standard: 9)

## Tips

- Dette fungerer med alle 2D-baner: [Sirkel](../../2d-paths/circle-path.md), [Boks](../../2d-paths/box-path.md), [Stjerne](../../2d-paths/star-path.md), [SVG](../../primitives/svg-object.md) og [Egendefinert](../../2d-paths/custom-path.md)-baner
- Aktiver Fas topp for et mer forseggjort, profesjonelt uttrykk
- Hvis du vil rotere en bane rundt en akse i stedet for å ekstrudere rett opp, se [Roter rundt akse](revolve.md)

## Relatert

- [Roter rundt akse](revolve.md) - Snurr en bane rundt en akse
- [2D-baner](../../2d-paths/index.md) - Tilgjengelige baneformer
- [Tekst](../../primitives/text.md) - Tekst ekstruderes automatisk
