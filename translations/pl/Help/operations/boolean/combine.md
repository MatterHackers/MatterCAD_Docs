---
title: Połącz
articleKey: CombineObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: a3066faa634b5a88a2fe1650a4e2ac278ac50e24
source_lang: en
---
# Połącz

Połącz scala wszystko w jedną bryłę. Wewnętrzne ściany w miejscach, w których kształty się nakładały, zostają usunięte, więc wynikiem jest jedna ciągła siatka, a nie nakładające się powłoki.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_combine -->
![boolean_combine](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_combine.png)

Operacje Połącz, [Odejmij](subtract.md), [Część wspólna](intersect.md) i [Odejmij i zamień](subtract-and-replace.md) są wykonywane przez jeden obiekt logiczny (Boolean) — przycisk na pasku narzędzi tworzy go z już wybraną operacją Połącz, a w dowolnej chwili możesz przełączyć się na jedną z trzech pozostałych w rzędzie ikon **Operacja** u góry panelu Właściwości.

Połącz działa na bryłach i na ścieżkach 2D. Sprawdza, co zostało jej przekazane, i wykonuje właściwy rodzaj operacji, więc połączenie dwóch ścieżek daje jedną ścieżkę, a połączenie dwóch siatek daje jedną bryłę.

## Sposób użycia

1. Wybierz dwa lub więcej obiektów
2. Kliknij **Połącz** na pasku narzędzi
3. Zmień zdanie w dowolnym momencie, klikając inną ikonę w rzędzie **Operacja** u góry panelu Właściwości — kształt zostanie przebudowany z użyciem nowej operacji

## Parametry

- **Operacja** — która operacja logiczna ma zostać wykonana. Wyświetlana jako rząd ikon u góry panelu
- **Zachowaj geometrię odwróconą na lewą stronę** — traktuje powłokę odwróconą na lewą stronę jako materiał bryły, zamiast pozwolić jej znieść otaczającą ją objętość. Włącz tę opcję, gdy model, który powinien być pełną bryłą, wraca z brakującymi fragmentami. Wymusza wolniejszy, dokładny mechanizm operacji logicznych
- **Napraw kolejność nawijania** — odwraca powłoki wywrócone na lewą stronę w każdej części przed wykonaniem operacji logicznej. Naprawia to geometrię raz, zamiast zmieniać to, co każda kolejna operacja uznaje za bryłę, i zwykle jest lepszym z dwóch rozwiązań problemu modelu odwróconego na lewą stronę

## Wskazówki

- Połącz nadal scali nienakładające się obiekty w jedną siatkę, ale wizualnie pozostaną one oddzielne
- Połącz obsługuje za Ciebie obiekty Otwór: wszystko oznaczone jako otwór jest odejmowane od wyniku, a nie do niego dodawane
- Połącz przenosi kolory poszczególnych ścian z obiektów źródłowych
- Jeśli wynik wygląda niepoprawnie, sprawdź, czy obiekty źródłowe są wodoszczelne. **Napraw kolejność nawijania** naprawia powłoki odwrócone na lewą stronę; [Napraw](../mesh/repair.md) usuwa szersze uszkodzenia w importowanych modelach

## Powiązane

- [Odejmij](subtract.md) — wytnij jeden kształt z drugiego
- [Część wspólna](intersect.md) — zachowaj tylko objętość, w której obiekty się nakładają
- [Odejmij i zamień](subtract-and-replace.md) — odejmij jeden kształt i zachowaj wyciętą część
- [Cięcie płaszczyzną](../reshape/plane-cut.md) — tnij płaską płaszczyzną zamiast innym kształtem
- [Otwór](../../primitives/hole.md) — sześcian wstępnie skonfigurowany do odejmowania
- [Napraw](../mesh/repair.md) — napraw uszkodzone importowane siatki przed operacją logiczną

Ta strona obejmuje również starsze obiekty Połącz, wciąż spotykane w projektach zapisanych przed scaleniem operacji. Działają dokładnie tak jak wcześniej; nowe projekty używają wspólnego obiektu logicznego (Boolean) z wybraną operacją Połącz.
