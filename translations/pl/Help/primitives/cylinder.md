---
title: Walec
articleKey: CylinderObject3D
parent: "Primitives"
nav_order: 5
source_hash: ab8394a14de799f83dc9c39eb86b8eaf2aab37b7
source_lang: en
---
# Walec

Kształt okrągłej kolumny z konfigurowalną średnicą, wysokością i liczbą boków. Walec jest niezbędny do tworzenia sworzni, prętów, otworów i okrągłych detali.

<!--  Screenshot of a Cylinder primitive on the workspace -->
![20260318 183248 paste 20260318 183248](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183248-paste-20260318-183248.jpg)


## Parametry

- **Średnica** - Szerokość walca w poprzek (domyślnie: 20mm)
- **Wysokość** - Wysokość walca (domyślnie: 20mm)
- **Boki** - Liczba segmentów na obwodzie (domyślnie: 40). Niższe wartości tworzą kształty wielokątne (np. 6 dla sześciokąta)

### Parametry zaawansowane

Włącz tryb **Zaawansowane**, aby uzyskać dostęp do dodatkowych ustawień:

- **Średnica górna** - Ustaw inną średnicę górnej części walca, aby utworzyć kształty zbieżne lub ścięte stożki (domyślnie: zgodna ze **Średnicą**)
- **Kąt początkowy** - Kąt, od którego zaczyna się walec (domyślnie: 0). Używaj razem z **Kątem końcowym**, aby tworzyć niepełne walce
- **Kąt końcowy** - Kąt, na którym kończy się walec (domyślnie: 360). Ustaw wartość mniejszą niż 360, aby uzyskać kształty w formie wycinka koła

## Wskazówki

- Ustaw **Boki** na niską wartość, aby tworzyć wielokąty foremne -- 6 dla sześciokątów, 8 dla ośmiokątów itd.
- Użyj różnych wartości **Średnicy** i **Średnicy górnej**, aby tworzyć ścięte stożki i kształty zbieżne
- Ustaw **Kąt początkowy** i **Kąt końcowy**, aby tworzyć kształty w formie wycinka koła lub łuku
- Walce doskonale sprawdzają się jako narzędzia tnące do tworzenia okrągłych otworów za pomocą operacji [Odejmij](../operations/boolean/subtract.md)

## Powiązane

- [Stożek](cone.md) - Walec zbiegający się do punktu
- [Półwalec](half-cylinder.md) - Walec przecięty wzdłuż na pół
- [Pierścień](ring.md) - Pusty w środku walec (rura)
