---
title: List proměnných
articleKey: SheetObject3D
parent: "Workspace"
nav_order: 3
source_hash: 3137a4da2b9d2086d4dcace156435caca288dd79
source_lang: en
---
# List proměnných

List proměnných uchovává sdílené hodnoty pro návrh. Použijte jej, když má několik objektů odkazovat na stejné rozměry, počty, popisky nebo vzorce. Změna hodnoty v listu přepočítá závislé objekty, takže parametrické návrhy zůstanou konzistentní, aniž byste museli upravovat každý objekt zvlášť.

<!--  Screenshot of the Variable Sheet editor showing named cells, formulas, and the Documentation button -->
![20260507 080914 paste 20260507 080914](https://matterhackers.github.io/MatterCAD_Docs/assets/20260507-080914-paste-20260507-080914.jpg)


## Jak přidat List proměnných

1. Otevřete knihovnu a přidejte do scény **List proměnných**.
2. Vyberte objekt List proměnných, čímž se zobrazí editor listu.
3. Vyberte buňku a poté zadejte **Název** a hodnotu nebo vzorec.
4. Název buňky použijte v dalších polích návrhu, která podporují výrazy.

## Úprava buněk

Každá buňka má dvě upravitelné části:

- **Název** - Volitelný název proměnné pro danou buňku. U názvů se nerozlišují velká a malá písmena, mezery se převádějí na podtržítka a duplicitní názvy se automaticky upraví.
- **Výraz** - Hodnota buňky. Prostý text nebo čísla se ukládají přímo. Vzorce začínají znakem `=`.

Na buňky lze odkazovat také pomocí adresy, například `A1` nebo `B2`. Pro parametry návrhu jsou obvykle srozumitelnější pojmenované buňky, protože popisují záměr, například `wall_thickness`, `outer_diameter` nebo `hole_count`.

## Vzorce

Vzorec začněte znakem `=`, aby se v listu vyhodnotil:

- `=20 + 5` vrátí `25`
- `=pi * 10` vrátí `31.41592653589793`
- `=A1 * 2` odkazuje na jinou buňku podle adresy
- `=wall_thickness + 4` odkazuje na pojmenovanou buňku

List podporuje aritmetiku, závorky, porovnávací operátory, běžné funkce `Math`, jako jsou `sin`, `cos`, `sqrt` a `round`, a konstanty včetně `pi`, `tau` a `e`.

## Použití hodnot z listu v objektech

Většina číselných polí v MatterCAD podporuje výrazy. Chcete-li použít hodnotu z listu v parametru objektu, uveďte před odkazem znak `=`:

- Nastavte **Šířka** objektu Kvádr na `=case_width`.
- Nastavte **Počet** objektu Pole na `=hole_count`.
- Nastavte hodnotu **Odsazení** operace Posunout na `=wall_thickness * 2`.

Při změně listu MatterCAD přepočítá objekty, které na něm závisejí.

## Text a pomocné funkce

Buňky Listu proměnných mohou obsahovat text i čísla. Textové hodnoty se hodí pro generované popisky, čísla dílů, importovaná data a vlastní návrhové aplikace.

Mezi užitečné pomocné funkce patří:

- `concat()` nebo `strcat()` - Spojí text nebo hodnoty dohromady.
- `substring()` - Vyjme část textové hodnoty.
- `split()` - Rozdělí text a vrátí jednu položku.
- `count()` - Spočítá položky oddělené oddělovačem v textu.
- `substitute()` - Nahradí text.
- `rand(seed)` - Vygeneruje deterministickou náhodnou hodnotu, je-li zadáno počáteční číslo (seed).
- `importdata()` - Načte hodnotu z URL nebo z místní cesty k souboru.

## Tipy

- U hodnot používaných jinými objekty upřednostňujte výstižné názvy před adresami buněk.
- Klíčové rozměry umístěte blízko levého horního rohu listu, aby se snadno hledaly.
- Pro odvozené hodnoty používejte vzorce, například `inner_diameter = outer_diameter - wall_thickness * 2`.
- Vyhněte se používání vyhrazených slov, jako jsou `pi`, `e`, `true`, `false`, nebo názvů funkcí jako názvů buněk.
- Pokud vzorec nelze zpracovat, MatterCAD ponechá původní vstup jako text.

## Související

- [Výrazy](expressions.md) - Použití výrazů v parametrech objektů
- [Komponenty](components.md) - Vytvoření znovupoužitelných parametrických návrhů
- [Pole](../operations/array/array.md) - Vytvoření opakovaných vzorů řízených hodnotami z listu
