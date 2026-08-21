---
title: Wyciągnięcie liniowe
articleKey: LinearExtrudeObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cdfdb9cfe4c3339e70a23ddfb2f5071b1e8c5557
source_lang: en
---
# Wyciągnięcie liniowe

Wyciągnięcie liniowe nadaje ścieżce 2D wysokość, zamieniając płaski kształt w bryłę 3D. To podstawowy sposób przekształcania ścieżek w obiekty 3D.

<!--  Before and after showing a 2D star path extruded into a 3D star -->
![20260506 100726 paste 20260506 100726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100726-paste-20260506-100726.jpg)


## Sposób użycia

1. Wybierz ścieżkę 2D lub obiekt oparty na ścieżce
2. Zastosuj **Wyciągnięcie liniowe** z menu operacji Ścieżka
3. Ustaw żądaną wysokość

## Parametry

- **Wysokość** - Wysokość wyciągnięcia (domyślnie: 5mm, zakres: 0,1-50mm)
- **Faza górna** - Dodaje sfazowaną (zaokrągloną) krawędź na górze wyciągnięcia (domyślnie: wyłączone)

### Parametry fazy (widoczne, gdy włączona jest Faza górna)

- **Styl** - Profil fazy (Ostry lub zaokrąglony)
- **Promień** - Szerokość fazy (domyślnie: 3mm)
- **Segmenty** - Gładkość krzywej fazy (domyślnie: 9)

## Wskazówki

- Działa z każdą ścieżką 2D: [Okrąg](../../2d-paths/circle-path.md), [Prostopadłościan](../../2d-paths/box-path.md), [Gwiazda](../../2d-paths/star-path.md), [SVG](../../primitives/svg-object.md) oraz ścieżki [Niestandardowy](../../2d-paths/custom-path.md)
- Włącz Fazę górną, aby uzyskać bardziej dopracowany, profesjonalny wygląd
- Aby obrócić ścieżkę wokół osi zamiast wyciągać ją prosto w górę, zobacz [Obrót (Revolve)](revolve.md)

## Powiązane

- [Obrót (Revolve)](revolve.md) - Obraca ścieżkę wokół osi
- [Ścieżki 2D](../../2d-paths/index.md) - Dostępne kształty ścieżek
- [Tekst](../../primitives/text.md) - Tekst jest wyciągany automatycznie
