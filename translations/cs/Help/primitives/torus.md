---
title: Torus
articleKey: TorusObject3D
parent: "Primitives"
nav_order: 17
source_hash: aaec1652de4d6713bd01a707964cf4985d3fb5f6
source_lang: en
---
# Torus

Prstenec ve tvaru koblihy s nezávislým ovládáním celkové velikosti a tloušťky průřezu prstence.

<!--  Screenshot of a Torus primitive on the workspace -->
![20260318 184240 paste 20260318 184240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184240-paste-20260318-184240.jpg)


## Parametry

- **Vnější průměr** - Celková šířka přes torus (výchozí: 20mm)
- **Vnitřní průměr** - Průměr otvoru uprostřed (výchozí: 10mm)
- **Strany** - Počet segmentů kolem hlavního prstence (výchozí: 40)

### Rozšířené parametry

Zapněte režim **Rozšířené** pro další ovládací prvky:

- **Počáteční úhel** - Úhel, ve kterém torus začíná (výchozí: 0)
- **Koncový úhel** - Úhel, ve kterém torus končí (výchozí: 360). Nastavte méně než 360 pro otevřený prstenec nebo oblouk
- **Strany prstence** - Počet segmentů kolem průřezu prstence (výchozí: 15). Více = hladší profil trubky
- **Fázový úhel prstence** - Otáčí profilem průřezu (výchozí: 0)

## Tipy

- Tloušťka trubky prstence je dána rozdílem mezi vnějším a vnitřním průměrem
- Pomocí počátečního a koncového úhlu vytvoříte otevřené segmenty prstence, oblouky nebo tvary písmene C
- Užitečné pro tvorbu O-kroužků, držadel, dekorativních prstenců a ohybů potrubí

## Související

- [Prstenec](ring.md) - Dutý válec s rovnými stěnami (trubka)
- [Koule](sphere.md) - Plný kulový tvar
- [Polokoule](half-sphere.md) - Tvar kopule
