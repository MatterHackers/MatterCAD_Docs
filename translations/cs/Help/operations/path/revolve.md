---
title: Rotovat
articleKey: RevolveObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: a63ebb08d982178e0e59f0b9f07c3c0dca53148b
source_lang: en
---
# Rotovat

Rotovat otáčí 2D cestu kolem osy a vytváří tak 3D rotační těleso. Takto vytvoříte vázy, misky, kola a další rotačně symetrické objekty.

<!--  Before and after showing a profile path being revolved into a vase shape -->
![20260506 102004 paste 20260506 102004](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-102004-paste-20260506-102004.jpg)


## Jak to použít

1. Vyberte 2D cestu
2. Použijte **Rotovat** z nabídky operací s cestou
3. Upravte rozsah rotace, pozici osy a počet stran

## Parametry

- **Rotace** – Celkový úhel rotace (výchozí: 0, rozsah: 0–360). Nastavte 360 pro úplné otočení.
- **Pozice osy** – Odsazení osy rotace od středu cesty (výchozí: 0, rozsah: −30 až 30). Kladný posune osu dál od cesty a vytvoří větší otvor.
- **Počáteční úhel** – Kde rotace začíná (výchozí: 0)
- **Koncový úhel** – Kde rotace končí (výchozí: 45). Nastavte 360 pro úplné otočení.
- **Strany** – Počet segmentů po obvodu rotace (výchozí: 30). Více = hladší povrch.

## Tipy

- Pomocí parametru Pozice osy řídíte vnitřní průměr rotovaného tvaru
- Nastavte Počáteční úhel a Koncový úhel na méně než 360 pro vytvoření částečných rotací (oblouky, žlaby)
- Nakreslete profilovou cestu tvaru vázy nebo misky a poté ji rotujte pro dokonalou symetrii
- Rotovaná [kruhová cesta](../../2d-paths/circle-path.md) vytvoří torus

## Související

- [Lineární extruze](linear-extrude.md) – Vytažení přímo vzhůru namísto rotace
- [2D cesty](../../2d-paths/index.md) – Vytvořte profilové cesty k rotaci
- [Torus](../../primitives/torus.md) – Hotový rotovaný prstencový tvar
