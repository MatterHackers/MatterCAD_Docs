---
title: Rozszerz ścieżkę
articleKey: InflatePathObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: c0e11d3d24c5f832f797cde4d392e26a4694733d
source_lang: en
---
# Rozszerz ścieżkę

Rozszerz ścieżkę powiększa ścieżkę 2D na zewnątrz, zwiększając kształt przy zachowaniu jego ogólnej formy. Działa to podobnie do zastosowania równomiernego odsunięcia wszystkich krawędzi.

<!--  Before and after showing a path inflated outward -->
![20260506 100652 paste 20260506 100652](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100652-paste-20260506-100652.jpg)


## Sposób użycia

1. Wybierz ścieżkę 2D
2. Zastosuj **Rozszerz ścieżkę** z menu operacji Ścieżka
3. Dostosuj wartość rozszerzenia

## Rozszerzanie otwartej linii

Rozszerz to sposób na zamianę linii w kształt. Odznacz opcję **Zamknięty** w [Ścieżce niestandardowej](../../2d-paths/custom-path.md), aby narysować otwartą linię, a następnie ją rozszerz: wynikiem jest wypełniona wstęga o szerokości równej ustawionej wartości po obu stronach linii. Od tego momentu wyciąga się ją tak samo jak każdą inną ścieżkę.

**Styl** określa sposób zakończenia obu końców linii, a także sposób łączenia jej narożników:

- **Płaski** kończy wstęgę prosto w każdym punkcie końcowym
- **Zaokrąglenie** dodaje półokrąg za każdym punktem końcowym
- **Ostry** dodaje kwadrat za każdym punktem końcowym

Otwarta linia nie ma wnętrza, do którego mogłaby się skurczyć, więc wartość zerowa lub ujemna nie pozostawiłaby zupełnie niczego. Gdy ścieżka jest *całkowicie* otwarta, operacja Rozszerz ogranicza wartość w górę do niewielkiej liczby dodatniej i wpisuje ograniczoną liczbę z powrotem do pola, dzięki czemu widać, co się stało.

Ścieżka łącząca kontury otwarte i zamknięte nie podlega temu ograniczeniu: kontury zamknięte kurczą się normalnie, a otwarte po prostu znikają. Ścieżki zamknięte nadal kurczą się przy wartościach ujemnych dokładnie tak jak zawsze.

## Wskazówki

- Używaj wartości ujemnych, aby zamiast rozszerzać, zwężać ścieżkę do wewnątrz
- Rozszerz przydaje się do tworzenia odsunięć tolerancyjnych wokół kształtów
- Połącz z [Ścieżką konturu](outline-path.md), aby tworzyć obramowania o określonej szerokości

## Powiązane

- [Ścieżka konturu](outline-path.md) – Utwórz kontur na podstawie ścieżki
- [Ścieżka obramowania](border-path.md) – Dodaj odsunięcie obramowania
- [Wygładź ścieżkę](smooth-path.md) – Zaokrąglij narożniki ścieżki
