---
title: Lineaire extrusie
articleKey: LinearExtrudeObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cdfdb9cfe4c3339e70a23ddfb2f5071b1e8c5557
source_lang: en
---
# Lineaire extrusie

Lineaire extrusie geeft hoogte aan een 2D-pad, waardoor een vlakke vorm een 3D-vaste vorm wordt. Dit is de belangrijkste manier om paden om te zetten in 3D-objecten.

<!--  Before and after showing a 2D star path extruded into a 3D star -->
![20260506 100726 paste 20260506 100726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100726-paste-20260506-100726.jpg)


## Gebruik

1. Selecteer een 2D-pad of een op een pad gebaseerd object
2. Pas **Lineaire extrusie** toe via het menu met Pad-bewerkingen
3. Stel de gewenste hoogte in

## Parameters

- **Hoogte** - Hoe hoog de extrusie is (standaard: 5mm, bereik: 0,1-50mm)
- **Afschuining boven** - Voeg een afgeschuinde (afgeronde) rand toe aan de bovenkant van de extrusie (standaard: uit)

### Afschuiningsparameters (zichtbaar wanneer Afschuining boven is ingeschakeld)

- **Stijl** - Het profiel van de afschuining (Scherp of afgerond)
- **Straal** - Hoe ver de afschuining zich uitstrekt (standaard: 3mm)
- **Segmenten** - Gladheid van de afschuiningscurve (standaard: 9)

## Tips

- Dit werkt met elk 2D-pad: [Cirkel](../../2d-paths/circle-path.md), [Kubus](../../2d-paths/box-path.md), [Ster](../../2d-paths/star-path.md), [SVG](../../primitives/svg-object.md) en [Aangepast](../../2d-paths/custom-path.md) paden
- Schakel Afschuining boven in voor een verzorgder, professioneler resultaat
- Om een pad om een as te wentelen in plaats van recht omhoog te extruderen, zie [Wentelen](revolve.md)

## Gerelateerd

- [Wentelen](revolve.md) - Draai een pad rond een as
- [2D-paden](../../2d-paths/index.md) - Beschikbare padvormen
- [Tekst](../../primitives/text.md) - Tekst wordt automatisch geëxtrudeerd
