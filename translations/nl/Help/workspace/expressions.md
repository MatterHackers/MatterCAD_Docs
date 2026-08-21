---
title: Expressies
parent: "Workspace"
nav_order: 2
source_hash: 79a2f2c42d81f7fca56a87ad89f69e4303ed0ae5
source_lang: en
---
# Expressies

Veel parameters in MatterCAD accepteren wiskundige expressies in plaats van gewone getallen. Dit maakt parametrisch ontwerpen mogelijk, waarbij het wijzigen van één waarde automatisch de gerelateerde afmetingen bijwerkt.

<!--  Screenshot showing an expression being entered in a parameter field -->
![20260318 193631 paste 20260318 193631](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193631-paste-20260318-193631.jpg)


## Gebruik

In plaats van een gewoon getal in een parameterveld te typen, kunt u een wiskundige expressie invoeren. Bijvoorbeeld:

- `20 + 5` levert 25 op
- `pi * 10` levert 31,416 op
- `width * 2` verwijst naar een andere parameter met de naam "width"

## Beschikbare constanten

- **pi** - 3,14159... (de verhouding tussen omtrek en diameter)
- **tau** - 6,28318... (2 * pi, een volledige omwenteling in radialen)

## Ondersteunde bewerkingen

- Optellen: `+`
- Aftrekken: `-`
- Vermenigvuldigen: `*`
- Delen: `/`
- Haakjes: `(` en `)` om te groeperen

## Tips

- Expressies worden ondersteund in elk veld dat `DoubleOrExpression`, `IntOrExpression` of `StringOrExpression` in de code toont -- in de praktijk accepteren de meeste numerieke velden in ontwerpgereedschappen ze
- Gebruik expressies om verbanden tussen parameters te leggen -- stel bijvoorbeeld de diameter van een gat in op `outer_diameter - 4` zodat het altijd wanden van 2 mm heeft
- Expressies worden automatisch bijgewerkt wanneer de waarden waarnaar wordt verwezen veranderen
- Gebruik een [Variabelenblad](variable-sheet.md) wanneer meerdere objecten dezelfde benoemde waarden of formules moeten delen
- U kunt expressies gebruiken in [Reeks](../operations/array/index.md)-bewerkingen om parametrische patronen te maken

## Gerelateerd

- [Componenten](components.md) - Maak herbruikbare geparametriseerde ontwerpen
- [Variabelenblad](variable-sheet.md) - Gedeelde waarden en formules voor een ontwerp opslaan
- [Objecten bewerken](../getting-started/editing-objects.md) - Werken met objectparameters
