---
title: Otočit
articleKey: RotateObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 9bdc210c5c375fe3179050e8a8916d895455ce5f
source_lang: en
---
# Otočit

Otočit otáčí objektem okolo zadané osy o daný úhel. Můžete otáčet okolo libovolného směru osy a zvolit střed otáčení.

<!--  Screenshot showing the Rotate operation with the rotation gizmo visible in the viewport -->
![20260506 160726 paste 20260506 160726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160726-paste-20260506-160726.jpg)

## Jak používat

1. Vyberte objekt
2. Použijte operaci **Otočit** z nabídky Transformace
3. Nastavte úhel a osu otáčení v panelu Vlastnosti

Objekty můžete otáčet také přímo ve výřezu kliknutím na rohové ovládací prvky otáčení na vybraném objektu. Při pohybu myší nad indikátory úhlu se hodnota přichytává po 45stupňových krocích.

## Parametry

- **Úhel** – Úhel otočení ve stupních (rozsah: 3–360). Podporuje [výrazy](../../workspace/expressions.md).
- **Otočit okolo** – Určuje osu otáčení a počáteční bod. Můžete otáčet okolo osy X, Y nebo Z, případně zadat vlastní směr.

## Tipy

- Otočení je ve výchozím nastavení vystředěno na střed ohraničujícího kvádru objektu
- U otočení o 90 stupňů usnadňují indikátory přichycení získání přesných hodnot
- Použijte operaci Otočit (namísto ovládacích prvků ve výřezu), když potřebujete přesný úhel, který není násobkem 45 stupňů
- Osu otáčení můžete změnit i po použití operace úpravou vlastnosti Otočit okolo

## Související

- [Posunout](translate.md) – Přesunout objekt o určitou vzdálenost
- [Měřítko](scale.md) – Změnit velikost objektu
- [Zrcadlit](mirror.md) – Vytvořit zrcadlový odraz
