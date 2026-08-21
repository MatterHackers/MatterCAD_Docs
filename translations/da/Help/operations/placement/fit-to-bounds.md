---
title: Tilpas til grænser
articleKey: FitToBoundsObject3D_4
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: 91b9c917cb636f28403c291a4d56f22bf6758b70
source_lang: en
---
# Tilpas til grænser

Tilpas til grænser skalerer et objekt, så det passer inden for angivne mål for bredde, dybde og højde. Du kan styre, hvordan objektet strækkes og justeres inden for målgrænserne.

<!--  Screenshot showing an object being fit to specific bounding dimensions -->
![20260506 154930 paste 20260506 154930](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154930-paste-20260506-154930.jpg)

## Sådan bruges det

1. Vælg et objekt
2. Anvend handlingen **Tilpas til grænser** fra menuen Placering
3. Indtast målmålene
4. Vælg låsning af proportioner og strækadfærd

## Parametre

- **Lås proportioner** - Hvordan proportionerne skal begrænses:
  - **Ingen** - Hver akse kan indstilles uafhængigt
  - **X & Y** - Bredde og dybde er låst sammen
  - **X, Y & Z** - Ensartet skalering på alle akser
- **Bredde** - Målbredde (X-dimension)
- **Dybde** - Måldybde (Y-dimension)
- **Højde** - Målhøjde (Z-dimension)

### Når Lås proportioner er X & Y eller X, Y & Z

- **Stræk** - Hvordan objektet tilpasses:
  - **Indvendig** - Skalér ned, så objektet passer helt inden for grænserne (kan efterlade mellemrum)
  - **Udvid** - Skalér op, så grænserne fyldes ud (kan overskride i nogle dimensioner)

### Når Lås proportioner er Ingen

Hver akse har sin egen:

- **Stræk** - Indvendig eller Udvid pr. akse
- **Justér** - Hvor objektet placeres inden for grænserne (Min, Centrer, Maks)

## Tip

- Brug dette til at ændre størrelsen på importerede modeller til nøjagtige målmål
- Lås alle proportioner for ensartet skalering, der bevarer den oprindelige form
- Brug styring pr. akse, når du skal ramme en bestemt bredde, men er ligeglad med de øvrige dimensioner

## Relateret

- [Skalér](../transform/scale.md) - Skalér efter forhold eller procent i stedet for målstørrelse
- [Tilpas til cylinder](fit-to-cylinder.md) - Tilpas inden for en cylindrisk afgrænsning
- [Justér](align.md) - Placér objekter i forhold til hinanden
