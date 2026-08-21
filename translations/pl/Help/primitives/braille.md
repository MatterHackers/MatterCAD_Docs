---
title: Brajl
articleKey: BrailleObject3D
parent: "Primitives"
nav_order: 2
source_hash: d1d9d4aeb9b87efbe32045f2a96cfea49048f95f
source_lang: en
---
# Brajl

Generuj tekst brajlowski do druku 3D ze standardowego tekstu angielskiego. Narzędzie Brajl obsługuje kodowanie brajlowskie zarówno w stopniu 1 (litera po literze), jak i w stopniu 2 (skrótowe).

<!-- Screenshot of a Braille object showing raised dots on the workspace -->
![20260318 182800 paste 20260318 182800](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-182800-paste-20260318-182800.jpg)


## Sposób użycia

1. Dodaj prymityw **Brajl** z panelu Prymitywy
2. Wpisz swój tekst w polu **Tekst do zakodowania**
3. Narzędzie automatycznie przekształci go w prawidłowy układ punktów brajlowskich

## Parametry

- **Tekst do zakodowania** – tekst angielski do konwersji na brajla
- **Skaluj** – dostosowuje ogólny rozmiar wyniku brajlowskiego
- **Wysokość** – wysokość wypukłych punktów brajlowskich

## Wskazówki

- Brajl w stopniu 2 wykorzystuje skróty i skrótowce dla często występujących słów i połączeń liter, dzięki czemu jest bardziej zwarty
- Stosowane są standardowe wymiary komórki brajlowskiej, aby zapewnić czytelność wyniku
- Połącz z płaską podstawą [Sześcian](cube.md), aby utworzyć kompletną etykietę lub tabliczkę brajlowską
- Informacje o kartach brajlowskich ze zintegrowaną podstawą znajdziesz w [Karta brajlowska](braille-card.md)

## Powiązane

- [Karta brajlowska](braille-card.md) – brajl ze zintegrowaną podstawą karty
- [Tekst](text.md) – standardowy tekst 3D
