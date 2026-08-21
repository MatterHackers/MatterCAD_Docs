---
title: Speil
articleKey: MirrorObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 8a8de28f5e429177d4b0092d0756387eb6b83a70
source_lang: en
---
# Speil

Speil oppretter en speilvendt kopi av et objekt over en av de tre hovedaksene. Resultatet er en speilet versjon av den opprinnelige formen.

<!--  Before and after showing an object mirrored across the X axis -->
![20260506 160651 paste 20260506 160651](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160651-paste-20260506-160651.jpg)


## Slik bruker du den

1. Velg et objekt
2. Bruk operasjonen **Speil** fra Transformer-menyen
3. Velg hvilken akse det skal speiles over

## Parametere

- **Speiling på** – Aksen det skal speiles over:
  - **X-akse** – Vender objektet fra venstre til høyre
  - **Y-akse** – Vender objektet forfra og bakover
  - **Z-akse** – Vender objektet fra topp til bunn

## Tips

- Speil sentreres på objektets avgrensningsboks, slik at det speilede resultatet opptar samme plass som originalen
- Flatenormaler korrigeres automatisk etter speiling for å opprettholde riktig gjengivelse
- Bruk Speil til å lage symmetriske design – modeller den ene halvdelen, speil den og [Kombiner](../boolean/combine.md) den med originalen
- Speil er ikke-destruktiv: du kan endre speilaksen når som helst

## Relatert

- [Roter](rotate.md) – Roter et objekt i stedet for å speile det
- [Skaler](scale.md) – Endre størrelsen på et objekt
- [Kombiner](../boolean/combine.md) – Slå sammen originalen og den speilede kopien til ett objekt
