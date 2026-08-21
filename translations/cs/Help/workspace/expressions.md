---
title: Výrazy
parent: "Workspace"
nav_order: 2
source_hash: 79a2f2c42d81f7fca56a87ad89f69e4303ed0ae5
source_lang: en
---
# Výrazy

Mnoho parametrů v MatterCADu přijímá místo prostých čísel matematické výrazy. To umožňuje parametrické navrhování, kdy změna jedné hodnoty automaticky aktualizuje související rozměry.

<!--  Screenshot showing an expression being entered in a parameter field -->
![20260318 193631 paste 20260318 193631](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193631-paste-20260318-193631.jpg)


## Jak to použít

Místo zadání prostého čísla do pole parametru můžete napsat matematický výraz. Například:

- `20 + 5` se vyhodnotí jako 25
- `pi * 10` se vyhodnotí jako 31.416
- `width * 2` odkazuje na jiný parametr s názvem „width“

## Dostupné konstanty

- **pi** – 3,14159... (poměr obvodu k průměru)
- **tau** – 6,28318... (2 * pi, celá otáčka v radiánech)

## Podporované operace

- Sčítání: `+`
- Odčítání: `-`
- Násobení: `*`
- Dělení: `/`
- Závorky: `(` a `)` pro seskupování

## Tipy

- Výrazy jsou podporovány v každém poli, které má v kódu `DoubleOrExpression`, `IntOrExpression` nebo `StringOrExpression` – v praxi je přijímá většina číselných polí v návrhových nástrojích
- Pomocí výrazů vytvářejte vztahy mezi parametry – například nastavte průměr otvoru na `outer_diameter - 4`, aby měl vždy stěny o tloušťce 2 mm
- Výrazy se automaticky aktualizují, když se změní odkazované hodnoty
- Použijte [List proměnných](variable-sheet.md), když má několik objektů sdílet stejné pojmenované hodnoty nebo vzorce
- Výrazy můžete použít v operacích [Pole](../operations/array/index.md) k vytváření parametrických vzorů

## Související

- [Komponenty](components.md) – Vytvářejte znovu použitelné parametrizované návrhy
- [List proměnných](variable-sheet.md) – Ukládejte sdílené hodnoty a vzorce pro návrh
- [Úprava objektů](../getting-started/editing-objects.md) – Práce s parametry objektu
