---
title: Odejmij
articleKey: SubtractObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 59685bd0a635b70d7f938780f71e90be595dd993
source_lang: en
---
# Odejmij

Odejmij wycina wybrane części z części, których nie wybrano. Użyj opcji **Część(-i) do odjęcia**, aby wskazać kształty tnące; wszystko pozostałe stanowi bazę, która zostanie przycięta.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract -->
![boolean_subtract](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract.png)

[Połącz](combine.md), Odejmij, [Część wspólna](intersect.md) i [Odejmij i zamień](subtract-and-replace.md) są wykonywane przez jeden obiekt Boole'a — przycisk na pasku narzędzi tworzy go z już wybraną operacją Odejmij, a w dowolnej chwili możesz przełączyć się na jedną z pozostałych trzech w rzędzie ikon **Operacja** u góry panelu Właściwości.

Odejmij działa na bryłach oraz na ścieżkach 2D. Sprawdza, co zostało przekazane, i wykonuje właściwy rodzaj operacji, więc odjęcie jednej ścieżki od drugiej daje ścieżkę, a odjęcie jednej siatki od drugiej daje bryłę.

## Sposób użycia

1. Wybierz dwa lub więcej obiektów
2. Kliknij **Odejmij** na pasku narzędzi — domyślna część do wycięcia zostanie wybrana automatycznie, aby operacja od razu przyniosła efekt
3. Użyj opcji **Część(-i) do odjęcia**, aby wskazać, które obiekty podrzędne są kształtami tnącymi
4. Możesz zmienić zdanie w dowolnym momencie, klikając inną ikonę w rzędzie **Operacja** u góry panelu Właściwości — kształt zostanie przebudowany z nową operacją

## Parametry

- **Operacja** – Która operacja logiczna ma zostać wykonana. Wyświetlana jako rząd ikon u góry panelu
- **Część(-i) do odjęcia** – Które obiekty podrzędne są kształtami tnącymi
- **Zachowaj odjęte części** – Pozostawia wycięte części w scenie zamiast je odrzucać
- **Zachowaj geometrię odwróconą na lewą stronę** – Traktuje powłokę odwróconą na lewą stronę jako materiał pełny, zamiast pozwalać jej zniwelować otaczającą ją objętość. Włącz tę opcję, gdy model, który powinien być pełny, wraca z brakującymi fragmentami. Wymusza użycie wolniejszego, dokładnego silnika operacji logicznych
- **Napraw kolejność nawijania** – Odwraca powłoki wywrócone na lewą stronę w każdej części przed wykonaniem operacji logicznej. Naprawia to geometrię raz na zawsze, zamiast zmieniać to, co każda kolejna operacja uznaje za materiał pełny, i zwykle jest lepszym z dwóch rozwiązań problemu modelu odwróconego na lewą stronę

## Wskazówki

- Obiekty muszą się przenikać, aby operacja Odejmij dała jakikolwiek efekt
- Aby wyciąć otwór na wylot, upewnij się, że obiekt tnący przechodzi całkowicie przez bazę
- W przypadku prostego otworu prymityw [Otwór](../../primitives/hole.md) jest już skonfigurowany do odejmowania
- Obiekty tnące pozostają w drzewie projektu, więc możesz je przesuwać lub zmieniać ich rozmiar, a wycięcie zostanie zaktualizowane
- Jeśli wynik wygląda niepoprawnie, sprawdź, czy obiekty źródłowe są szczelne. **Napraw kolejność nawijania** naprawia powłoki odwrócone na lewą stronę; [Napraw](../mesh/repair.md) usuwa poważniejsze uszkodzenia w zaimportowanych modelach

## Powiązane

- [Połącz](combine.md) – Scal wiele obiektów w jeden kształt pełny
- [Część wspólna](intersect.md) – Zachowaj tylko objętość, w której obiekty się przenikają
- [Odejmij i zamień](subtract-and-replace.md) – Odejmij jeden kształt i zachowaj wycięty fragment
- [Cięcie płaszczyzną](../reshape/plane-cut.md) – Tnij płaską płaszczyzną zamiast innym kształtem
- [Otwór](../../primitives/hole.md) – Sześcian wstępnie skonfigurowany do odejmowania
- [Napraw](../mesh/repair.md) – Napraw uszkodzone zaimportowane siatki przed operacją logiczną

Ta strona obejmuje również starsze obiekty Odejmij, wciąż występujące w projektach zapisanych przed scaleniem operacji. Działają dokładnie tak jak wcześniej; nowe projekty używają wspólnego obiektu Boole'a z wybraną operacją Odejmij.
