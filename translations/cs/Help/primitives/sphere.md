---
title: Koule
articleKey: SphereObject3D
parent: "Primitives"
nav_order: 14
source_hash: c227e98ac116c3481bb2af73c55801de84e70b1e
source_lang: en
---
# Koule

Kulatý tvar koule s nastavitelným průměrem a úrovní detailu.

<!--  Screenshot of a Sphere primitive on the workspace -->
![20260318 183909 paste 20260318 183909](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183909-paste-20260318-183909.jpg)


## Parametry

- **Průměr** - Šířka koule (výchozí: 20mm)
- **Strany** - Počet segmentů po obvodu (výchozí: 40). Více stran = hladší povrch

### Rozšířené parametry

Zapněte režim **Rozšířené** pro další ovládací prvky:

- **Počáteční úhel** - Úhel, kde povrch koule začíná (výchozí: 0)
- **Koncový úhel** - Úhel, kde povrch koule končí (výchozí: 360). Nastavte méně než 360 pro částečné tvary koule
- **Strany na šířku** - Počet segmentů shora dolů (výchozí: 30). Více = hladší póly

## Tipy

- Pro 3D tisk obvykle postačuje 40 stran. Vyšší hodnoty vytvářejí hladší povrchy, ale větší soubory
- Pomocí počátečního a koncového úhlu vytvoříte částečné tvary koule, například misky nebo kopule
- Zkombinujte s operací [Odečíst](../operations/boolean/subtract.md) pro vytvoření kulových dutin

## Související

- [Polokoule](half-sphere.md) - Pouze horní polovina koule
- [Torus](torus.md) - Tvar koblihy
