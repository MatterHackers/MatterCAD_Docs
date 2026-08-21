---
title: Obróć
articleKey: RotateObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 9bdc210c5c375fe3179050e8a8916d895455ce5f
source_lang: en
---
# Obróć

Obróć obraca obiekt wokół określonej osi o zadany kąt. Możesz obracać wokół dowolnego kierunku osi i wybrać punkt środkowy obrotu.

<!--  Screenshot showing the Rotate operation with the rotation gizmo visible in the viewport -->
![20260506 160726 paste 20260506 160726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160726-paste-20260506-160726.jpg)

## Jak używać

1. Wybierz obiekt
2. Zastosuj operację **Obróć** z menu Przekształć
3. Ustaw kąt i oś obrotu w panelu Właściwości

Możesz również obracać obiekty bezpośrednio w widoku, klikając narożne uchwyty obrotu na zaznaczonym obiekcie. Przesuwanie myszy nad wskaźnikami kąta powoduje przyciąganie do przyrostów co 45 stopni.

## Parametry

- **Kąt** – Kąt obrotu w stopniach (zakres: 3–360). Obsługuje [wyrażenia](../../workspace/expressions.md).
- **Obróć wokół** – Określa oś obrotu oraz punkt początkowy. Możesz obracać wokół osi X, Y lub Z albo podać własny kierunek.

## Wskazówki

- Domyślnie obrót odbywa się względem środka prostopadłościanu otaczającego obiekt
- Przy obrotach o 90 stopni wskaźniki przyciągania ułatwiają uzyskanie dokładnych wartości
- Użyj operacji Obróć (zamiast uchwytów w widoku), gdy potrzebujesz precyzyjnego kąta niebędącego wielokrotnością 45 stopni
- Oś obrotu możesz zmienić po zastosowaniu operacji, edytując właściwość Obróć wokół

## Powiązane

- [Przesuń](translate.md) – Przesuwa obiekt o określoną odległość
- [Skaluj](scale.md) – Zmienia rozmiar obiektu
- [Odbicie lustrzane](mirror.md) – Tworzy lustrzane odbicie
