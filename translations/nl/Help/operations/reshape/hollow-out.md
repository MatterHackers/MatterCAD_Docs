---
title: Uithollen
articleKey: HollowOutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cc2c5555723ecfe77475fef9e7a2090cdf760204
source_lang: en
---
# Uithollen

Uithollen maakt van een massief object een holle schaal door het oppervlak naar binnen te verschuiven. Het resultaat is een dunwandige versie van de oorspronkelijke vorm.

<!--  Cross-section view showing a solid object hollowed out with visible wall thickness -->
![20260506 155412 paste 20260506 155412](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155412-paste-20260506-155412.jpg)

## Gebruik

1. Selecteer een massief object
2. Pas de bewerking **Uithollen** toe via het menu Hervormen
3. Stel de gewenste wanddikte in

## Parameters

- **Afstand** - De wanddikte in millimeters (standaard: 2 mm). Dit is de dikte van de resulterende schaal.
- **Aantal cellen** - Resolutie van het uithollingsalgoritme (standaard: 64). Hogere waarden leveren gladdere binnenoppervlakken op, maar vergen meer rekentijd.

## Tips

- Uithollen is handig voor het maken van behuizingen, houders, vazen en lichtgewicht onderdelen
- Een wanddikte van 1-2 mm is gebruikelijk voor de meeste 3D-geprinte onderdelen
- Verhoog Aantal cellen als het binnenoppervlak ruw of hoekig oogt
- Bij het uithollen ontstaat een open onderkant -- combineer met een [Kubus](../../primitives/cube.md) als je een gesloten bodem nodig hebt
- Bij complexe vormen kan de berekening enkele seconden duren

## Gerelateerd

- [Vlaksnede](plane-cut.md) - Een object op een specifieke hoogte doorsnijden
- [Aftrekken](../boolean/subtract.md) - Handmatig materiaal wegsnijden
