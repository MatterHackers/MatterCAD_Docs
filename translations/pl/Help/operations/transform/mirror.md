---
title: Odbicie lustrzane
articleKey: MirrorObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 8a8de28f5e429177d4b0092d0756387eb6b83a70
source_lang: en
---
# Odbicie lustrzane

Odbicie lustrzane tworzy odbitą kopię obiektu względem jednej z trzech głównych osi. Wynikiem jest lustrzana wersja pierwotnego kształtu.

<!--  Before and after showing an object mirrored across the X axis -->
![20260506 160651 paste 20260506 160651](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160651-paste-20260506-160651.jpg)


## Sposób użycia

1. Wybierz obiekt
2. Zastosuj operację **Odbicie lustrzane** z menu Przekształć
3. Wybierz oś, względem której ma nastąpić odbicie

## Parametry

- **Odbicie lustrzane wł.** - Oś, względem której następuje odbicie:
  - **Oś X** - Odwraca obiekt z lewej na prawą stronę
  - **Oś Y** - Odwraca obiekt z przodu do tyłu
  - **Oś Z** - Odwraca obiekt z góry na dół

## Wskazówki

- Odbicie lustrzane jest wyśrodkowane względem obwiedni obiektu, więc odbity wynik zajmuje tę samą przestrzeń co oryginał
- Normalne ścian są automatycznie korygowane po odbiciu, aby zachować prawidłowe renderowanie
- Użyj operacji Odbicie lustrzane do tworzenia symetrycznych projektów -- wymodeluj jedną połowę, następnie odbij ją lustrzanie i użyj [Połącz](../boolean/combine.md) z oryginałem
- Odbicie lustrzane jest nieniszczące: oś odbicia możesz zmienić w dowolnym momencie

## Powiązane

- [Obróć](rotate.md) - Obróć obiekt zamiast go odbijać
- [Skaluj](scale.md) - Zmień rozmiar obiektu
- [Połącz](../boolean/combine.md) - Scal oryginał i odbitą kopię w jeden obiekt
