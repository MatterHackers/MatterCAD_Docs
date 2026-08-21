---
title: Tworzenie nowych obiektów
parent: "Getting Started"
nav_order: 2
source_hash: 3eccb5aac5bb6f4d88f1ca3583eedd2f70384eeb
source_lang: en
---
# Tworzenie nowych obiektów

MatterCAD udostępnia bogaty zestaw narzędzi do tworzenia obiektów 3D. Możesz zacząć od kształtów prymitywnych, skorzystać ze specjalistycznych narzędzi, takich jak tekst i kody QR, albo budować złożone formy przy użyciu operacji logicznych i szyków.

![20260324 081122 paste 20260324 081122](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081122-paste-20260324-081122.jpg)

## Dodawanie prymitywów

Najszybszym sposobem rozpoczęcia projektu jest dodanie kształtów prymitywnych. Otwórz panel Prymitywy w bibliotece i kliknij dowolny kształt, aby dodać go do obszaru roboczego. Dostępne prymitywy to:

- **Kształty podstawowe** – Sześcian, Walec, Kula, Stożek, Torus, Pierścień, Ostrosłup, Klin oraz ich warianty połówkowe
- **Tekst i elementy specjalne** – Tekst, Brajl, Kod QR, Obiekt Obraz, Obiekt SVG

Każdy prymityw ma parametry, które możesz dostosować w panelu Właściwości po jego zaznaczeniu. Na przykład Sześcian ma ustawienia Szerokość, Głębokość i Wysokość. Szczegółowe informacje o poszczególnych kształtach znajdziesz w artykule [Prymitywy](../primitives/index.md).

## Pasek narzędzi operacji

![20260324 081005 paste 20260324 081005](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081005-paste-20260324-081005.jpg)

Pasek narzędzi u góry okna widoku zapewnia szybki dostęp do najczęściej używanych operacji:

- **Cofnij / Ponów** – cofa lub przywraca zmiany. Możesz również użyć skrótów **Ctrl+Z**, aby cofnąć, oraz **Ctrl+Y**, aby ponowić
- **Grupuj / Rozgrupuj** – łączy zaznaczone obiekty w grupę, która przemieszcza się i działa jako jedna całość, albo rozdziela grupę
- **Kopiuj / Usuń** – duplikuje lub usuwa zaznaczone obiekty. Działają również standardowe skróty **Ctrl+C**, **Ctrl+X** i **Ctrl+V**
- **Wyrównaj** – ustawia wiele obiektów względem siebie
- **Operacje logiczne** – [Połącz](../operations/boolean/combine.md), [Odejmij](../operations/boolean/subtract.md), [Część wspólna](../operations/boolean/intersect.md) oraz [Odejmij i zastąp](../operations/boolean/subtract-and-replace.md)
- **Szyk** – tworzy [wzory liniowe, promieniste, po krzywej i przekształcenia](../operations/array/array.md) zduplikowanych obiektów
- **Przekształć** – stosuje operacje [Obróć](../operations/transform/rotate.md), [Skaluj](../operations/transform/scale.md), [Odbicie lustrzane](../operations/transform/mirror.md) i inne modyfikacje

## Budowanie złożonych kształtów

Większość projektów w MatterCAD powstaje przez łączenie prostych kształtów:

1. **Zacznij od prymitywów** – dodaj potrzebne kształty podstawowe
2. **Ustaw je** – przesuwaj i obracaj obiekty tak, aby nachodziły na siebie w wybranych miejscach
3. **Zastosuj operacje logiczne** – użyj operacji [Połącz](../operations/boolean/combine.md), aby scalić kształty, lub [Odejmij](../operations/boolean/subtract.md), aby wyciąć jeden kształt z drugiego
4. **Dopracuj** – użyj operacji [Przekształć](../operations/reshape/index.md), takich jak Faza, Krzywa lub Skręcenie, aby dodać szczegóły

## Powiązane

- [Prymitywy](../primitives/index.md) – pełne omówienie wszystkich kształtów prymitywnych
- [Dodawanie istniejących obiektów](adding-existing-objects.md) – importuj pliki zamiast tworzyć obiekty od podstaw
- [Operacje logiczne](../operations/boolean/index.md) – łączenie kształtów w złożone formy
- [Edytowanie obiektów](editing-objects.md) – przesuwanie, obracanie i skalowanie obiektów po ich utworzeniu
