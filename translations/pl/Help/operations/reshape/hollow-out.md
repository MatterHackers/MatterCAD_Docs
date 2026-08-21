---
title: Wydrąż
articleKey: HollowOutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cc2c5555723ecfe77475fef9e7a2090cdf760204
source_lang: en
---
# Wydrąż

Wydrąż tworzy pustą w środku skorupę z obiektu bryłowego, odsuwając powierzchnię do wewnątrz. Wynikiem jest cienkościenna wersja pierwotnego kształtu.

<!--  Cross-section view showing a solid object hollowed out with visible wall thickness -->
![20260506 155412 paste 20260506 155412](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155412-paste-20260506-155412.jpg)

## Sposób użycia

1. Wybierz obiekt bryłowy
2. Zastosuj operację **Wydrąż** z menu Przekształć
3. Ustaw żądaną grubość ścianki

## Parametry

- **Odległość** — grubość ścianki w milimetrach (domyślnie: 2 mm). Określa, jak gruba będzie powstała skorupa.
- **Liczba komórek** — rozdzielczość algorytmu drążenia (domyślnie: 64). Wyższe wartości dają gładsze powierzchnie wewnętrzne, ale wydłużają czas obliczeń.

## Wskazówki

- Wydrąż przydaje się do tworzenia obudów, pojemników, wazonów i lekkich części
- Grubość ścianki 1–2 mm jest typowa dla większości części drukowanych w 3D
- Zwiększ wartość Liczba komórek, jeśli powierzchnia wewnętrzna wygląda na chropowatą lub kanciastą
- Drążenie tworzy otwarty spód — połącz je z operacją [Sześcian](../../primitives/cube.md), jeśli potrzebujesz zamkniętej podstawy
- W przypadku złożonych kształtów obliczenia mogą potrwać kilka sekund

## Powiązane

- [Cięcie płaszczyzną](plane-cut.md) — przecina obiekt na określonej wysokości
- [Odejmij](../boolean/subtract.md) — ręcznie usuwa materiał
