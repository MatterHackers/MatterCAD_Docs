---
title: Obraz na ścieżkę
articleKey: ImageToPathObject3D_2
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 0145587f635ede68bfc1df37b4f0d366a03d3a6c
source_lang: en
---
# Obraz na ścieżkę

Obraz na ścieżkę obrysowuje kontury obrazu, tworząc ścieżki 2D. Takie ścieżki można następnie wyciągnąć, obrócić lub wykorzystać w dowolnej innej operacji na ścieżkach. To idealne rozwiązanie do zamiany logo, sylwetek i prostych grafik w obiekty 3D.

![20260324 075521 paste 20260324 075521](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-075521-paste-20260324-075521.jpg)


## Sposób użycia

1. Wybierz obiekt obrazu w obszarze roboczym
2. Zastosuj operację **Obraz na ścieżkę** z menu operacji Obraz
3. Wybierz typ analizy i dostosuj zakres wyboru

## Parametry

- **Typ analizy** - Sposób analizowania obrazu na potrzeby obrysu:
  - **Przezroczystość** - Obrys na podstawie obszarów przezroczystych i nieprzezroczystych (najlepsze dla plików PNG z przezroczystym tłem)
  - **Kolory** - Obrys na podstawie obszarów kolorów
  - **Intensywność** - Obrys na podstawie poziomów jasności (najlepsze dla większości obrazów)
- **Wybierz zakres** - Element sterujący w postaci histogramu, służący do wyboru wartości jasności/koloru uwzględnianych w obrysie
- **Min. pole powierzchni** - Minimalne pole pętli ścieżki, aby została uwzględniona. Zwiększ, aby odfiltrować drobne artefakty szumu

## Wskazówki

- Najlepiej sprawdzają się czyste obrazy o wysokim kontraście i prostych kształtach
- Używaj trybu Przezroczystość dla obrazów PNG z przezroczystym tłem
- Używaj trybu Intensywność dla fotografii i obrazów bez przezroczystości
- Po wykonaniu obrysu zastosuj [Wyciągnięcie liniowe](../path/linear-extrude.md), aby nadać ścieżce wysokość
- Zwiększ wartość Min. pole powierzchni, aby usunąć z obrysu małe, niepożądane detale

## Powiązane

- [Konwerter obrazów](image-converter.md) - Tworzy relief na podstawie mapy wysokości zamiast płaskich ścieżek
- [Litofan](lithophane.md) - Tworzy podświetlane obrazy
- [Obiekt SVG](../../primitives/svg-object.md) - Importuj grafikę wektorową bezpośrednio (bez potrzeby obrysu)
- [Wyciągnięcie liniowe](../path/linear-extrude.md) - Nadaje obrysowanej ścieżce wysokość
