---
title: Ścieżka gwiazdy
articleKey: StarPathObject3D
parent: "2D Paths"
nav_order: 5
source_hash: 74d92e4171c452cd10069921636e45d7ef9dc70e
source_lang: en
---
# Ścieżka gwiazdy

Dwuwymiarowa ścieżka w kształcie gwiazdy z konfigurowalną liczbą punktów oraz promieniem wewnętrznym i zewnętrznym. Użyj jej razem z [Wyciągnięcie liniowe](../operations/path/linear-extrude.md), aby tworzyć trójwymiarowe kształty gwiazd.

<!-- Screenshot of a Star Path on the workspace -->
![20260506 080319 paste 20260506 080319](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080319-paste-20260506-080319.jpg)


## Parametry

- **Punkty** - Liczba punktów gwiazdy
- **Promień zewnętrzny** - Odległość od środka do wierzchołka każdego punktu
- **Promień wewnętrzny** - Odległość od środka do wcięć pomiędzy punktami

## Wskazówki

- Stosunek promienia wewnętrznego do zewnętrznego decyduje o tym, jak bardzo „szpiczasta” jest gwiazda. Mały promień wewnętrzny daje ostre, wyraźnie zarysowane punkty.
- Ustaw **Punkty** na 5, aby uzyskać klasyczną gwiazdę, na 6, aby otrzymać gwiazdę Dawida, lub na większą wartość, aby uzyskać kształty przypominające koło zębate
- Użyj operacji [Wygładź ścieżkę](../operations/path/smooth-path.md) na ścieżce gwiazdy, aby uzyskać zaokrąglone kształty gwiazd

## Powiązane

- [Ścieżka okręgu](circle-path.md) - Gładki okrąg
- [Koło zębate 2D](../mechanical/gear-2d.md) - Właściwy profil koła zębatego
- [Wyciągnięcie liniowe](../operations/path/linear-extrude.md) - Nadaje ścieżkom wysokość
