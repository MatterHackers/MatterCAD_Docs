---
title: Spiegelen
articleKey: MirrorObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 8a8de28f5e429177d4b0092d0756387eb6b83a70
source_lang: en
---
# Spiegelen

Spiegelen maakt een gespiegelde kopie van een object langs een van de drie hoofdassen. Het resultaat is een gespiegelde versie van de oorspronkelijke vorm.

<!--  Before and after showing an object mirrored across the X axis -->
![20260506 160651 paste 20260506 160651](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160651-paste-20260506-160651.jpg)


## Gebruik

1. Selecteer een object
2. Pas de bewerking **Spiegelen** toe via het menu Transformeren
3. Kies langs welke as gespiegeld wordt

## Parameters

- **Spiegelen aan** - De as waarlangs gespiegeld wordt:
  - **X-as** - Spiegelt het object van links naar rechts
  - **Y-as** - Spiegelt het object van voor naar achter
  - **Z-as** - Spiegelt het object van boven naar onder

## Tips

- Spiegelen wordt gecentreerd op de begrenzingsdoos van het object, zodat het gespiegelde resultaat dezelfde ruimte inneemt als het origineel
- Vlaknormalen worden na het spiegelen automatisch gecorrigeerd, zodat de weergave correct blijft
- Gebruik Spiegelen om symmetrische ontwerpen te maken -- modelleer één helft, spiegel die en gebruik [Combineren](../boolean/combine.md) met het origineel
- Spiegelen is niet-destructief: je kunt de spiegelas op elk moment wijzigen

## Gerelateerd

- [Roteren](rotate.md) - Een object roteren in plaats van spiegelen
- [Schalen](scale.md) - De grootte van een object aanpassen
- [Combineren](../boolean/combine.md) - Het origineel en de gespiegelde kopie samenvoegen tot één object
