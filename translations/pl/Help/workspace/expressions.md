---
title: Wyrażenia
parent: "Workspace"
nav_order: 2
source_hash: 79a2f2c42d81f7fca56a87ad89f69e4303ed0ae5
source_lang: en
---
# Wyrażenia

Wiele parametrów w MatterCAD przyjmuje wyrażenia matematyczne zamiast zwykłych liczb. Umożliwia to projektowanie parametryczne, w którym zmiana jednej wartości automatycznie aktualizuje powiązane wymiary.

<!--  Screenshot showing an expression being entered in a parameter field -->
![20260318 193631 paste 20260318 193631](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193631-paste-20260318-193631.jpg)


## Sposób użycia

Zamiast wpisywać w polu parametru zwykłą liczbę, możesz wpisać wyrażenie matematyczne. Na przykład:

- `20 + 5` daje wynik 25
- `pi * 10` daje wynik 31,416
- `width * 2` odwołuje się do innego parametru o nazwie „width”

## Dostępne stałe

- **pi** – 3,14159... (stosunek obwodu do średnicy)
- **tau** – 6,28318... (2 * pi, pełny obrót w radianach)

## Obsługiwane operacje

- Dodawanie: `+`
- Odejmowanie: `-`
- Mnożenie: `*`
- Dzielenie: `/`
- Nawiasy: `(` i `)` do grupowania

## Wskazówki

- Wyrażenia są obsługiwane w każdym polu, które w kodzie zawiera `DoubleOrExpression`, `IntOrExpression` lub `StringOrExpression` – w praktyce przyjmuje je większość pól liczbowych w narzędziach projektowych
- Używaj wyrażeń, aby tworzyć zależności między parametrami – na przykład ustaw średnicę otworu na `outer_diameter - 4`, aby zawsze miał ścianki o grubości 2 mm
- Wyrażenia aktualizują się automatycznie, gdy zmienią się wartości, do których się odwołują
- Użyj [Arkusza zmiennych](variable-sheet.md), gdy kilka obiektów ma współdzielić te same nazwane wartości lub formuły
- Wyrażeń możesz używać w operacjach [Szyk](../operations/array/index.md), aby tworzyć wzory parametryczne

## Powiązane

- [Komponenty](components.md) – Twórz parametryczne projekty wielokrotnego użytku
- [Arkusz zmiennych](variable-sheet.md) – Przechowuj wspólne wartości i formuły projektu
- [Edycja obiektów](../getting-started/editing-objects.md) – Praca z parametrami obiektów
