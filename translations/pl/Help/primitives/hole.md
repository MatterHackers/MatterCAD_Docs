---
title: Otwór
articleKey: CubeHoleObject3D
parent: "Primitives"
nav_order: 9
source_hash: c6c802f54eaaccbd4caad827b9f967aa46b059a6
source_lang: en
---
# Otwór

Obiekt w kształcie sześcianu, wstępnie skonfigurowany tak, aby działać jako narzędzie odejmowania logicznego. Gdy używasz operacji [Połącz](../operations/boolean/combine.md), obiekty Otwór są automatycznie odejmowane od pozostałych kształtów, zamiast być do nich dodawane.

<!--  Screenshot showing a Hole object being used to cut a rectangular slot in another shape -->
![20260318 183619 paste 20260318 183619](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183619-paste-20260318-183619.jpg)


## Jak to działa

Prymityw Otwór działa jak [Sześcian](cube.md), ale ma typ wyjściowy ustawiony na „Otwór”. Gdy łączysz obiekty, wśród których znajduje się Otwór, jego objętość zostaje usunięta z wyniku.

## Parametry

Takie same jak w przypadku obiektu [Sześcian](cube.md):

- **Szerokość** - Rozmiar wzdłuż osi X
- **Głębokość** - Rozmiar wzdłuż osi Y
- **Wysokość** - Rozmiar wzdłuż osi Z

## Wskazówki

- Ustaw Otwór tak, aby nachodził na obiekt, który chcesz przyciąć
- Spraw, aby Otwór przechodził całkowicie przez obiekt docelowy, jeśli chcesz uzyskać otwór przelotowy
- Ten sam efekt możesz uzyskać, stosując zwykłe kształty z operacją [Odejmij](../operations/boolean/subtract.md), ale Otwory są wygodne, ponieważ działają automatycznie z operacją [Połącz](../operations/boolean/combine.md)
- Do okrągłych otworów użyj obiektu [Walec](cylinder.md) wraz z operacją Odejmij

## Powiązane

- [Sześcian](cube.md) - Ten sam kształt bez zachowania otworu
- [Połącz](../operations/boolean/combine.md) - Scala kształty i automatycznie odejmuje Otwory
- [Odejmij](../operations/boolean/subtract.md) - Ręcznie odejmij dowolny kształt od innego
