---
title: Vydutit
articleKey: HollowOutObject3D
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 3
source_hash: cc2c5555723ecfe77475fef9e7a2090cdf760204
source_lang: en
---
# Vydutit

Vydutit vytvoří z plného tělesa dutou skořepinu odsazením povrchu směrem dovnitř. Výsledkem je tenkostěnná verze původního tvaru.

<!--  Cross-section view showing a solid object hollowed out with visible wall thickness -->
![20260506 155412 paste 20260506 155412](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155412-paste-20260506-155412.jpg)

## Jak postupovat

1. Vyberte plné těleso
2. Použijte operaci **Vydutit** z nabídky Přetvarovat
3. Nastavte požadovanou tloušťku stěny

## Parametry

- **Vzdálenost** – Tloušťka stěny v milimetrech (výchozí: 2 mm). Určuje, jak silná bude výsledná skořepina.
- **Počet buněk** – Rozlišení algoritmu vydutí (výchozí: 64). Vyšší hodnoty vytvářejí hladší vnitřní povrchy, ale výpočet trvá déle.

## Tipy

- Vydutit se hodí pro tvorbu krytů, nádob, váz a lehkých dílů
- Tloušťka stěny 1–2 mm je typická pro většinu 3D tištěných dílů
- Pokud vnitřní povrch vypadá hrubě nebo hranatě, zvyšte Počet buněk
- Vydutí vytvoří otevřené dno – pokud potřebujete uzavřenou základnu, zkombinujte jej s operací [Kvádr](../../primitives/cube.md)
- U složitých tvarů může výpočet trvat několik sekund

## Související

- [Řez rovinou](plane-cut.md) – Rozřízne objekt v určité výšce
- [Odečíst](../boolean/subtract.md) – Ruční odebrání materiálu
