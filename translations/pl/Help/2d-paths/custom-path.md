---
title: Ścieżka niestandardowa
articleKey: CustomPathObject3D
parent: "2D Paths"
nav_order: 3
source_hash: 3633c708477de3ac77d3547b730c33f7e4431cf6
source_lang: en
---
# Ścieżka niestandardowa

Narysuj własną ścieżkę 2D przy użyciu punktów kontrolnych. Daje to pełną swobodę tworzenia dowolnego kształtu 2D, który następnie można wyciągnąć lub obrócić w obiekt 3D.

<!-- Screenshot showing a custom path being edited with control points -->
![20260506 080247 paste 20260506 080247](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080247-paste-20260506-080247.jpg)


## Sposób użycia

1. Dodaj **Ścieżkę niestandardową** z biblioteki ścieżek 2D
2. Edytuj punkty kontrolne, aby zdefiniować kształt
3. Zastosuj [Wyciągnięcie liniowe](../operations/path/linear-extrude.md) lub inne operacje na ścieżkach, aby utworzyć obiekt 3D

## Ścieżki otwarte i zamknięte

Pole wyboru **Zamknięty** decyduje o tym, czy ścieżka łączy swój ostatni punkt z pierwszym.

- **Zamknięty** (ustawienie domyślne) sprawia, że ścieżka obrysowuje obszar. To właśnie ten obszar wypełniają [Wyciągnięcie liniowe](../operations/path/linear-extrude.md) i [Obrót (Revolve)](../operations/path/revolve.md).
- **Otwórz** sprawia, że ścieżka staje się linią. Linia niczego nie otacza, więc w scenie jest widoczna jako cienka wstęga biegnąca wzdłuż swojej długości, a nie jako wypełniony kształt. Użyj operacji [Rozszerz ścieżkę](../operations/path/inflate-path.md), aby nadać jej szerokość i ponownie zamienić ją w coś pełnego.

Dwie rzeczy, o których warto wiedzieć przed odznaczeniem opcji **Zamknięty**:

- **Ponowne zamknięcie to nie cofnięcie.** Otwarcie ścieżki usuwa jej segment zamykający. Jeśli segment ten był krzywą, ponowne zaznaczenie opcji **Zamknięty** przywróci linię prostą, a nie krzywą. Zamiast tego użyj Ctrl+Z — cofnięcie przywraca oryginalną ścieżkę dokładnie taką, jaka była.
- **Niektóre kontury nie dają się otworzyć.** Kontur, w którym pozostałyby mniej niż dwa punkty — na przykład kropla narysowana jako pojedynczy punkt i krzywa zawracająca do niego — pozostaje zamknięty, zamiast zapaść się w coś, czego nie dałoby się już zobaczyć ani kliknąć. Tak samo zachowuje się kontur zawierający krzywą kwadratową, jaka może wystąpić w zaimportowanym pliku SVG: jego otwarcie spłaszczyłoby krzywą do narożnika. Odmowa dotyczy pojedynczego konturu, więc pozostała część ścieżki i tak zostanie otwarta.

Jeśli ścieżka ma kilka konturów i nie są one ze sobą zgodne, pole wyboru pokazuje stan otwarty. Zaznaczenie go ujednolica wszystkie kontury.

Operacje wymagające obszaru same zamkną otwartą ścieżkę, zamiast ją odrzucić. Robią tak Wyciągnięcie liniowe, Obrót (Revolve), Odejmij oraz pozostałe operacje logiczne, więc otwarta ścieżka daje po wyciągnięciu tę samą bryłę co jej zamknięta wersja.

## Wskazówki

- Używaj Ścieżki niestandardowej, gdy żaden z wbudowanych kształtów ścieżek nie odpowiada Twoim potrzebom
- Aby zaimportować kształty z zewnętrznych edytorów wektorowych, zobacz [Obiekt SVG](../primitives/svg-object.md)
- Aby narysować linię i zamienić ją w część, odznacz opcję **Zamknięty**, zastosuj [Rozszerz ścieżkę](../operations/path/inflate-path.md), aby nadać jej grubość, a następnie [Wyciągnięcie liniowe](../operations/path/linear-extrude.md), aby nadać jej wysokość

## Powiązane

- [Ścieżka Okrąg](circle-path.md) — gotowy okrąg
- [Ścieżka Prostopadłościan](box-path.md) — gotowy prostokąt
- [Obiekt SVG](../primitives/svg-object.md) — importuj ścieżki wektorowe z plików SVG
- [Wyciągnięcie liniowe](../operations/path/linear-extrude.md) — nadaj ścieżkom wysokość
