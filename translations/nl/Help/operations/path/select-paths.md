---
title: Paden selecteren
articleKey: SelectPathsObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 7
source_hash: f7df7bb24841030643e4634febedcfce6e92ada9
source_lang: en
---
# Paden selecteren

Paden selecteren filtert welke subpaden van een complex padobject behouden blijven. Dit is vooral handig bij decoratieve of meerdelige lettertypen waarbij je de buitenste letervormen en de binnenste uitsparingen als aparte onderdelen nodig hebt — bijvoorbeeld om ze in twee verschillende kleuren te 3D-printen.

<!--  Screenshot showing Select Paths applied to decorative text with outer paths highlighted -->
![20260506 154655 paste 20260506 154655](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154655-paste-20260506-154655.jpg)

## Hoe paddiepte werkt

Wanneer een padobject vormen met ingesloten gebieden bevat (zoals de binnenkant van de letter "O" of de holte van een decoratieve krul), zijn die ingesloten gebieden **gaten** op diepte 1. De buitencontour van elke letter of vorm bevindt zich op **diepte 0**.

```
Depth 0 — outer contour of each letter or shape
Depth 1 — first level of enclosed holes (inside an "O", "A", etc.)
Depth 2 — shapes nested inside a hole (rarely used)
```

## Filtervoorinstellingen

### Alle
Neemt elk pad ongewijzigd op. Dit is de standaardinstelling en komt overeen met het helemaal niet toepassen van Paden selecteren.

### Alleen buitenste paden
Behoudt alleen de buitencontour van elke vorm (diepte == 0). Gebruik dit om alleen de letteromtrekken van een decoratief lettertype te krijgen, zonder de binnenste uitsparingen.

### Alleen gaten
Behoudt alleen de ingesloten gaten (diepte > 0). Gebruik dit om alleen de binnenste uitgesneden gebieden van letters en vormen te krijgen.

### Op groepsindex
Behoudt alleen paden die bij één losstaande vorm horen. Groep 0 is de eerste vorm, groep 1 de tweede, enzovoort. Gebruik dit om één teken uit een woord te isoleren.

### Aangepast
Schrijf een expressie die voor elk pad wordt geëvalueerd. Het pad wordt **opgenomen** als de expressie ongelijk aan nul is en **uitgesloten** als deze nul is.

Expressies moeten beginnen met `=` om variabelesubstitutie in te schakelen. Zonder `=` wordt de waarde als een gewoon getal behandeld (bijv. `1` neemt altijd op, `0` sluit altijd uit).

## Voorbeelden van aangepaste expressies

| Expressie | Effect |
|------------|--------|
| `=PathDepth==0` | Alleen buitencontouren (zelfde als Alleen buitenste paden) |
| `=PathDepth>0` | Alleen gaten (zelfde als Alleen gaten) |
| `=GroupIndex==0` | Alleen de eerste losstaande vorm |
| `=PathArea>100` | Vormen met een oppervlakte groter dan 100 mm² |
| `=PathLength>50` | Vormen met een omtrek langer dan 50 mm |

## Variabelen voor aangepaste expressies

| Variabele | Betekenis |
|----------|---------|
| `PathDepth` | 0 = buitencontour; 1+ = gat of geneste vorm |
| `GroupIndex` | Index van de losstaande vorm (0, 1, 2…) |
| `GroupOuterArea` | Oppervlakte van het buitenste pad van deze groep |
| `GroupOuterLength` | Omtrek van het buitenste pad van deze groep |
| `ChildCount` | Aantal gaten binnen het buitenste pad van deze groep |
| `PathIndex` | Volgnummer van dit pad binnen zijn groep |
| `PathArea` | Oppervlakte van dit afzonderlijke pad |
| `PathLength` | Omtrek van dit afzonderlijke pad |

## Voorbeeld: kerstlettertype in meerdere kleuren printen

Een veelvoorkomend gebruik van Paden selecteren is het printen van decoratieve tekst waarbij de letters binnenste uitsparingen hebben. Om de buitenste letters in de ene kleur en de binnenste uitsparingen in een tweede kleur te printen:

1. Voeg een **Tekst**-object toe en stel het in op **2D-uitvoer**
2. Pas **Paden selecteren** toe → stel de voorinstelling in op **Alleen buitenste paden**
3. Pas **Lineaire extrusie** toe om er hoogte aan te geven → wijs je eerste filamentkleur toe
4. Ga terug naar het oorspronkelijke tekstobject
5. Pas een tweede keer **Paden selecteren** toe → stel de voorinstelling in op **Alleen gaten**
6. Pas **Lineaire extrusie** toe met dezelfde hoogte → wijs je tweede filamentkleur toe
7. Plaats het ene geëxtrudeerde object boven op het andere — de twee kleuren sluiten perfect op elkaar aan

## Gerelateerd

- [Lineaire extrusie](linear-extrude.md) — Geef de gefilterde paden hoogte om een 3D-object te maken
- [Wentelen](revolve.md) — Draai gefilterde paden om een as
- [SVG-object](../../primitives/svg-object.md) — Importeer vectorpaden die meerdere subpaden kunnen bevatten
- [Tekst](../../primitives/text.md) — Tekstobjecten in 2D-modus leveren uitvoer met meerdere paden op
