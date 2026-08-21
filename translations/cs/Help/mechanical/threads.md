---
title: Závity
articleKey: ThreadsObject3D_2
parent: "Mechanical Parts"
nav_order: 3
source_hash: 7d881b3293a508e102d3a4b845cdfd4eb9c34fa8
source_lang: en
---
# Závity

Vytvořte šroubové závity s nastavitelným průměrem, roztečí a profilem závitu. Závity lze použít samostatně jako šrouby, nebo je odečíst od jiných objektů a vytvořit tak závitové otvory.

<!-- AUTO_IMAGE: type=from_thumbnail item=threads file=mechanical_threads -->
![mechanical_threads](https://matterhackers.github.io/MatterCAD_Docs/assets/mechanical_threads.png)

## Jak na to

1. Přidejte **Závity** z nástrojů Mechanické nebo z panelu Základní tělesa
2. Nastavte průměr, rozteč a počet rotací
3. Volitelně zapněte „Použít jako otvor“ pro vytváření závitových otvorů

## Parametry

### Použití

- **Použít jako otvor** – Je-li zapnuto, závity se vytvoří s přídavnou tolerancí pro použití jako odečítaný otvor (výchozí: vypnuto)
- **Tolerance** – Přídavná vůle pro uložení při použití jako otvor (výchozí: 0,2 mm, zobrazí se, když je zapnuto Použít jako otvor)

### Vlastnosti

- **Průměr** – Vnější průměr závitové části (výchozí: 10 mm)
- **Rozteč** – Vzdálenost mezi jednotlivými závity (výchozí: 2 mm). Menší rozteč = jemnější závity
- **Měřítko závitu** – Šířka závitů jako poměr k rozteči (výchozí: 1,0, rozsah: 0,1–1,0)
- **Rotace** – Počet úplných otáček závitu (výchozí: 10)

### Geometrie

- **Strany** – Počet segmentů po obvodu (výchozí: 40). Více = hladší

### Hroty (konce závitu)

- **Měřítko hrotu** – Jak moc se mají konce závitu zkosit (výchozí: 0, rozsah: 0–1). Nastavte hodnotu vyšší než 0 pro vytvoření zúženého náběhu na koncích
- **Úhel hrotu** – Úhel, na kterém se hroty zužují (výchozí: 90 stupňů)

## Tipy

- Vytvoření závitového otvoru: zapněte „Použít jako otvor“, umístěte závity a použijte [Odečíst](../operations/boolean/subtract.md) od svého objektu
- Při použití jako otvor přidejte Toleranci, aby k sobě vytištěné díly pasovaly
- Standardní metrické rozteče závitů: M3=0,5 mm, M4=0,7 mm, M5=0,8 mm, M6=1,0 mm, M8=1,25 mm, M10=1,5 mm
- Pomocí Měřítka hrotu vytvořte náběh, který usnadní zašroubování

## Související

- [Ozubené kolo](gears.md) – Vytvoření tvarů mechanických ozubených kol
- [Válec](../primitives/cylinder.md) – Hladký kulatý sloupec (bez závitů)
- [Odečíst](../operations/boolean/subtract.md) – Vyříznutí závitů z jiných objektů pro vytvoření otvorů
