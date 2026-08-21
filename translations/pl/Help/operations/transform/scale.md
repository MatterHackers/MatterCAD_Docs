---
title: Skaluj
articleKey: ScaleObject3D_3
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b3b5419c3db29550b2544bb6aca91ca3ce6fa715
source_lang: en
---
# Skaluj

Skaluj zmienia rozmiar obiektu z precyzyjną kontrolą nad wymiarami, proporcjami i konwersją jednostek. Możesz skalować równomiernie, zablokować wybrane osie razem lub zmieniać rozmiar każdej osi niezależnie.

<!--  Screenshot showing the Scale operation properties with dimension fields and lock proportion options -->
![20260506 160759 paste 20260506 160759](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160759-paste-20260506-160759.jpg)

## Sposób użycia

1. Wybierz obiekt
2. Zastosuj operację **Skaluj** z menu Przekształć
3. Wybierz metodę skalowania i wprowadź żądane wartości

Możesz również skalować obiekty w widoku roboczym, klikając i przeciągając narożne uchwyty skalowania na wybranym obiekcie.

## Parametry

### Typ skalowania

Wybierz ustawienie predefiniowane lub niestandardowe:

- **Niestandardowy** — wprowadź własne wymiary lub wartości procentowe
- **Cale na mm** — pomnóż przez 25,4 (konwersja z jednostek imperialnych na metryczne)
- **mm na cale** — pomnóż przez 0,0393 (konwersja z jednostek metrycznych na imperialne)
- **mm na cm** — pomnóż przez 0,1
- **cm na mm** — pomnóż przez 10

### Metoda skalowania (tryb Niestandardowy)

- **Bezpośredni** — wprowadź żądaną Szerokość, Głębokość i Wysokość w milimetrach
- **Wartość procentowa** — wprowadź Szerokość, Głębokość i Wysokość jako wartości procentowe rozmiaru pierwotnego

### Zablokuj proporcje

- **Brak (Skaluj swobodnie)** — każda oś skalowana jest niezależnie
- **X i Y** — Szerokość i Głębokość są zablokowane razem; Wysokość skalowana jest niezależnie
- **X, Y i Z** — wszystkie trzy osie skalowane są równomiernie razem

### Wymiary

- **Szerokość** — rozmiar wzdłuż osi X
- **Głębokość** — rozmiar wzdłuż osi Y
- **Wysokość** — rozmiar wzdłuż osi Z

## Wskazówki

- Użyj opcji „Cale na mm”, jeśli zaimportowany plik STL został zaprojektowany w calach i wydaje się zbyt mały
- Ustaw Zablokuj proporcje na X, Y i Z, aby skalować równomiernie — zmiana dowolnego wymiaru aktualizuje wszystkie pozostałe
- Położenie podstawy obiektu jest zachowywane podczas skalowania, dzięki czemu obiekt pozostaje na powierzchni obszaru roboczego
- Możesz wpisać dokładne wartości, aby precyzyjnie określić rozmiar, lub użyć suwaków do szybkich korekt

## Powiązane

- [Przesuń](translate.md) — przesuwanie obiektu
- [Obróć](rotate.md) — obracanie obiektu
- [Dopasuj do granic](../placement/fit-to-bounds.md) — skalowanie tak, aby zmieścić się w określonym rozmiarze
