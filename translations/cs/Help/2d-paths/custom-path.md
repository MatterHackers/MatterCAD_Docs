---
title: Vlastní cesta
articleKey: CustomPathObject3D
parent: "2D Paths"
nav_order: 3
source_hash: 3633c708477de3ac77d3547b730c33f7e4431cf6
source_lang: en
---
# Vlastní cesta

Nakreslete vlastní 2D cestu pomocí řídicích bodů. Získáte tak úplnou volnost při vytváření libovolného 2D tvaru, který lze následně vytáhnout nebo rotovat do 3D objektu.

<!-- Screenshot showing a custom path being edited with control points -->
![20260506 080247 paste 20260506 080247](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080247-paste-20260506-080247.jpg)


## Jak ji použít

1. Přidejte **Vlastní cesta** z knihovny 2D cest
2. Upravte řídicí body a definujte tak svůj tvar
3. Použijte [Lineární extruze](../operations/path/linear-extrude.md) nebo jiné operace s cestami k vytvoření 3D objektu

## Otevřené a uzavřené cesty

Zaškrtávací políčko **Uzavřeno** určuje, zda cesta spojuje svůj poslední bod zpět s prvním.

- **Uzavřeno** (výchozí nastavení) způsobí, že cesta ohraničuje oblast. Tu vyplňuje [Lineární extruze](../operations/path/linear-extrude.md) a [Rotovat](../operations/path/revolve.md).
- **Otevřít** změní cestu na čáru. Čára nic neuzavírá, takže se ve scéně zobrazuje jako tenký pásek podél své délky, nikoli jako vyplněný tvar. Pomocí [Nafouknout cestu](../operations/path/inflate-path.md) jí dáte šířku a proměníte ji zpět v něco pevného.

Dvě věci, které je dobré vědět, než zrušíte zaškrtnutí **Uzavřeno**:

- **Opětovné uzavření není krok zpět.** Otevřením cesty zahodíte její uzavírací segment. Pokud byl tento segment zakřivený, opětovné zaškrtnutí **Uzavřeno** vrátí přímou čáru, nikoli křivku. Použijte raději Ctrl+Z – krok zpět obnoví původní cestu přesně.
- **Některé kontury se otevřít odmítnou.** Kontura, které by zbyly méně než dva body – například kapka nakreslená jediným bodem a křivkou, která se k němu vrací – zůstane uzavřená, místo aby se zhroutila do něčeho, co byste už neviděli ani neklikli. Totéž platí pro konturu obsahující kvadratickou křivku, jaká se může vyskytnout v importovaném SVG: jejím otevřením by se křivka zploštila do rohu. Odmítnutí platí pro jednotlivé kontury, takže zbytek cesty se přesto otevře.

Pokud má cesta několik kontur a ty se neshodují, zaškrtávací políčko se zobrazí jako otevřené. Jeho zaškrtnutím sjednotíte všechny kontury.

Operace, které potřebují oblast, otevřenou cestu za vás uzavřou, místo aby ji odmítly. Lineární extruze, Rotovat, Odečíst a další booleovské operace to dělají všechny, takže otevřená cesta se vytáhne do stejného tělesa jako její uzavřená verze.

## Tipy

- Vlastní cesta použijte, když žádný z vestavěných tvarů cest neodpovídá tomu, co potřebujete
- Pro import tvarů z externích vektorových editorů viz [SVG objekt](../primitives/svg-object.md)
- Chcete-li nakreslit čáru a proměnit ji v součást, zrušte zaškrtnutí **Uzavřeno**, použijte [Nafouknout cestu](../operations/path/inflate-path.md) k dodání tloušťky a poté [Lineární extruze](../operations/path/linear-extrude.md) k dodání výšky

## Související

- [Kruhová cesta](circle-path.md) – Hotový kruh
- [Obdélníková cesta](box-path.md) – Hotový obdélník
- [SVG objekt](../primitives/svg-object.md) – Importovat vektorové cesty ze souborů SVG
- [Lineární extruze](../operations/path/linear-extrude.md) – Dodá cestám výšku
