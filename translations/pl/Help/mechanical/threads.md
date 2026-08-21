---
title: Gwinty
articleKey: ThreadsObject3D_2
parent: "Mechanical Parts"
nav_order: 3
source_hash: 7d881b3293a508e102d3a4b845cdfd4eb9c34fa8
source_lang: en
---
# Gwinty

Twórz gwinty śrubowe z konfigurowalną średnicą, podziałką i profilem gwintu. Gwinty mogą służyć jako samodzielne śruby/wkręty albo być odejmowane od innych obiektów w celu utworzenia otworów gwintowanych.

<!-- AUTO_IMAGE: type=from_thumbnail item=threads file=mechanical_threads -->
![mechanical_threads](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_threads.png)

## Jak używać

1. Dodaj **Gwinty** z narzędzi Mechaniczne lub z panelu Prymitywy
2. Ustaw średnicę, podziałkę i liczbę obrotów
3. Opcjonalnie włącz „Użyj jako Otwór”, aby tworzyć otwory gwintowane

## Parametry

### Zastosowanie

- **Użyj jako Otwór** – po włączeniu gwinty otrzymują dodatkową tolerancję z myślą o użyciu jako odejmowany otwór (domyślnie: wyłączone)
- **Tolerancja** – dodatkowy luz pasowania przy użyciu jako otwór (domyślnie: 0,2 mm, widoczne, gdy Użyj jako Otwór jest włączone)

### Atrybuty

- **Średnica** – średnica zewnętrzna gwintowanej części (domyślnie: 10 mm)
- **Podziałka** – odległość między kolejnymi zwojami gwintu (domyślnie: 2 mm). Mniejsza podziałka = drobniejszy gwint
- **Skala gwintu** – szerokość gwintu jako stosunek do podziałki (domyślnie: 1,0, zakres: 0,1–1,0)
- **Obroty** – liczba pełnych zwojów gwintu (domyślnie: 10)

### Geometria

- **Boki** – liczba segmentów na obwodzie (domyślnie: 40). Więcej = gładsza powierzchnia

### Wierzchołki (końce gwintu)

- **Skala wierzchołka** – stopień zwężenia końców gwintu (domyślnie: 0, zakres: 0–1). Ustaw wartość powyżej 0, aby utworzyć stożkowe wprowadzenie na końcach
- **Kąt wierzchołka** – kąt, na którym następuje zwężenie wierzchołków (domyślnie: 90 stopni)

## Wskazówki

- Aby utworzyć otwór gwintowany: włącz „Użyj jako Otwór”, ustaw położenie gwintu i użyj [Odejmij](../operations/boolean/subtract.md) względem swojego obiektu
- Dodaj Tolerancję przy użyciu jako otwór, aby wydrukowane części do siebie pasowały
- Standardowe metryczne podziałki gwintu: M3=0,5 mm, M4=0,7 mm, M5=0,8 mm, M6=1,0 mm, M8=1,25 mm, M10=1,5 mm
- Użyj Skali wierzchołka, aby utworzyć wprowadzenie ułatwiające rozpoczęcie wkręcania

## Powiązane

- [Koła zębate](gears.md) – twórz mechaniczne kształty kół zębatych
- [Walec](../primitives/cylinder.md) – zwykły okrągły słupek (bez gwintu)
- [Odejmij](../operations/boolean/subtract.md) – wycinaj gwinty z innych obiektów, aby tworzyć otwory
