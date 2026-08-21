---
title: Úprava objektů
parent: "Getting Started"
nav_order: 3
source_hash: 5190f3e59be7ea02497903b15c1956ed68b4d270
source_lang: en
---
# Úprava objektů

MatterCAD nabízí intuitivní ovládací prvky přímo ve 3D zobrazení pro přesouvání, otáčení a změnu měřítka objektů. Můžete také upravovat parametry objektu v panelu Vlastnosti.

## Přesouvání dílů


- **Přetažení po podložce** – Klikněte a přetáhněte libovolný objekt, chcete-li s ním posouvat po ploše pracovního prostoru
- **Pohyb nahoru a dolů** – Pomocí svislého ovládacího prvku se šipkou v horní části vybraného objektu upravte jeho výšku (pozici Z)
- Pro přesné umístění použijte operaci [Posunout](../operations/transform/translate.md) nebo zadejte přesné hodnoty v panelu Vlastnosti

## Otáčení dílů

![20260324 080843 paste 20260324 080843](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080843-paste-20260324-080843.jpg)

Klikněte na některý z **rohových ovládacích prvků otáčení**, které se zobrazí po výběru objektu. Umožňují otáčet objektem v rovině daného ovládacího prvku.

- Přejeďte myší nad některý z indikátorů úhlu, chcete-li přichytit otáčení po **45stupňových krocích**
- Pro přesné otočení použijte operaci [Otočit](../operations/transform/rotate.md) a zadejte přesný úhel

## Změna měřítka dílů

![20260324 080819 paste 20260324 080819](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080819-paste-20260324-080819.jpg)


Kliknutím na některý z **rohových ovládacích prvků měřítka** změníte velikost dílu v pracovním prostoru.

- Přetažením rohu změníte měřítko proporcionálně
- Pro přesné rozměry nebo neproporcionální změnu měřítka použijte operaci [Měřítko](../operations/transform/scale.md), kde můžete nastavit přesné rozměry nebo změnit měřítko každé osy nezávisle

## Úprava parametrů

Když vyberete objekt, jeho parametry se zobrazí v panelu Vlastnosti na pravé straně obrazovky. Například:

- **Kvádr** zobrazuje Šířku, Hloubku, Výšku a volitelné ovládací prvky Zaoblení
- **Válec** zobrazuje Průměr, Výšku a Strany
- Objekt **Text** zobrazuje obsah textu, písmo, velikost a výšku

Hodnoty můžete zadávat přímo, používat posuvníky nebo zadat [výrazy](../workspace/expressions.md) pro parametrické vztahy.

## Kontextová nabídka

Kliknutím pravým tlačítkem na libovolný objekt získáte přístup k dalším možnostem, mezi které patří:

- Kopírovat, Vyjmout, Odstranit
- Seskupit / Rozdělit skupinu
- Dostupné operace pro vybraný objekt
- Nápověda pro konkrétní typ objektu (je-li k dispozici)

## Tipy

- Podržte **Shift** při klikání, chcete-li vybrat více objektů, a poté je přesouvejte nebo s nimi pracujte společně
- Stiskněte **Ctrl+Z**, chcete-li vrátit zpět jakoukoli provedenou změnu
- Použijte [Zarovnat](../operations/placement/align.md) k přesnému umístění více objektů vůči sobě navzájem
- Stiskněte **mezerník**, chcete-li zrušit výběr

## Související

- [Navigace ve výřezu](viewport-navigation.md) – Jak otáčet, posouvat a přibližovat zobrazení
- [Výběr](../workspace/selection.md) – Podrobné chování výběru
- [Operace transformace](../operations/transform/index.md) – Přesné ovládací prvky transformace
- [Klávesové zkratky](../workspace/keyboard-shortcuts.md) – Všechny dostupné zkratky
