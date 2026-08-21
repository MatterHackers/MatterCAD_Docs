---
title: Křivka
articleKey: CurveObject3D_3
parent: "Reshape Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 6adde5da3bb469384f59eb5e9dfe5cb642b3eec5
source_lang: en
---
# Křivka

Křivka ohne rovný objekt do oblouku nebo kruhového tvaru. Ohyb můžete řídit zadáním úhlu nebo průměru, kolem kterého se objekt obtočí.

<!--  Before and after showing a straight bar being curved into an arc -->
![20260506 155243 paste 20260506 155243](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-155243-paste-20260506-155243.jpg)

## Jak ji použít

1. Vyberte objekt
2. Použijte operaci **Křivka** z nabídky Přetvarovat
3. Zvolte typ ohybu Úhel nebo Průměr
4. Upravte parametry tak, abyste dosáhli požadovaného zakřivení

## Parametry

- **Typ ohybu** - Zvolte mezi:
  - **Úhel** - Zadejte přímo úhel ohybu (1–360 stupňů)
  - **Průměr** - Zadejte průměr kružnice, kolem které se díl obtočí
- **Směr ohybu** - Ohnout nahoru nebo Ohnout dolů
- **Počáteční procento** - Kde po délce objektu ohyb začíná (0–100 %)
- **Rozdělit síť** - Rozdělí síť pro hladké křivky (výchozí: zapnuto)
- **Min. počet stran na otáčku** - Minimální počet segmentů sítě na celou otáčku. Vyšší hodnoty = hladší křivky

### Rozšířené parametry

- **Počáteční procento ohybu** - Procento zleva, kde ohyb začíná
- **Procento ohybu na konci** - Procento zleva, kde ohyb končí

## Tipy

- Pomocí operace Křivka vytvoříte z rovných polotovarů oblouky, prstence a ohnuté konzoly
- Nastavení úhlu na 360 obtočí objekt do úplného prstence
- U ostrých ohybů zvyšte hodnotu Min. počet stran na otáčku pro hladší výsledky
- Objekt se ohýbá po své délce (osa X)

## Související

- [Zkroucení](twist.md) - Otáčení podél výšky místo ohýbání
- [Torus](../../primitives/torus.md) - Hotový tvar prstence
