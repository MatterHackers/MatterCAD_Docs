---
title: Obiekt SVG
articleKey: SvgObject3D
parent: "Primitives"
nav_order: 15
source_hash: dab97cdde74d938b5612d959f83b54b4a04a49da
source_lang: en
---
# Obiekt SVG

Importuj pliki SVG (Scalable Vector Graphics) i używaj ich jako ścieżek 2D w swoim projekcie. Pliki SVG można następnie wyciągnąć do kształtów 3D za pomocą operacji [Wyciągnięcie liniowe](../operations/path/linear-extrude.md) lub [Obrót (Revolve)](../operations/path/revolve.md).

<!--  Screenshot showing an imported SVG path being extruded into a 3D shape -->
![20260318 184807 paste 20260318 184807](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184807-paste-20260318-184807.jpg)



## Jak używać

1. Zaimportuj plik SVG, przeciągając go na obszar roboczy lub używając przycisku Otwórz
2. Plik SVG zostanie zaimportowany jako ścieżka 2D
3. Zastosuj [Wyciągnięcie liniowe](../operations/path/linear-extrude.md), aby nadać jej wysokość, lub użyj innych [operacji na ścieżkach](../operations/path/index.md)

## Wskazówki

- Pliki SVG powinny zawierać wypełnione kształty lub zamknięte ścieżki, aby uzyskać najlepsze rezultaty
- Złożone pliki SVG z wieloma ścieżkami mogą wymagać dłuższego przetwarzania
- Użyj operacji [Wybierz ścieżki](../operations/path/select-paths.md), aby pracować z określonymi częściami wielościeżkowego pliku SVG
- W internecie dostępnych jest wiele darmowych plików SVG z logo, ikonami i wzorami dekoracyjnymi

## Powiązane

- [Obraz na ścieżkę](../operations/image/image-to-path.md) – konwertuj obrazy rastrowe na ścieżki zamiast używać SVG
- [Tekst](text.md) – twórz tekst bezpośrednio, bez potrzeby stosowania SVG
- [Wyciągnięcie liniowe](../operations/path/linear-extrude.md) – nadaj płaskim ścieżkom wysokość
- [Ścieżki 2D](../2d-paths/index.md) – wbudowane prymitywy ścieżek
