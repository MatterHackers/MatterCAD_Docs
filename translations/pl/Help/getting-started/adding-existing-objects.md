---
title: Dodawanie istniejących obiektów
parent: "Getting Started"
nav_order: 1
source_hash: e384a5c024336c3c58343d262d914fa40e0b0426
source_lang: en
---
# Dodawanie istniejących obiektów

Istniejące modele 3D możesz wczytać do MatterCAD, importując pliki z komputera lub dodając zawartość z wbudowanej biblioteki.

## Z komputera

![20260324 081143 paste 20260324 081143](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081143-paste-20260324-081143.jpg)

![20260324 081240 paste 20260324 081240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081240-paste-20260324-081240.jpg)


Kliknij przycisk **Otwórz** na pasku narzędzi, aby przeglądać i dodawać pliki z komputera. MatterCAD obsługuje następujące formaty importu:

- **STL** (.stl) — standardowy w branży format modeli 3D, szeroko stosowany w druku 3D
- **AMF** (.amf) — zaawansowany format obsługujący kolory i obiekty wielomateriałowe
- **OBJ** (.obj) — format grafiki 3D Wavefront (wyłącznie geometria siatki)
- **3MF** (.3mf) — 3D Manufacturing Format z rozbudowaną obsługą metadanych
- **MCX** (.mcx) — natywny format MatterCAD, zachowujący wszystkie dane i parametry projektu
- **SVG** (.svg) — Scalable Vector Graphics, importowany jako ścieżki 2D
- **TTF / OTF** (.ttf, .otf) — pliki czcionek do użycia z narzędziem Tekst

## Przeciąganie i upuszczanie

Możesz również przeciągać i upuszczać pliki bezpośrednio z pulpitu lub eksploratora plików do obszaru roboczego MatterCAD. Obsługiwane typy plików zostaną zaimportowane automatycznie.

![20260324 081416 paste 20260324 081416](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081416-paste-20260324-081416.jpg)

## Z Biblioteki

### Panel boczny Biblioteki

Kliknij przycisk **Dodaj zawartość** na pasku narzędzi, aby otworzyć panel przeglądarki biblioteki. Możesz w nim:

- Przeglądać zapisane projekty
- Przejść do biblioteki Prymitywy z wbudowanymi kształtami
- Uzyskać dostęp do Biblioteki w chmurze po zalogowaniu
- Przeciągnąć i upuścić dowolny element z biblioteki bezpośrednio do obszaru roboczego

![20260324 081446 paste 20260324 081446](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081446-paste-20260324-081446.jpg)

### Karta Biblioteka

Możesz również skorzystać z karty Biblioteka, aby przeglądać swoje kolekcje. Kliknij prawym przyciskiem myszy dowolny obiekt w bibliotece i wybierz **Dodaj do sceny**, aby zaimportować go do bieżącego obszaru roboczego projektu.

![20260324 081536 paste 20260324 081536](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081536-paste-20260324-081536.jpg)

## Wskazówki

- MCX to najlepszy format do późniejszej ponownej edycji projektów, ponieważ zachowuje wszystkie parametry oraz drzewo projektu
- Pliki STL zawierają wyłącznie geometrię siatki. Po zaimportowaniu pliku STL nadal możesz stosować na nim operacje, ale nie możesz edytować pierwotnych parametrów
- Przy importowaniu wielu plików każdy z nich staje się osobnym obiektem w scenie. Użyj operacji [Grupuj](../workspace/grouping.md), aby je uporządkować

## Powiązane

- [Tworzenie nowych obiektów](creating-new-objects.md) — rozpocznij projekt od zera z użyciem prymitywów
- [Zapisywanie i eksportowanie](saving-and-exporting.md) — zapisuj i eksportuj ukończone projekty
- [Biblioteka](../library/index.md) — dowiedz się więcej o porządkowaniu biblioteki projektów
