---
title: Krzywa
articleKey: CurveObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 6adde5da3bb469384f59eb5e9dfe5cb642b3eec5
source_lang: en
---
# Krzywa

Krzywa zagina prosty obiekt w łuk lub kształt kołowy. Zgięciem można sterować, określając kąt albo średnicę, wokół której obiekt ma zostać owinięty.

<!--  Before and after showing a straight bar being curved into an arc -->
![20260506 155243 paste 20260506 155243](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155243-paste-20260506-155243.jpg)

## Sposób użycia

1. Wybierz obiekt
2. Zastosuj operację **Krzywa** z menu Przekształć
3. Wybierz typ zgięcia: Kąt lub Średnica
4. Dostosuj parametry, aby uzyskać żądaną krzywiznę

## Parametry

- **Typ zgięcia** – do wyboru:
  - **Kąt** – bezpośrednio określ kąt zgięcia (1–360 stopni)
  - **Średnica** – określ średnicę okręgu, wokół którego owija się element
- **Kierunek zginania** – Zegnij w górę lub Zegnij w dół
- **Procent początkowy** – miejsce na długości obiektu, w którym rozpoczyna się zgięcie (0–100%)
- **Podziel siatkę** – dzieli siatkę, aby uzyskać gładkie krzywe (domyślnie: włączone)
- **Min. liczba boków na obrót** – minimalna liczba segmentów siatki na pełny obrót. Wyższe wartości = gładsze krzywe

### Parametry zaawansowane

- **Procent początku zgięcia** – wartość procentowa od lewej strony, w której zaczyna się zgięcie
- **Procent zagięcia końcowego** – wartość procentowa od lewej strony, w której kończy się zgięcie

## Wskazówki

- Użyj operacji Krzywa, aby tworzyć łuki, pierścienie i wygięte wsporniki z prostych kształtów wyjściowych
- Ustawienie kąta na 360 zawija obiekt w pełny pierścień
- Zwiększ wartość Min. liczba boków na obrót, aby uzyskać gładsze wyniki przy ciasnych zgięciach
- Obiekt jest zginany wzdłuż swojej długości (oś X)

## Powiązane

- [Skręcenie](twist.md) – obrót wzdłuż wysokości zamiast zginania
- [Torus](../../primitives/torus.md) – gotowy kształt pierścienia
