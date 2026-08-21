---
title: Přidání existujících objektů
parent: "Getting Started"
nav_order: 1
source_hash: e384a5c024336c3c58343d262d914fa40e0b0426
source_lang: en
---
# Přidání existujících objektů

Existující 3D modely můžete do MatterCAD dostat importem souborů z počítače nebo přidáním obsahu z vestavěné knihovny.

## Z vašeho počítače

![20260324 081143 paste 20260324 081143](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081143-paste-20260324-081143.jpg)

![20260324 081240 paste 20260324 081240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081240-paste-20260324-081240.jpg)


Kliknutím na tlačítko **Otevřít** na panelu nástrojů můžete procházet a přidávat soubory z počítače. MatterCAD podporuje následující formáty importu:

- **STL** (.stl) – průmyslový standard pro 3D modely, hojně používaný pro 3D tisk
- **AMF** (.amf) – pokročilý formát podporující barvy a vícemateriálové objekty
- **OBJ** (.obj) – formát 3D grafiky Wavefront (pouze geometrie sítě)
- **3MF** (.3mf) – 3D Manufacturing Format s bohatou podporou metadat
- **MCX** (.mcx) – nativní formát MatterCAD, který zachovává všechna data a parametry návrhu
- **SVG** (.svg) – Scalable Vector Graphics, importuje se jako 2D dráhy
- **TTF / OTF** (.ttf, .otf) – soubory písem pro použití s nástrojem Text

## Přetažení myší

Soubory můžete také přetáhnout přímo z plochy nebo správce souborů do pracovní plochy MatterCAD. Podporované typy souborů se importují automaticky.

![20260324 081416 paste 20260324 081416](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081416-paste-20260324-081416.jpg)

## Z knihovny

### Postranní panel Knihovna

Kliknutím na tlačítko **Přidat obsah** na panelu nástrojů otevřete panel prohlížeče knihovny. Odtud můžete:

- procházet své uložené návrhy
- přejít do knihovny Základní tělesa s vestavěnými tvary
- přistupovat ke své Cloudové knihovně, pokud jste přihlášeni
- přetáhnout jakoukoli položku z knihovny přímo do pracovní plochy

![20260324 081446 paste 20260324 081446](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081446-paste-20260324-081446.jpg)

### Karta Knihovna

K procházení svých kolekcí můžete také použít kartu Knihovna. Klikněte pravým tlačítkem na libovolný objekt v knihovně a vyberte **Přidat do scény**, čímž jej importujete do aktuální pracovní plochy návrhu.

![20260324 081536 paste 20260324 081536](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081536-paste-20260324-081536.jpg)

## Tipy

- MCX je nejlepší formát pro pozdější úpravy návrhů, protože zachovává všechny parametry i strom návrhu
- Soubory STL obsahují pouze geometrii sítě. Pokud importujete STL, můžete na něj stále aplikovat operace, ale nelze upravovat původní parametry
- Při importu více souborů se z každého stane samostatný objekt ve scéně. K jejich uspořádání použijte [Seskupit](../workspace/grouping.md)

## Související

- [Vytváření nových objektů](creating-new-objects.md) – začněte návrh od nuly pomocí základních těles
- [Ukládání a exportování](saving-and-exporting.md) – uložte a exportujte své hotové návrhy
- [Knihovna](../library/index.md) – zjistěte více o uspořádání své knihovny návrhů
