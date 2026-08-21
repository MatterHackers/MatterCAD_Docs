---
title: Zmenšit
articleKey: DecimateObject3D
parent: "Mesh Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 58a2573b968808e98203832142fa8bacf7a9cf99
source_lang: en
---
# Zmenšit (Decimace)

Zmenšit sníží počet polygonů síťoviny při zachování celkového tvaru. Hodí se to pro zjednodušení velmi detailních modelů, zmenšení velikosti souboru a zrychlení operací se složitou geometrií.

![20260324 080430 paste 20260324 080430](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080430-paste-20260324-080430.jpg)


## Jak se používá

1. Vyberte objekt
2. Použijte operaci **Zmenšit** z nabídky Síťovina
3. Zvolte svůj cíl (počet nebo procenta) a upravte jej

## Parametry

- **Režim** - Zvolte, jak zadat cíl:
  - **Procento** - Zachová procentní podíl původních polygonů (výchozí: 50 %)
  - **Počet** - Cílem je konkrétní počet polygonů
- **Počet polygonů zdroje** - Původní počet polygonů (pouze pro čtení)
- **Cílová procenta** - Procento polygonů, které se mají zachovat (viditelné v režimu Procento)
- **Cílový počet** - Přesný počet polygonů, které se mají zachovat (viditelné v režimu Počet)
- **Počet po procentuální redukci** - Výsledný počet polygonů po redukci podle procent (pouze pro čtení)
- **Zachovat povrch** - Promítne vrcholy zpět na původní povrch pro vyšší přesnost (pomalejší, ale věrnější původnímu tvaru)

## Tipy

- Redukce o 50 % obvykle dobře zachová vizuální kvalitu
- Zapněte Zachovat povrch, když je přesnost důležitější než rychlost
- Snížení počtu polygonů zrychlí booleovské operace na složitých importovaných modelech
- Velmi nízké počty polygonů viditelně degradují tvar -- před potvrzením výsledek zkontrolujte

## Související

- [Opravit](repair.md) - Oprava problémů se síťovinou
