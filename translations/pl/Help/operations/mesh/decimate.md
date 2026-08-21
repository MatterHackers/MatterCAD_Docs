---
title: Zmniejsz
articleKey: DecimateObject3D
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 58a2573b968808e98203832142fa8bacf7a9cf99
source_lang: en
---
# Zmniejsz (Decymacja)

Zmniejsz obniża liczbę wielokątów siatki, zachowując ogólny kształt. Jest to przydatne do upraszczania bardzo szczegółowych modeli, zmniejszania rozmiaru pliku oraz przyspieszania operacji na złożonej geometrii.

![20260324 080430 paste 20260324 080430](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080430-paste-20260324-080430.jpg)


## Sposób użycia

1. Wybierz obiekt
2. Zastosuj operację **Zmniejsz** z menu Siatka
3. Wybierz cel (liczbę lub wartość procentową) i dostosuj go

## Parametry

- **Tryb** - Wybierz sposób określenia celu:
  - **Procent** - Zachowaj określony procent oryginalnych wielokątów (domyślnie: 50%)
  - **Liczba** - Ustaw konkretną docelową liczbę wielokątów
- **Źródłowa liczba wielokątów** - Pierwotna liczba wielokątów (tylko do odczytu)
- **Docelowy procent** - Procent wielokątów do zachowania (widoczny w trybie Procent)
- **Docelowa liczba** - Dokładna liczba wielokątów do zachowania (widoczna w trybie Liczba)
- **Liczba po redukcji procentowej** - Końcowa liczba wielokątów po redukcji procentowej (tylko do odczytu)
- **Zachowaj powierzchnię** - Rzutuje wierzchołki z powrotem na oryginalną powierzchnię w celu uzyskania większej dokładności (wolniej, ale wierniej wobec oryginalnego kształtu)

## Wskazówki

- Redukcja o 50% zwykle dobrze zachowuje jakość wizualną
- Włącz opcję Zachowaj powierzchnię, gdy dokładność jest ważniejsza niż szybkość
- Zmniejszenie liczby wielokątów przyspiesza operacje logiczne na złożonych zaimportowanych modelach
- Bardzo mała liczba wielokątów w widoczny sposób pogorszy kształt -- sprawdź wynik przed zatwierdzeniem

## Powiązane

- [Napraw](repair.md) - Naprawa problemów z siatką
