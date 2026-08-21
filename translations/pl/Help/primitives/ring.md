---
title: Pierścień
articleKey: RingObject3D
parent: "Primitives"
nav_order: 13
source_hash: fd16c400f3d8c8af13416ab57ddd8407e761d93a
source_lang: en
---
# Pierścień

Pusty w środku walec (rura) o niezależnych średnicach wewnętrznej i zewnętrznej oraz określonej wysokości. Znany również jako kształt rury lub tulei.

<!--  Screenshot of a Ring primitive on the workspace -->
![20260318 183848 paste 20260318 183848](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183848-paste-20260318-183848.jpg)


## Parametry

- **Średnica zewnętrzna** - Zewnętrzna szerokość pierścienia (domyślnie: 20mm)
- **Średnica wewnętrzna** - Średnica pustego środka (domyślnie: 15mm)
- **Wysokość** - Wysokość pierścienia (domyślnie: 5mm)
- **Boki** - Liczba segmentów na obwodzie (domyślnie: 40)

### Parametry zaawansowane

Włącz tryb **Zaawansowane**, aby uzyskać dodatkowe ustawienia:

- **Kąt początkowy** - Kąt, od którego zaczyna się pierścień (domyślnie: 0)
- **Kąt końcowy** - Kąt, na którym kończy się pierścień (domyślnie: 360). Ustaw wartość mniejszą niż 360, aby uzyskać niepełny pierścień
- **Zaokrąglenie** - Dodaj zaokrąglenie krawędzi (Brak, Góra lub Dół)
- **Kierunek** - Zaokrąglenie w stronę krawędzi wewnętrznej lub zewnętrznej (widoczne, gdy włączone jest Zaokrąglenie)
- **Segmenty zaokrąglenia** - Gładkość zaokrąglenia (widoczne, gdy włączone jest Zaokrąglenie)

## Wskazówki

- Grubość ścianki wynosi (Średnica zewnętrzna - Średnica wewnętrzna) / 2
- Używaj tego kształtu do podkładek, dystansów, tulei i elementów rurowych
- Ustaw dużą wysokość dla rur lub małą dla płaskich podkładek
- Użyj parametrów Kąt początkowy i Kąt końcowy, aby uzyskać niepełne pierścienie, np. pierścienie osadcze typu C

## Powiązane

- [Torus](torus.md) - Pierścień w kształcie obwarzanka o okrągłym przekroju
- [Walec](cylinder.md) - Pełna okrągła kolumna (bez pustego środka)
