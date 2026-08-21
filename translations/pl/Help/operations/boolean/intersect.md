---
title: Część wspólna
articleKey: IntersectionObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: b997cfc4f6d2f02559346365311f217388a6a2da
source_lang: en
---
# Część wspólna

Część wspólna zachowuje wyłącznie objętość współdzieloną przez wszystkie obiekty, a resztę odrzuca.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_intersect -->
![boolean_intersect](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_intersect.png)

[Połącz](combine.md), [Odejmij](subtract.md), Część wspólna i [Odejmij i zamień](subtract-and-replace.md) są wykonywane przez jeden obiekt logiczny (Boolean) — przycisk na pasku narzędzi tworzy go z już wybraną operacją Część wspólna, a w dowolnej chwili możesz przełączyć się na jedną z pozostałych trzech w rzędzie ikon **Operacja** u góry panelu Właściwości.

Część wspólna działa na bryłach oraz na ścieżkach 2D. Analizuje to, co jej przekażesz, i wykonuje odpowiedni rodzaj operacji, więc część wspólna dwóch ścieżek daje jedną ścieżkę, a część wspólna dwóch siatek daje jedną bryłę.

## Jak używać

1. Wybierz dwa lub więcej obiektów
2. Kliknij **Część wspólna** na pasku narzędzi
3. W dowolnym momencie zmień zdanie, klikając inną ikonę w rzędzie **Operacja** u góry panelu Właściwości — kształt zostanie przebudowany z nową operacją

## Parametry

- **Operacja** — którą operację logiczną wykonać. Wyświetlana jako rząd ikon u góry panelu
- **Zachowaj geometrię odwróconą na lewą stronę** — traktuj powłokę odwróconą na lewą stronę jako materiał pełny, zamiast pozwalać jej znosić otaczającą ją objętość. Włącz tę opcję, gdy model, który powinien być pełny, wraca z brakującymi fragmentami. Wymusza wolniejszy, dokładny mechanizm operacji logicznych
- **Napraw kolejność nawijania** — przed wykonaniem operacji logicznej odwraca nawinięcie powłok wywróconych na lewą stronę w każdej części. Naprawia to geometrię raz na zawsze, zamiast zmieniać to, co każda kolejna operacja uznaje za materiał pełny, i zwykle jest lepszą z dwóch odpowiedzi na model odwrócony na lewą stronę

## Wskazówki

- Obiekty muszą się przenikać. Jeśli w rzeczywistości się nie przenikają, wynik będzie pusty
- Przy więcej niż dwóch obiektach operacja przebiega po kolei: najpierw wyznaczana jest część wspólna dwóch pierwszych, następnie tego wyniku z trzecim i tak dalej
- Jeśli wynik wygląda nieprawidłowo, sprawdź, czy obiekty źródłowe są szczelne. **Napraw kolejność nawijania** naprawia powłoki odwrócone na lewą stronę; [Napraw](../mesh/repair.md) usuwa poważniejsze uszkodzenia w importowanych modelach

## Powiązane

- [Połącz](combine.md) — scal wiele obiektów w jeden pełny kształt
- [Odejmij](subtract.md) — wytnij jeden kształt z drugiego
- [Odejmij i zamień](subtract-and-replace.md) — odejmij jeden kształt i zachowaj wyciętą część
- [Cięcie płaszczyzną](../reshape/plane-cut.md) — tnij płaską płaszczyzną zamiast innym kształtem
- [Napraw](../mesh/repair.md) — napraw uszkodzone importowane siatki przed operacją logiczną

Ta strona opisuje także starsze obiekty Przecięcie, wciąż spotykane w projektach zapisanych przed scaleniem operacji. Działają dokładnie tak jak wcześniej; nowe projekty korzystają ze wspólnego obiektu logicznego (Boolean) z wybraną operacją Część wspólna.
