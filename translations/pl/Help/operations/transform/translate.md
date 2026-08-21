---
title: Przesuń
articleKey: TranslateObject3D
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c05550dee2397bdb58dc2e247a068a544233a71d
source_lang: en
---
# Przesuń

Przesuń przemieszcza obiekt o określoną odległość wzdłuż osi X, Y i/lub Z. W przeciwieństwie do przeciągania obiektu myszą, funkcja Przesuń pozwala wprowadzić dokładne wartości przesunięcia.

<!--  Screenshot showing the Translate operation properties with X, Y, Z offset fields -->
![20260506 160828 paste 20260506 160828](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160828-paste-20260506-160828.jpg)


## Sposób użycia

1. Wybierz obiekt
2. Zastosuj operację **Przesuń** z menu Przekształć
3. Wprowadź żądane wartości przesunięcia dla X, Y i Z w panelu Właściwości

## Parametry

- **X, Y, Z** (Przesunięcie) — Odległość, o jaką obiekt zostanie przemieszczony wzdłuż każdej osi, w milimetrach. Obsługuje [wyrażenia](../../workspace/expressions.md) dla wartości obliczanych.

## Wskazówki

- Używaj funkcji Przesuń, gdy potrzebujesz precyzyjnego, powtarzalnego pozycjonowania, które można później skorygować
- Wartości przesunięcia są względne wobec bieżącej pozycji obiektu — wpisanie 10 dla X przesuwa go o 10 mm w prawo od miejsca, w którym się znajduje
- Do szybkiej zmiany położenia możesz również przeciągać obiekty bezpośrednio w widoku. Zobacz [Edytowanie obiektów](../../getting-started/editing-objects.md)

## Powiązane

- [Obróć](rotate.md) — Obróć obiekt o określony kąt
- [Skaluj](scale.md) — Precyzyjnie zmień rozmiar obiektu
- [Wyrównaj](../placement/align.md) — Ustaw obiekty względem siebie
