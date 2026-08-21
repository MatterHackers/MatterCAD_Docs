---
title: Koła zębate
articleKey: GearObject3D
parent: "Mechanical Parts"
nav_order: 2
source_hash: 23098f94da8cd032e0617fbf346621504446347f
source_lang: en
---
# Koła zębate

Twórz trójwymiarowe koła zębate z w pełni konfigurowalną geometrią zębów. MatterCAD generuje prawidłowe ewolwentowe profile zębów, które poprawnie zazębiają się z innymi kołami o tym samym module i kącie przyporu.

<!-- AUTO_IMAGE: type=from_thumbnail item=gear file=mechanical_gears -->
![mechanical_gears](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_gears.png)

## Sposób użycia

1. Dodaj **Koło zębate** z narzędzi Mechaniczne lub z panelu Prymitywy
2. Ustaw liczbę zębów i pozostałe parametry
3. Profil koła zębatego zostanie wygenerowany automatycznie

## Parametry

### Elementy

- **Typ koła zębatego** - Koło Zewnętrzny lub Zębatka (prosty pręt z zębami)
- **Wysokość** - Grubość koła zębatego (wysokość wyciągnięcia)
- **Liczba zębów** - Liczba zębów na obwodzie koła zębatego (domyślnie: 30, zakres: 4-60)
- **Podziałka kołowa** - Odległość łukowa między zębami mierzona wzdłuż okręgu podziałowego (zakres: 3-30). Określa ona ogólny rozmiar.
- **Średnica otworu środkowego** - Średnica środkowego otworu na wałek (domyślnie: 4mm, ustaw 0, aby nie tworzyć otworu). Tylko dla kół zewnętrznych.
- **Szerokość krawędzi zewnętrznej** - Szerokość krawędzi na zewnątrz zębów wewnętrznych
- **Liczba zębów koła wewnętrznego** - Liczba zębów współpracującego koła wewnętrznego

### Zaawansowane

- **Kąt przyporu** - Kąt powierzchni styku zęba (typowe wartości: 14,5, 20 lub 25 stopni). Wszystkie zazębiające się koła muszą mieć ten sam kąt przyporu.
- **Luz** - Minimalny odstęp między wierzchołkiem zęba a dnem wrębu współpracującego koła
- **Luz** - Minimalny odstęp między zazębiającymi się zębami, zapobiegający zakleszczaniu

### Dane koła zębatego (tylko do odczytu)

- **Promień podziałowy** - Promień, na którym koła zazębiają się ze sobą
- **Średnica zewnętrzna** - Całkowita średnica mierzona do wierzchołków zębów

## Wskazówki

- Dwa koła zębate będą poprawnie się zazębiać, jeśli mają tę samą Podziałkę kołową i Kąt przyporu
- Skorzystaj z wartości Promień podziałowy, aby prawidłowo rozmieścić zazębiające się koła -- odległość między środkami kół powinna być równa sumie ich promieni podziałowych
- Dodaj Luz w przypadku kół drukowanych w 3D, aby uwzględnić tolerancje druku
- Profile kół zębatych 2D (do użycia z operacją Wyciągnij) opisano w artykule [Koło zębate 2D](gear-2d.md)

## Powiązane

- [Koło zębate 2D](gear-2d.md) - Ścieżka koła zębatego 2D do operacji na ścieżkach
- [Gwinty](threads.md) - Tworzenie elementów gwintowanych
