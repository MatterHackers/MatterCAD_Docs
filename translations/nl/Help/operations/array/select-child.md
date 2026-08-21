---
title: Onderliggend item selecteren
articleKey: SelectChildObject3D
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: f6f71d2b457b82126f272ea9354f877c36570df0
source_lang: en
---
# Onderliggend item selecteren

Onderliggend item selecteren kiest één onderliggend item uit een groep objecten op basis van een indexnummer of een naam. Dit is vooral handig in scriptgestuurde en parametrische ontwerpen waarbij je dynamisch wilt bepalen welk object wordt weergegeven.

<!-- IMAGE: Screenshot showing Select Child operation with multiple children and one selected by index -->
![20260506 080526 paste 20260506 080526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080526-paste-20260506-080526.jpg)


## Gebruik

1. Selecteer twee of meer objecten
2. Pas de bewerking **Onderliggend item selecteren** toe via het menu Duplicatie
3. Kies **Op index** of **Op naam** om te bepalen hoe het onderliggende item wordt geselecteerd
4. Stel het indexnummer of de naam in waarmee overeengekomen moet worden

## Parameters

- **Selectiemethode** - Kies tussen **Op index** (selecteren op positie) of **Op naam** (selecteren op objectnaam). Weergegeven als knoppen.
- **Onderliggende index** - De nulgebaseerde index van het te selecteren onderliggende item (wordt getoond bij gebruik van Op index). Ondersteunt [expressies](../../workspace/expressions.md).
- **Onderliggende naam** - De naam van het te selecteren onderliggende item (wordt getoond bij gebruik van Op naam). Ondersteunt [expressies](../../workspace/expressions.md).

Als de index buiten het bereik valt of de naam met geen enkel onderliggend item overeenkomt, wordt het eerste onderliggende item als terugval teruggegeven. Als er geen onderliggende items zijn, wordt er niets teruggegeven.

## Gebruik in scripts

Onderliggend item selecteren is ontworpen om samen te werken met expressies en de functie `rand()` om dynamische, datagestuurde ontwerpen te maken. Je kunt bijvoorbeeld een scène opbouwen met verschillende variantobjecten als onderliggende items en een expressie zoals `rand(42)` als indexseed gebruiken om er willekeurig één te kiezen.

**Voorbeeld: willekeurige boekrekwisieten voor een toneelvoorstelling**

1. Importeer 5 verschillende boekmeshes als onderliggende items van een bewerking Onderliggend item selecteren
2. Stel de Selectiemethode in op **Op index**
3. Gebruik een expressie voor Onderliggende index, zoals `floor(rand(seed) * 5)` waarbij `seed` een werkbladvariabele is
4. Dupliceer de bewerking Onderliggend item selecteren meerdere keren, elk met een andere seedwaarde
5. Elke instantie kiest willekeurig een ander boek uit de set

Dit patroon werkt voor elk scenario waarin je uit een set varianten moet kiezen: meubels, decoraties, architectonische elementen of elke verzameling uitwisselbare onderdelen.

## Tips

- Combineer met [Reeks](array.md) om gevarieerde patronen te maken waarbij elke kopie een ander onderliggend item selecteert
- Gebruik werkbladvariabelen voor de index of de naam om de selectie vanuit een spreadsheet aan te sturen
- Door de terugval naar het eerste onderliggende item loopt je ontwerp nooit vast, ook niet als de index of naam verkeerd is

## Gerelateerd

- [Reeks](array.md) - Dupliceer objecten in lineaire, radiale, curve- en transformatiepatronen
