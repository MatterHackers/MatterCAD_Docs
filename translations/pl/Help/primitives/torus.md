---
title: Torus
articleKey: TorusObject3D
parent: "Primitives"
nav_order: 17
source_hash: aaec1652de4d6713bd01a707964cf4985d3fb5f6
source_lang: en
---
# Torus

Pierścień w kształcie pączka z niezależną kontrolą nad ogólnym rozmiarem oraz grubością przekroju pierścienia.

<!--  Screenshot of a Torus primitive on the workspace -->
![20260318 184240 paste 20260318 184240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184240-paste-20260318-184240.jpg)


## Parametry

- **Średnica zewnętrzna** - Całkowita szerokość torusa (domyślnie: 20mm)
- **Średnica wewnętrzna** - Średnica otworu na środku (domyślnie: 10mm)
- **Boki** - Liczba segmentów wokół głównego pierścienia (domyślnie: 40)

### Parametry zaawansowane

Włącz tryb **Zaawansowane**, aby uzyskać dodatkowe ustawienia:

- **Kąt początkowy** - Kąt, przy którym zaczyna się torus (domyślnie: 0)
- **Kąt końcowy** - Kąt, przy którym kończy się torus (domyślnie: 360). Ustaw wartość mniejszą niż 360, aby uzyskać otwarty pierścień lub łuk
- **Boki pierścienia** - Liczba segmentów wokół przekroju pierścienia (domyślnie: 15). Więcej = gładszy profil rury
- **Kąt fazy pierścienia** - Obraca profil przekroju (domyślnie: 0)

## Wskazówki

- Grubość rury pierścienia zależy od różnicy między Średnicą zewnętrzną a Średnicą wewnętrzną
- Użyj Kąta początkowego i Kąta końcowego, aby tworzyć otwarte segmenty pierścienia, łuki lub kształty w formie litery C
- Przydatne do tworzenia oringów, uchwytów, pierścieni dekoracyjnych i kolan rur

## Powiązane

- [Pierścień](ring.md) - Wydrążony walec o prostych ściankach (rura)
- [Kula](sphere.md) - Pełna kula
- [Półkula](half-sphere.md) - Kształt kopuły
