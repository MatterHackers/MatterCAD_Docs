---
title: Lineární extruze
articleKey: LinearExtrudeObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cdfdb9cfe4c3339e70a23ddfb2f5071b1e8c5557
source_lang: en
---
# Lineární extruze

Lineární extruze dodá 2D cestě výšku a promění plochý tvar v 3D těleso. Toto je základní způsob, jak převést cesty na 3D objekty.

<!--  Before and after showing a 2D star path extruded into a 3D star -->
![20260506 100726 paste 20260506 100726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-100726-paste-20260506-100726.jpg)


## Jak ji použít

1. Vyberte 2D cestu nebo objekt založený na cestě
2. Použijte **Lineární extruze** z nabídky operací s cestami
3. Nastavte požadovanou výšku

## Parametry

- **Výška** – Jak vysoká extruze je (výchozí: 5 mm, rozsah: 0,1–50 mm)
- **Zkosení nahoře** – Přidá zkosenou (zaoblenou) hranu na horní části extruze (výchozí: vypnuto)

### Parametry zkosení (viditelné, když je zapnuto Zkosení nahoře)

- **Styl** – Profil zkosení (Ostrý nebo zaoblený)
- **Poloměr** – Jak široko zkosení zasahuje (výchozí: 3 mm)
- **Segmenty** – Hladkost křivky zkosení (výchozí: 9)

## Tipy

- Funguje s libovolnou 2D cestou: [Kruh](../../2d-paths/circle-path.md), [Kvádr](../../2d-paths/box-path.md), [Hvězda](../../2d-paths/star-path.md), [SVG](../../primitives/svg-object.md) a [Vlastní](../../2d-paths/custom-path.md) cesty
- Zapněte Zkosení nahoře pro uhlazenější, profesionálnější vzhled
- Pokud chcete cestu rotovat kolem osy místo vytažení přímo vzhůru, viz [Rotovat](revolve.md)

## Související

- [Rotovat](revolve.md) – Otočí cestu kolem osy
- [2D cesty](../../2d-paths/index.md) – Dostupné tvary cest
- [Text](../../primitives/text.md) – Text je vytažen automaticky
