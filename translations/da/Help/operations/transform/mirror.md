---
title: Spejl
articleKey: MirrorObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 8a8de28f5e429177d4b0092d0756387eb6b83a70
source_lang: en
---
# Spejl

Spejl opretter en spejlvendt kopiér af et objekt om en af de tre primære akser. Resultatet er en spejlvendt udgave af den oprindelige form.

<!--  Before and after showing an object mirrored across the X axis -->
![20260506 160651 paste 20260506 160651](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160651-paste-20260506-160651.jpg)


## Sådan bruges den

1. Vælg et objekt
2. Anvend handlingen **Spejl** fra menuen Transformér
3. Vælg hvilken akse der skal spejles om

## Parametre

- **Spejl om** - Aksen der spejles om:
  - **X-akse** - Vender objektet fra venstre mod højre
  - **Y-akse** - Vender objektet forfra og bagud
  - **Z-akse** - Vender objektet oppefra og ned

## Tips

- Spejl centreres om objektets afgrænsningsboks, så det spejlede resultat optager samme plads som originalen
- Fladenormaler korrigeres automatisk efter spejling, så gengivelsen forbliver korrekt
- Brug Spejl til at lave symmetriske designs -- modellér den ene halvdel, spejl den derefter, og [Kombinér](../boolean/combine.md) den med originalen
- Spejl er ikke-destruktiv: du kan ændre spejlaksen når som helst

## Relateret

- [Roter](rotate.md) - Roter et objekt i stedet for at spejle det
- [Skalér](scale.md) - Ændr størrelsen på et objekt
- [Kombinér](../boolean/combine.md) - Flet originalen og den spejlede kopiér til ét objekt
