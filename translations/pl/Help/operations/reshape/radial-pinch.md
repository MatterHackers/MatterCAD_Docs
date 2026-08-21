---
title: Ściśnięcie promieniowe
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: 95ef5847767e5cfcdbae9df9aaa1cb1727da2f5e
source_lang: en
---
# Ściśnięcie promieniowe

Ściśnięcie promieniowe kompresuje obiekt do wewnątrz względem punktu środkowego przy użyciu konfigurowalnej krzywej profilu. W przeciwieństwie do zwykłego [Zwężenie](pinch.md), które działa od tyłu do przodu, Ściśnięcie promieniowe kompresuje obiekt symetrycznie wokół osi środkowej.

<!--  Before and after showing an object with radial pinch applied, creating a waisted shape -->
![20260506 155741 paste 20260506 155741](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155741-paste-20260506-155741.jpg)

## Sposób użycia

1. Wybierz obiekt
2. Zastosuj operację **Ściśnięcie promieniowe** z menu Przekształć
3. Edytuj profil ścieżki, aby określić, jak duże ściśnięcie jest stosowane na każdej wysokości
4. Dostosuj liczbę przekrojów, aby uzyskać większą gładkość

## Parametry

- **Ścieżka** – Edytor krzywej profilu, który określa wielkość zwężenia na każdym poziomie wysokości. Edytuj krzywą, aby tworzyć własne profile zwężenia
- **Przekroje** – Liczba poziomych cięć zapewniających płynne zwężanie, rozmieszczonych równomiernie na całej wysokości części. Więcej przekrojów = gładszy wynik

### Parametry zaawansowane

- **Typ zwężenia** – Kierunek kompresji:
  - **Promieniowy** – Kompresja równomiernie ze wszystkich stron w kierunku środka
  - **Oś X** – Kompresja tylko wzdłuż osi X
  - **Oś Y** – Kompresja tylko wzdłuż osi Y
- **Przesunięcie obrotu** – Przesuwa środek efektu zwężenia

## Wskazówki

- Użyj edytora ścieżki, aby tworzyć kształty przypominające klepsydrę, butelkę lub wazon
- Ściśnięcie promieniowe doskonale nadaje się do tworzenia organicznych, zaokrąglonych form z obiektów walcowych
- Zwiększ wartość Przekroje, aby uzyskać gładsze krzywe, zwłaszcza przy ostrych profilach zwężenia

## Powiązane

- [Zwężenie](pinch.md) – Prosta kompresja od tyłu do przodu
- [Skręcenie](twist.md) – Spiralny obrót wzdłuż wysokości
- [Krzywa](curve.md) – Wygięcie w łuk
