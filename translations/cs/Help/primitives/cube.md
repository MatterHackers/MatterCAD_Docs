---
title: Kvádr
articleKey: CubeObject3D
parent: "Primitives"
nav_order: 4
source_hash: a376a9c78d88d995f3c6ce21dd5098672d6c1dfb
source_lang: en
---
# Kvádr

Kvádrový tvar s nastavitelnou šířkou, hloubkou, výškou a volitelně zaoblenými hranami. Kvádr patří mezi nejpoužívanější primitiva pro tvorbu návrhů.

<!--  Screenshot of a Cube primitive on the workspace -->
![20260318 183230 paste 20260318 183230](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183230-paste-20260318-183230.jpg)


## Parametry

- **Šířka** - Velikost podél osy X (výchozí: 20mm)
- **Hloubka** - Velikost podél osy Y (výchozí: 20mm)
- **Výška** - Velikost podél osy Z (výchozí: 20mm)
- **Zaoblení** - Zapne zaoblené hrany
- **Poloměr** - Velikost zaoblení (zobrazí se, když je zapnuté Zaoblení)
- **Segmenty zaoblení** - Hladkost zaoblení, více segmentů = hladší křivky (zobrazí se, když je zapnuté Zaoblení)

## Tipy

- Kvádr použijte jako výchozí bod pro krabičky, desky, držáky a kryty
- Zapněte Zaoblení pro hladké, profesionálně vypadající hrany
- Poloměr nesmí přesáhnout polovinu nejmenšího rozměru
- Kombinací kvádru s operací [Odečíst](../operations/boolean/subtract.md) vytvoříte obdélníkové výřezy a drážky

## Související

- [Válec](cylinder.md) - Kulatý sloupcový tvar
- [Jehlan](pyramid.md) - Zúžený čtyřboký tvar
- [Otvor](hole.md) - Kvádr přednastavený pro booleovské odečítání
