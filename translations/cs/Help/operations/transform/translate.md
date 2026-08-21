---
title: Posunout
articleKey: TranslateObject3D
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c05550dee2397bdb58dc2e247a068a544233a71d
source_lang: en
---
# Posunout

Posunout přemístí objekt o zadanou vzdálenost podél os X, Y a/nebo Z. Na rozdíl od tažení objektu myší umožňuje operace Posunout zadat přesné hodnoty odsazení.

<!--  Screenshot showing the Translate operation properties with X, Y, Z offset fields -->
![20260506 160828 paste 20260506 160828](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160828-paste-20260506-160828.jpg)


## Použití

1. Vyberte objekt
2. Použijte operaci **Posunout** z nabídky Transformace
3. Zadejte požadované hodnoty odsazení pro X, Y a Z v panelu Vlastnosti

## Parametry

- **X, Y, Z** (Posunutí) – Vzdálenost, o kterou se objekt posune podél jednotlivých os, v milimetrech. Podporuje [výrazy](../../workspace/expressions.md) pro vypočítané hodnoty.

## Tipy

- Operaci Posunout použijte, když potřebujete přesné a opakovatelné umístění, které lze později upravit
- Hodnoty posunutí jsou relativní vůči aktuální pozici objektu – zadání 10 pro X jej posune o 10 mm doprava od místa, kde se nachází
- Pro rychlé přemístění můžete objekty také přetahovat přímo v pracovní ploše. Viz [Úprava objektů](../../getting-started/editing-objects.md)

## Související

- [Otočit](rotate.md) – Otočení objektu o zadaný úhel
- [Měřítko](scale.md) – Přesná změna velikosti objektu
- [Zarovnat](../placement/align.md) – Umístění objektů vůči sobě navzájem
