---
title: Vlaksnede
articleKey: PlaneCutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 5
source_hash: 64a9901bf54b71cd2ecc12c8db189b6e2fcde25e
source_lang: en
---
# Vlaksnede

Vlaksnede snijdt een object op een opgegeven hoogte door met een horizontaal vlak, waarbij alleen het deel onder de snede behouden blijft. Het snijvlak wordt afgesloten met een plat vlak.

<!--  Before and after showing an object being sliced at a specific height -->
![20260506 155526 paste 20260506 155526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155526-paste-20260506-155526.jpg)

## Gebruik

1. Selecteer een object
2. Pas de bewerking **Vlaksnede** toe via het menu Hervormen
3. Stel de snijhoogte in

## Parameters

- **Snijhoogte** - De Z-hoogte waarop het object wordt doorgesneden (standaard: 10mm, bereik: 1-200mm)

## Tips

- Gebruik Vlaksnede om de bovenkant van een model op een specifieke hoogte vlak te maken
- Handig voor het bijsnijden van geïmporteerde modellen of het maken van vlakke bodems
- Gebruik voor het snijden met een niet-vlakke vorm in plaats daarvan [Aftrekken](../boolean/subtract.md) met een ander object
- Om met een schuin vlak te snijden, roteert u het object eerst, past u Vlaksnede toe en roteert u het daarna terug

## Gerelateerd

- [Doorsnijden](../boolean/intersect.md) - Behoud alleen waar objecten elkaar overlappen
- [Aftrekken](../boolean/subtract.md) - Snijden met elke vorm, niet alleen met een vlak
- [Uithollen](hollow-out.md) - Maak een holle schaal
