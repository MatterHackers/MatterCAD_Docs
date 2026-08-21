---
title: Vybrat potomka
articleKey: SelectChildObject3D
parent: "Array Operations"
grand_parent: "Operations"
nav_order: 4
source_hash: f6f71d2b457b82126f272ea9354f877c36570df0
source_lang: en
---
# Vybrat potomka

Vybrat potomka vybere jednoho potomka ze skupiny objektů na základě indexu nebo názvu. To je užitečné zejména ve skriptovaných a parametrických návrzích, kde chcete dynamicky určovat, který objekt se zobrazí.

<!-- IMAGE: Screenshot showing Select Child operation with multiple children and one selected by index -->
![20260506 080526 paste 20260506 080526](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080526-paste-20260506-080526.jpg)


## Jak na to

1. Vyberte dva nebo více objektů
2. Použijte operaci **Vybrat potomka** z nabídky Duplikace
3. Zvolte **Podle indexu** nebo **Podle názvu** a určete tak, jak se potomek vybírá
4. Nastavte index nebo název, který se má shodovat

## Parametry

- **Metoda výběru** – Zvolte mezi **Podle indexu** (výběr podle pozice) nebo **Podle názvu** (výběr podle názvu objektu). Zobrazuje se jako tlačítka.
- **Index potomka** – Index vybíraného potomka počítaný od nuly (zobrazí se při použití Podle indexu). Podporuje [výrazy](../../workspace/expressions.md).
- **Název potomka** – Název vybíraného potomka (zobrazí se při použití Podle názvu). Podporuje [výrazy](../../workspace/expressions.md).

Pokud je index mimo rozsah nebo název neodpovídá žádnému potomkovi, vrátí se jako náhradní řešení první potomek. Pokud žádní potomci neexistují, nevrátí se nic.

## Použití ve skriptování

Operace Vybrat potomka je navržena tak, aby spolupracovala s výrazy a funkcí `rand()` a umožnila vytvářet dynamické návrhy řízené daty. Můžete například sestavit scénu s několika variantami objektů jako potomky a použít výraz jako `rand(42)` ve funkci indexu jako seed pro náhodný výběr jednoho z nich.

**Příklad: Náhodné knižní rekvizity pro divadelní scénu**

1. Importujte 5 různých sítí knih jako potomky operace Vybrat potomka
2. Nastavte Metodu výběru na **Podle indexu**
3. Použijte pro Index potomka výraz, například `floor(rand(seed) * 5)`, kde `seed` je proměnná listu
4. Duplikujte operaci Vybrat potomka vícekrát, pokaždé s jinou hodnotou seedu
5. Každá instance náhodně vybere z dané sady jinou knihu

Tento postup funguje pro jakýkoli scénář, kdy potřebujete vybírat ze sady variant: nábytek, dekorace, architektonické prvky nebo libovolnou kolekci zaměnitelných dílů.

## Tipy

- Zkombinujte s [Pole](array.md) a vytvořte rozmanité vzory, kde každá kopie vybírá jiného potomka
- Použijte proměnné listu pro index nebo název a řiďte výběr z tabulky
- Chování s návratem k prvnímu potomkovi znamená, že se váš návrh nikdy nerozbije, ani když je index nebo název chybný

## Související

- [Pole](array.md) – Duplikuje objekty v lineárních, radiálních, křivkových a transformačních vzorech
