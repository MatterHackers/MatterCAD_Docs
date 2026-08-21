---
title: Verkleinen
articleKey: DecimateObject3D
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 58a2573b968808e98203832142fa8bacf7a9cf99
source_lang: en
---
# Verkleinen (Decimeren)

Verkleinen verlaagt het aantal polygonen van een mesh terwijl de algehele vorm behouden blijft. Dit is handig om zeer gedetailleerde modellen te vereenvoudigen, de bestandsgrootte te beperken en bewerkingen op complexe geometrie te versnellen.

![20260324 080430 paste 20260324 080430](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080430-paste-20260324-080430.jpg)


## Gebruik

1. Selecteer een object
2. Pas de bewerking **Verkleinen** toe via het menu Mesh
3. Kies je doel (aantal of percentage) en pas dit aan

## Parameters

- **Modus** - Kies hoe je het doel opgeeft:
  - **Procent** - Behoud een percentage van de oorspronkelijke polygonen (standaard: 50%)
  - **Aantal** - Streef naar een specifiek aantal polygonen
- **Aantal bronpolygonen** - Oorspronkelijk aantal polygonen (alleen-lezen)
- **Doelpercentage** - Percentage polygonen dat behouden blijft (zichtbaar in de modus Procent)
- **Doelaantal** - Exact aantal polygonen dat behouden blijft (zichtbaar in de modus Aantal)
- **Aantal na procentuele verkleining** - Uiteindelijk aantal polygonen na de procentuele verkleining (alleen-lezen)
- **Oppervlak behouden** - Projecteer vertices terug op het oorspronkelijke oppervlak voor hogere nauwkeurigheid (langzamer, maar getrouwer aan de oorspronkelijke vorm)

## Tips

- Een verkleining van 50% behoudt de visuele kwaliteit meestal goed
- Schakel Oppervlak behouden in wanneer nauwkeurigheid belangrijker is dan snelheid
- Een lager aantal polygonen versnelt booleaanse bewerkingen op complexe geïmporteerde modellen
- Zeer lage aantallen polygonen tasten de vorm zichtbaar aan -- controleer het resultaat voordat je het definitief maakt

## Gerelateerd

- [Repareren](repair.md) - Meshproblemen oplossen
