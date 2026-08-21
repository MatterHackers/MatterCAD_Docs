---
title: Dopasuj do granic
articleKey: FitToBoundsObject3D_4
parent: "Placement Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: 91b9c917cb636f28403c291a4d56f22bf6758b70
source_lang: en
---
# Dopasuj do granic

Dopasuj do granic skaluje obiekt tak, aby zmieścił się w zadanych wymiarach szerokości, głębokości i wysokości. Możesz kontrolować sposób rozciągania i wyrównania obiektu w obrębie docelowych granic.

<!--  Screenshot showing an object being fit to specific bounding dimensions -->
![20260506 154930 paste 20260506 154930](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-154930-paste-20260506-154930.jpg)

## Sposób użycia

1. Wybierz obiekt
2. Zastosuj operację **Dopasuj do granic** z menu Rozmieszczenie
3. Wprowadź wymiary docelowe
4. Wybierz blokowanie proporcji i sposób rozciągania

## Parametry

- **Zablokuj proporcje** - Sposób ograniczenia proporcji:
  - **Brak** - Każdą oś można ustawić niezależnie
  - **X i Y** - Szerokość i głębokość są ze sobą powiązane
  - **X, Y i Z** - Równomierne skalowanie we wszystkich osiach
- **Szerokość** - Docelowa szerokość (wymiar X)
- **Głębokość** - Docelowa głębokość (wymiar Y)
- **Wysokość** - Docelowa wysokość (wymiar Z)

### Gdy Zablokuj proporcje ma wartość X i Y lub X, Y i Z

- **Rozciągnij** - Sposób dopasowania obiektu:
  - **Wewnątrz** - Pomniejszenie tak, aby obiekt w całości zmieścił się w granicach (mogą pozostać odstępy)
  - **Rozwiń** - Powiększenie tak, aby wypełnić granice (w niektórych wymiarach może je przekroczyć)

### Gdy Zablokuj proporcje ma wartość Brak

Każda oś ma własne ustawienia:

- **Rozciągnij** - Wewnątrz lub Rozwiń dla każdej osi
- **Wyrównaj** - Miejsce ustawienia w obrębie granic (Min., Środek, Maks.)

## Wskazówki

- Użyj tej operacji, aby zmienić rozmiar importowanych modeli do dokładnych wymiarów docelowych
- Zablokuj wszystkie proporcje, aby uzyskać równomierne skalowanie zachowujące pierwotny kształt
- Korzystaj z kontroli dla poszczególnych osi, gdy musisz dopasować konkretną szerokość, a pozostałe wymiary nie mają znaczenia

## Powiązane

- [Skaluj](../transform/scale.md) - Skalowanie według współczynnika lub procentu zamiast rozmiaru docelowego
- [Dopasuj do walca](fit-to-cylinder.md) - Dopasowanie w obrębie granicy walcowej
- [Wyrównaj](align.md) - Ustawianie pozycji obiektów względem siebie
