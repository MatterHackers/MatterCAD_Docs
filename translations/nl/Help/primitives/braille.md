---
title: Braille
articleKey: BrailleObject3D
parent: "Primitives"
nav_order: 2
source_hash: d1d9d4aeb9b87efbe32045f2a96cfea49048f95f
source_lang: en
---
# Braille

Genereer 3D-printbare brailletekst op basis van gewone Engelse tekst. De Braille-tool ondersteunt zowel Grade 1 (letter voor letter) als Grade 2 (verkort) braille.

<!-- Screenshot of a Braille object showing raised dots on the workspace -->
![20260318 182800 paste 20260318 182800](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-182800-paste-20260318-182800.jpg)


## Gebruik

1. Voeg een **Braille**-primitief toe vanuit het paneel Primitieven
2. Typ je tekst in het veld **Te coderen tekst**
3. De tool zet deze automatisch om naar het juiste braillepuntpatroon

## Parameters

- **Te coderen tekst** - De Engelse tekst die naar braille wordt omgezet
- **Schalen** - Pas de totale grootte van het braille-resultaat aan
- **Hoogte** - De hoogte van de verhoogde braillepunten

## Tips

- Grade 2-braille gebruikt afkortingen en samentrekkingen voor veelvoorkomende woorden en lettercombinaties, waardoor het compacter is
- Er worden standaardafmetingen voor braillecellen gebruikt, zodat het resultaat leesbaar is
- Combineer met een platte [Kubus](cube.md) als basis om een volledig braillelabel of -bord te maken
- Voor braillekaarten met een geïntegreerde basis, zie [Braillekaart](braille-card.md)

## Gerelateerd

- [Braillekaart](braille-card.md) - Braille met een geïntegreerde kaartbasis
- [Tekst](text.md) - Standaard 3D-tekst
