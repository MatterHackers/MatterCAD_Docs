---
title: Přizpůsobit hranicím
articleKey: FitToBoundsObject3D_4
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: 91b9c917cb636f28403c291a4d56f22bf6758b70
source_lang: en
---
# Přizpůsobit hranicím

Přizpůsobit hranicím škáluje objekt tak, aby se vešel do zadaných rozměrů šířky, hloubky a výšky. Můžete určit, jak se objekt roztahuje a zarovnává v rámci cílových hranic.

<!--  Screenshot showing an object being fit to specific bounding dimensions -->
![20260506 154930 paste 20260506 154930](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154930-paste-20260506-154930.jpg)

## Jak používat

1. Vyberte objekt
2. Použijte operaci **Přizpůsobit hranicím** z nabídky Umístění
3. Zadejte cílové rozměry
4. Zvolte zamknutí proporcí a chování roztažení

## Parametry

- **Zamknout proporce** - Jak omezit proporce:
  - **Žádný** - Každou osu lze nastavit nezávisle
  - **X a Y** - Šířka a hloubka jsou svázány dohromady
  - **X, Y a Z** - Rovnoměrné škálování na všech osách
- **Šířka** - Cílová šířka (rozměr X)
- **Hloubka** - Cílová hloubka (rozměr Y)
- **Výška** - Cílová výška (rozměr Z)

### Když je Zamknout proporce nastaveno na X a Y nebo X, Y a Z

- **Roztažení** - Jak se objekt přizpůsobí:
  - **Uvnitř** - Zmenší se tak, aby se celý vešel do hranic (mohou vzniknout mezery)
  - **Rozbalit** - Zvětší se tak, aby hranice vyplnil (v některých rozměrech je může přesáhnout)

### Když je Zamknout proporce nastaveno na Žádný

Každá osa má vlastní:

- **Roztažení** - Uvnitř nebo Rozbalit pro každou osu
- **Zarovnat** - Kam umístit v rámci hranic (Min, Střed, Max)

## Tipy

- Použijte to ke změně velikosti importovaných modelů na přesné cílové rozměry
- Zamkněte všechny proporce pro rovnoměrné škálování, které zachová původní tvar
- Použijte ovládání po jednotlivých osách, když potřebujete dodržet konkrétní šířku, ale na ostatních rozměrech vám nezáleží

## Související

- [Měřítko](../transform/scale.md) - Škálování poměrem nebo procenty místo cílové velikosti
- [Přizpůsobit válci](fit-to-cylinder.md) - Přizpůsobení válcové hranici
- [Zarovnat](align.md) - Umístění objektů vůči sobě navzájem
