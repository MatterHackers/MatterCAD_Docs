---
title: Cięcie płaszczyzną
articleKey: PlaneCutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 5
source_hash: 64a9901bf54b71cd2ecc12c8db189b6e2fcde25e
source_lang: en
---
# Cięcie płaszczyzną

Cięcie płaszczyzną przecina obiekt płaszczyzną poziomą na zadanej wysokości, zachowując wyłącznie część znajdującą się poniżej cięcia. Powierzchnia cięcia zostaje zamknięta płaską ścianką.

<!--  Before and after showing an object being sliced at a specific height -->
![20260506 155526 paste 20260506 155526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155526-paste-20260506-155526.jpg)

## Sposób użycia

1. Wybierz obiekt
2. Zastosuj operację **Cięcie płaszczyzną** z menu Przekształć
3. Ustaw wysokość cięcia

## Parametry

- **Wysokość cięcia** - Wysokość Z, na której obiekt zostanie przecięty (domyślnie: 10mm, zakres: 1-200mm)

## Wskazówki

- Użyj operacji Cięcie płaszczyzną, aby spłaszczyć górną część modelu na określonej wysokości
- Przydatne do przycinania importowanych modeli lub tworzenia płaskich podstaw
- Aby wykonać cięcie kształtem innym niż płaski, użyj zamiast tego operacji [Odejmij](../boolean/subtract.md) z innym obiektem
- Aby wykonać cięcie pochyloną płaszczyzną, najpierw obróć obiekt, zastosuj Cięcie płaszczyzną, a następnie obróć go z powrotem

## Powiązane

- [Część wspólna](../boolean/intersect.md) - Zachowuje tylko obszar, w którym obiekty się pokrywają
- [Odejmij](../boolean/subtract.md) - Cięcie dowolnym kształtem, nie tylko płaszczyzną
- [Wydrąż](hollow-out.md) - Tworzy pustą w środku skorupę
