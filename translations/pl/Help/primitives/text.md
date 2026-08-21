---
title: Tekst
articleKey: TextObject3D_2
parent: "Primitives"
nav_order: 16
source_hash: 526f3190c7b2150243499b5874ac455d74810bb2
source_lang: en
---
# Tekst

Utwórz wytłaczany tekst 3D z konfigurowalną treścią, czcionką, rozmiarem i wysokością. Obiekty typu Tekst świetnie sprawdzają się jako etykiety, oznaczenia, tabliczki znamionowe i napisy dekoracyjne.

<!--  Screenshot of a 3D Text object on the workspace showing extruded letters -->
![20260318 184207 paste 20260318 184207](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184207-paste-20260318-184207.jpg)


## Sposób użycia

1. Dodaj prymityw **Tekst** z panelu Prymitywy
2. Wpisz swój tekst w polu **Nazwa** w panelu Właściwości
3. Dostosuj czcionkę, rozmiar i wysokość wytłoczenia według potrzeb

## Parametry

- **Nazwa** - Treść tekstu do wyświetlenia
- **Rozmiar punktu** - Rozmiar czcionki. Jest on zgodny ze standardowym rozmiarem druku -- rozmiar 12 punktów w MatterCAD odpowiada 12-punktowej czcionce na drukarce 2D
- **Wysokość** - Wysokość wytłoczenia (jak bardzo tekst wystaje ponad powierzchnię)
- **Czcionka** - Wybierz spośród dostępnych czcionek systemowych

## Wskazówki

- Użyj operacji [Odejmij](../operations/boolean/subtract.md), aby wygrawerować tekst w powierzchni zamiast go uwypuklać
- W przypadku bardzo małego tekstu zwiększ Rozmiar punktu, a następnie [Skaluj](../operations/transform/scale.md) cały obiekt w dół, aby uzyskać lepsze odwzorowanie szczegółów
- Każda litera w tekście jest oddzielną ścieżką, która jest wytłaczana razem z pozostałymi

## Powiązane

- [Brajl](braille.md) - Generuj tekst brajlowski do druku 3D
- [Kod QR](qr-code.md) - Generuj kod QR jako obiekt 3D
- [Obraz Obiekt](image-object.md) - Konwertuj obrazy na 3D
