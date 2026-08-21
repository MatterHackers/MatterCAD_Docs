---
title: Tilpass til grenser
articleKey: FitToBoundsObject3D_4
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: 91b9c917cb636f28403c291a4d56f22bf6758b70
source_lang: en
---
# Tilpass til grenser

Tilpass til grenser skalerer et objekt slik at det passer innenfor angitte mål for bredde, dybde og høyde. Du kan styre hvordan objektet strekkes og justeres innenfor målgrensene.

<!--  Screenshot showing an object being fit to specific bounding dimensions -->
![20260506 154930 paste 20260506 154930](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154930-paste-20260506-154930.jpg)

## Slik bruker du den

1. Velg et objekt
2. Bruk operasjonen **Tilpass til grenser** fra Plassering-menyen
3. Angi målene du vil oppnå
4. Velg låsing av proporsjoner og strekkoppførsel

## Parametere

- **Lås proporsjon** - Hvordan proporsjonene begrenses:
  - **Ingen** - Hver akse kan angis uavhengig
  - **X og Y** - Bredde og dybde er låst sammen
  - **X, Y og Z** - Uniform skalering på alle akser
- **Bredde** - Ønsket bredde (X-dimensjon)
- **Dybde** - Ønsket dybde (Y-dimensjon)
- **Høyde** - Ønsket høyde (Z-dimensjon)

### Når Lås proporsjon er X og Y eller X, Y og Z

- **Strekk** - Hvordan objektet tilpasses:
  - **Innside** - Skaler ned slik at objektet får plass helt innenfor grensene (kan gi mellomrom)
  - **Utvid** - Skaler opp for å fylle grensene (kan overskride i enkelte dimensjoner)

### Når Lås proporsjon er Ingen

Hver akse har sin egen:

- **Strekk** - Innside eller Utvid per akse
- **Juster** - Hvor objektet plasseres innenfor grensene (Min, Senter, Maks)

## Tips

- Bruk dette til å endre størrelsen på importerte modeller til nøyaktige mål
- Lås alle proporsjoner for uniform skalering som beholder den opprinnelige formen
- Bruk styring per akse når du må treffe en bestemt bredde, men de andre dimensjonene ikke spiller noen rolle

## Relatert

- [Skaler](../transform/scale.md) - Skaler etter forhold eller prosent i stedet for målstørrelse
- [Tilpass til sylinder](fit-to-cylinder.md) - Tilpass innenfor en sylindrisk grense
- [Juster](align.md) - Plasser objekter i forhold til hverandre
