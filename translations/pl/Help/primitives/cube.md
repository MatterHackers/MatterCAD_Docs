---
title: Sześcian
articleKey: CubeObject3D
parent: "Primitives"
nav_order: 4
source_hash: a376a9c78d88d995f3c6ce21dd5098672d6c1dfb
source_lang: en
---
# Sześcian

Prostopadłościenny kształt z regulowaną szerokością, głębokością, wysokością oraz opcjonalnie zaokrąglonymi krawędziami. Sześcian to jedna z najczęściej używanych brył podstawowych do budowania projektów.

<!--  Screenshot of a Cube primitive on the workspace -->
![20260318 183230 paste 20260318 183230](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183230-paste-20260318-183230.jpg)


## Parametry

- **Szerokość** - Rozmiar wzdłuż osi X (domyślnie: 20mm)
- **Głębokość** - Rozmiar wzdłuż osi Y (domyślnie: 20mm)
- **Wysokość** - Rozmiar wzdłuż osi Z (domyślnie: 20mm)
- **Zaokrąglenie** - Włącza zaokrąglone krawędzie
- **Promień** - Wielkość zaokrąglenia (widoczny, gdy włączone jest Zaokrąglenie)
- **Segmenty zaokrąglenia** - Gładkość zaokrąglenia, więcej segmentów = gładsze krzywizny (widoczne, gdy włączone jest Zaokrąglenie)

## Wskazówki

- Użyj Sześcianu jako punktu wyjścia dla pudełek, płyt, wsporników i obudów
- Włącz Zaokrąglenie, aby uzyskać gładkie, profesjonalnie wyglądające krawędzie
- Promień nie może przekraczać połowy najmniejszego wymiaru
- Połącz Sześcian z operacją [Odejmij](../operations/boolean/subtract.md), aby tworzyć prostokątne wycięcia i szczeliny

## Powiązane

- [Walec](cylinder.md) - Okrągły kształt kolumny
- [Ostrosłup](pyramid.md) - Zwężający się kształt czworoboczny
- [Otwór](hole.md) - Sześcian wstępnie skonfigurowany do odejmowania logicznego
