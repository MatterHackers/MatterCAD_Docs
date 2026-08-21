---
title: Obrázek na křivku
articleKey: ImageToPathObject3D_2
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 0145587f635ede68bfc1df37b4f0d366a03d3a6c
source_lang: en
---
# Obrázek na křivku

Obrázek na křivku obtáhne obrysy obrázku a vytvoří 2D cesty. Tyto cesty lze poté vytáhnout, rotovat nebo použít s libovolnou jinou operací s cestami. Je to ideální způsob, jak převést loga, siluety a jednoduchou grafiku na 3D objekty.

![20260324 075521 paste 20260324 075521](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-075521-paste-20260324-075521.jpg)


## Použití

1. Vyberte v pracovní ploše objekt obrázku
2. Použijte **Obrázek na křivku** z nabídky operací s obrázky
3. Zvolte typ analýzy a upravte vybraný rozsah

## Parametry

- **Typ analýzy** - Způsob, jakým je obrázek analyzován pro obtažení:
  - **Průhlednost** - Obtažení podle průhledných a neprůhledných oblastí (nejvhodnější pro PNG s průhledným pozadím)
  - **Barvy** - Obtažení podle barevných oblastí
  - **Intenzita** - Obtažení podle úrovní jasu (nejvhodnější pro většinu obrázků)
- **Vybrat rozsah** - Ovládací prvek histogramu pro výběr hodnot jasu/barev, které se do obtažení zahrnou
- **Min. plocha povrchu** - Minimální plocha smyčky cesty, aby byla zahrnuta. Zvyšte hodnotu pro odfiltrování drobných šumových artefaktů

## Tipy

- Nejlépe fungují čisté obrázky s vysokým kontrastem a jednoduchými tvary
- Pro obrázky PNG s průhledným pozadím použijte režim Průhlednost
- Pro fotografie a obrázky bez průhlednosti použijte režim Intenzita
- Po obtažení použijte [Lineární extruze](../path/linear-extrude.md), abyste cestě dali výšku
- Zvyšte hodnotu Min. plocha povrchu, chcete-li z obtažení odebrat drobné nežádoucí detaily

## Související

- [Konvertor obrázků](image-converter.md) - Vytvoří reliéf z výškové mapy namísto plochých cest
- [Litofanie](lithophane.md) - Vytvoří prosvětlené obrazové panely
- [SVG Object](../../primitives/svg-object.md) - Importuje vektorovou grafiku přímo (bez nutnosti obtahování)
- [Lineární extruze](../path/linear-extrude.md) - Dá obtažené cestě výšku
