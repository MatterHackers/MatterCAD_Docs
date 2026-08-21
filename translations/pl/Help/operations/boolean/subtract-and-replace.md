---
title: Odejmij i zastąp
articleKey: SubtractAndReplaceObject3D_2
parent: "Boolean Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: c1698bab75faca8046b23cc148803c8063ba0678
source_lang: en
---
# Odejmij i zastąp

Odejmij i zastąp odejmuje wybrane części od tych, których nie wybrano, ale zamiast odrzucać odciętą bryłę, zachowuje ją jako osobną część. Użyj opcji **Część(-i) do odjęcia**, aby wskazać kształty tnące; wszystko pozostałe stanowi bazę, która zostanie przycięta.

<!-- AUTO_IMAGE: type=from_mcx file=boolean_subtract_and_replace -->
![boolean_subtract_and_replace](https://matterhackers.github.io/MatterCAD_Docs/assets/boolean_subtract_and_replace.png)

[Połącz](combine.md), [Odejmij](subtract.md), [Część wspólna](intersect.md) oraz Odejmij i zastąp są wykonywane przez jeden obiekt logiczny (Boolean) -- przycisk na pasku narzędzi tworzy go z już wybraną operacją Odejmij i zastąp, a w dowolnej chwili możesz przełączyć się na dowolną z pozostałych trzech w rzędzie ikon **Operacja** u góry panelu Właściwości.

Odejmij i zastąp nie jest dostępne dla ścieżek 2D -- obszar nie ma usuniętej objętości, którą można by zwrócić.

## Jak używać

1. Zaznacz dwa lub więcej obiektów
2. Kliknij **Odejmij i zastąp** na pasku narzędzi
3. Użyj opcji **Część(-i) do odjęcia**, aby wybrać, które obiekty podrzędne są kształtami tnącymi
4. W dowolnej chwili zmień decyzję, klikając inną ikonę w rzędzie **Operacja** u góry panelu Właściwości -- kształt zostanie przebudowany z nową operacją

## Parametry

- **Operacja** - Która operacja logiczna ma zostać wykonana. Wyświetlana jako rząd ikon u góry panelu
- **Część(-i) do odjęcia** - Które obiekty podrzędne są kształtami tnącymi
- **Zachowaj geometrię odwróconą na lewą stronę** - Traktuj powłokę odwróconą na lewą stronę jako materiał pełny, zamiast pozwalać jej znosić otaczającą ją objętość. Włącz tę opcję, gdy model, który powinien być pełny, wraca z brakującymi fragmentami. Wymusza to użycie wolniejszego, dokładnego silnika operacji logicznych
- **Napraw kolejność nawijania** - Odwraca powłoki odwrócone na lewą stronę w każdej części przed wykonaniem operacji logicznej. Naprawia to geometrię raz, zamiast zmieniać to, co każda kolejna operacja uznaje za materiał pełny, i zwykle jest lepszym z dwóch rozwiązań problemu modelu odwróconego na lewą stronę

## Wskazówki

- Obie części pasują do siebie idealnie, ponieważ powstały w tej samej operacji
- Używaj tej operacji w projektach wielokolorowych, zazębiających się złożeniach i intarsjach
- Jeśli wynik wygląda nieprawidłowo, sprawdź, czy obiekty źródłowe są wodoszczelne. **Napraw kolejność nawijania** naprawia powłoki odwrócone na lewą stronę; [Napraw](../mesh/repair.md) usuwa poważniejsze uszkodzenia w importowanych modelach

## Powiązane

- [Połącz](combine.md) - Scal wiele obiektów w jeden pełny kształt
- [Odejmij](subtract.md) - Wytnij jeden kształt z drugiego
- [Część wspólna](intersect.md) - Zachowaj tylko objętość, w której obiekty się pokrywają
- [Cięcie płaszczyzną](../reshape/plane-cut.md) - Tnij płaską płaszczyzną zamiast innym kształtem
- [Napraw](../mesh/repair.md) - Napraw uszkodzone importowane siatki przed operacją logiczną

Ta strona obejmuje również starsze obiekty Odejmij i zastąp, które nadal występują w projektach zapisanych przed scaleniem operacji. Działają dokładnie tak samo jak wcześniej; nowe projekty używają wspólnego obiektu logicznego z wybraną operacją Odejmij i zastąp.
