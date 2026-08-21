---
title: Ukládání a exportování
parent: "Getting Started"
nav_order: 4
source_hash: 020d4bf43f07d3ab7dbd7d585e13c99309f0c0b8
source_lang: en
---
# Ukládání a exportování

MatterCAD podporuje několik formátů souborů pro ukládání a exportování vašich návrhů. Formát, který zvolíte, závisí na tom, jak chcete soubor použít.

## Formáty pro ukládání

### MCX (nativní formát)

MCX je nativní formát souborů aplikace MatterCAD a nejlepší volba pro návrhy, které chcete později dále upravovat. Zachovává:

- Kompletní strom návrhu se všemi objekty a jejich hierarchií
- Všechny parametry a nastavení každého objektu
- Booleovské operace, pole a další operace v upravitelné podobě
- Vztahy mezi komponentami

**Použijte MCX, když:** chcete uložit svou práci a později v ní pokračovat.

### STL

STL je nejrozšířenější formát pro 3D tisk. Obsahuje pouze výslednou trojúhelníkovou síť bez jakékoli historie návrhu či parametrů.

**Použijte STL, když:** chcete svůj návrh vytisknout na 3D tiskárně nebo jej sdílet s někým, kdo MatterCAD nepoužívá.

### OBJ

OBJ (Wavefront) je běžný 3D formát podporovaný většinou 3D softwaru. Stejně jako STL obsahuje pouze geometrii sítě.

**Použijte OBJ, když:** potřebujete svůj návrh otevřít v jiném 3D softwaru, například v Blenderu nebo herním enginu.

### SVG

Export do SVG vytvoří 2D vektorový soubor z pohledu na návrh shora. To se hodí pro laserové řezání nebo CNC frézování.

**Použijte SVG, když:** potřebujete 2D obrys svého návrhu pro laserové řezání nebo gravírování.

## Jak ukládat

![20260324 080726 paste 20260324 080726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080726-paste-20260324-080726.jpg)

1. Otevřete **nabídku značky** (logo MatterCAD v levém horním rohu)
2. Zvolte **Uložit jako** pro výběr umístění a formátu
3. Vyberte formát souboru z rozevíracího seznamu formátů
4. Zvolte, kam se má soubor uložit, a klikněte na **Uložit**

Váš návrh se také automaticky ukládá během práce, takže o změny nepřijdete ani při zavření aplikace.

## Tipy

- Před exportem do STL nebo OBJ si vždy uložte kopii návrhu ve formátu MCX, abyste v něm mohli později provádět změny
- Při exportu do STL se všechny objekty ve scéně sloučí do jediné sítě
- Pokud potřebujete sdílet návrh s někým, kdo používá MatterCAD, pošlete mu soubor MCX, aby zůstala zachována plná možnost úprav
- Návrhy můžete také ukládat do své [Cloudové knihovny](../library/cloud-library.md) a mít k nim přístup z libovolného počítače

## Související

- [Přidání existujících objektů](adding-existing-objects.md) – Importování souborů do MatterCADu
- [Knihovna](../library/index.md) – Uspořádejte si uložené návrhy
- [Cloudová knihovna](../library/cloud-library.md) – Ukládejte návrhy v cloudu
