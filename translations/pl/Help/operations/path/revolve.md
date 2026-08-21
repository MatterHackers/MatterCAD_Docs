---
title: Obrót (Revolve)
articleKey: RevolveObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: a63ebb08d982178e0e59f0b9f07c3c0dca53148b
source_lang: en
---
# Obrót (Revolve)

Obrót (Revolve) obraca ścieżkę 2D wokół osi, tworząc bryłę obrotową 3D. W ten sposób tworzysz wazony, misy, koła i inne obiekty o symetrii obrotowej.

<!--  Before and after showing a profile path being revolved into a vase shape -->
![20260506 102004 paste 20260506 102004](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-102004-paste-20260506-102004.jpg)


## Sposób użycia

1. Wybierz ścieżkę 2D
2. Zastosuj operację **Obrót (Revolve)** z menu operacji na ścieżkach
3. Dostosuj zakres obrotu, pozycję osi oraz liczbę boków

## Parametry

- **Obrót** - Całkowity kąt obrotu dla operacji obrotu (domyślnie: 0, zakres: 0-360). Ustaw 360, aby uzyskać pełny obrót.
- **Pozycja osi** - Przesunięcie osi obrotu względem środka ścieżki (domyślnie: 0, zakres: od -30 do 30). Wartość dodatnia odsuwa oś od ścieżki, tworząc większy otwór.
- **Kąt początkowy** - Miejsce, w którym rozpoczyna się obrót (domyślnie: 0)
- **Kąt końcowy** - Miejsce, w którym kończy się obrót (domyślnie: 45). Ustaw 360, aby uzyskać pełny obrót.
- **Boki** - Liczba segmentów wzdłuż obrotu (domyślnie: 30). Więcej = gładsza powierzchnia.

## Wskazówki

- Użyj **Pozycji osi**, aby kontrolować średnicę wewnętrzną obracanego kształtu
- Ustaw **Kąt początkowy** i **Kąt końcowy** na wartość mniejszą niż 360, aby utworzyć częściowe obroty (łuki, rynny)
- Narysuj ścieżkę profilu wazonu lub misy, a następnie obróć ją, aby uzyskać idealną symetrię
- [Ścieżka Okrąg](../../2d-paths/circle-path.md) po obróceniu tworzy torus

## Powiązane

- [Wyciągnięcie liniowe](linear-extrude.md) - Wyciągnij prosto w górę zamiast obracać
- [Ścieżki 2D](../../2d-paths/index.md) - Twórz ścieżki profilu do obracania
- [Torus](../../primitives/torus.md) - Gotowy kształt pierścienia utworzony przez obrót
