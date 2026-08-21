---
title: Zapisywanie i eksportowanie
parent: "Getting Started"
nav_order: 4
source_hash: 020d4bf43f07d3ab7dbd7d585e13c99309f0c0b8
source_lang: en
---
# Zapisywanie i eksportowanie

MatterCAD obsługuje kilka formatów plików do zapisywania i eksportowania projektów. Wybór formatu zależy od tego, w jaki sposób zamierzasz wykorzystać plik.

## Formaty zapisu

### MCX (format natywny)

MCX to natywny format plików MatterCAD i najlepszy wybór dla projektów, które chcesz później dalej edytować. Zachowuje on:

- Pełne drzewo projektu ze wszystkimi obiektami i ich hierarchią
- Wszystkie parametry i ustawienia każdego obiektu
- Operacje logiczne, tablice i inne operacje w formie edytowalnej
- Relacje między komponentami

**Użyj MCX, gdy:** chcesz zapisać swoją pracę i kontynuować jej edycję później.

### STL

STL to najczęściej używany format do druku 3D. Zawiera wyłącznie końcową geometrię siatki trójkątów, bez historii projektu i parametrów.

**Użyj STL, gdy:** chcesz wydrukować projekt w 3D lub udostępnić go osobie, która nie korzysta z MatterCAD.

### OBJ

OBJ (Wavefront) to popularny format 3D obsługiwany przez większość oprogramowania 3D. Podobnie jak STL zawiera wyłącznie geometrię siatki.

**Użyj OBJ, gdy:** musisz otworzyć projekt w innym oprogramowaniu 3D, takim jak Blender lub silnik gier.

### SVG

Eksport do SVG tworzy dwuwymiarowy plik wektorowy na podstawie widoku projektu z góry. Jest to przydatne przy cięciu laserowym lub frezowaniu CNC.

**Użyj SVG, gdy:** potrzebujesz dwuwymiarowego zarysu projektu do cięcia laserowego lub grawerowania.

## Jak zapisać

![20260324 080726 paste 20260324 080726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080726-paste-20260324-080726.jpg)

1. Otwórz **menu marki** (logo MatterCAD w lewym górnym rogu)
2. Wybierz **Zapisz jako**, aby wskazać lokalizację i format
3. Wybierz format pliku z listy rozwijanej formatów
4. Wskaż miejsce zapisu pliku i kliknij **Zapisz**

Twój projekt jest również zapisywany automatycznie w trakcie pracy, więc nie stracisz zmian po zamknięciu aplikacji.

## Wskazówki

- Zawsze zapisuj kopię projektu w formacie MCX przed eksportem do STL lub OBJ, aby móc później wprowadzać zmiany
- Podczas eksportu do STL wszystkie obiekty w scenie są scalane w jedną siatkę
- Jeśli musisz udostępnić projekt osobie korzystającej z MatterCAD, wyślij plik MCX, aby zachować pełną możliwość edycji
- Możesz również zapisywać projekty w [Bibliotece w chmurze](../library/cloud-library.md), aby mieć do nich dostęp z dowolnego komputera

## Powiązane

- [Dodawanie istniejących obiektów](adding-existing-objects.md) - Importuj pliki do MatterCAD
- [Biblioteka](../library/index.md) - Uporządkuj zapisane projekty
- [Biblioteka w chmurze](../library/cloud-library.md) - Przechowuj projekty w chmurze
