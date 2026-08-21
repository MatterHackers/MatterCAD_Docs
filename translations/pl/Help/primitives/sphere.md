---
title: Kula
articleKey: SphereObject3D
parent: "Primitives"
nav_order: 14
source_hash: c227e98ac116c3481bb2af73c55801de84e70b1e
source_lang: en
---
# Kula

Okrągły kształt kuli z regulowaną średnicą i poziomem szczegółowości.

<!--  Screenshot of a Sphere primitive on the workspace -->
![20260318 183909 paste 20260318 183909](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183909-paste-20260318-183909.jpg)


## Parametry

- **Średnica** - Szerokość kuli w poprzek (domyślnie: 20mm)
- **Boki** - Liczba segmentów na obwodzie (domyślnie: 40). Więcej boków = gładsza powierzchnia

### Parametry zaawansowane

Włącz tryb **Zaawansowane**, aby uzyskać dodatkowe ustawienia:

- **Kąt początkowy** - Kąt, przy którym zaczyna się powierzchnia kuli (domyślnie: 0)
- **Kąt końcowy** - Kąt, przy którym kończy się powierzchnia kuli (domyślnie: 360). Ustaw wartość mniejszą niż 360, aby uzyskać niepełne kształty kuliste
- **Podziały szerokości** - Liczba segmentów od góry do dołu (domyślnie: 30). Więcej = gładsze bieguny

## Wskazówki

- Do druku 3D zwykle wystarcza 40 boków. Wyższe wartości dają gładsze powierzchnie, ale większe pliki
- Użyj parametrów Kąt początkowy i Kąt końcowy, aby tworzyć niepełne kształty kuliste, takie jak misy lub kopuły
- Połącz z operacją [Odejmij](../operations/boolean/subtract.md), aby tworzyć kuliste wgłębienia

## Powiązane

- [Półkula](half-sphere.md) - Tylko górna półkula
- [Torus](torus.md) - Kształt pączka
