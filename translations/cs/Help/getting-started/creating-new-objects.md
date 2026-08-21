---
title: Vytváření nových objektů
parent: "Getting Started"
nav_order: 2
source_hash: 3eccb5aac5bb6f4d88f1ca3583eedd2f70384eeb
source_lang: en
---
# Vytváření nových objektů

MatterCAD nabízí bohatou sadu nástrojů pro vytváření 3D objektů. Můžete začít základními tělesy, použít specializované nástroje jako text a QR kódy nebo vytvářet složité tvary pomocí booleovských operací a polí.

![20260324 081122 paste 20260324 081122](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081122-paste-20260324-081122.jpg)

## Přidávání základních těles

Nejrychlejším způsobem, jak začít návrh, je přidání základních těles. Otevřete panel **Základní tělesa** v knihovně a kliknutím na libovolný tvar jej přidáte do pracovní plochy. K dispozici jsou tato základní tělesa:

- **Základní tvary** – Kvádr, Válec, Koule, Kužel, Torus, Prstenec, Jehlan, Klín a jejich poloviční varianty
- **Text a speciální** – Text, Braille, QR kód, Obrázkový objekt, SVG objekt

Každé základní těleso má parametry, které můžete po jeho výběru upravit v panelu **Vlastnosti**. Například Kvádr má ovládací prvky Šířka, Hloubka a Výška. Podrobnosti o jednotlivých tvarech najdete v článku [Základní tělesa](../primitives/index.md).

## Panel nástrojů operací

![20260324 081005 paste 20260324 081005](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081005-paste-20260324-081005.jpg)

Panel nástrojů v horní části pohledu vám poskytuje rychlý přístup k běžným operacím:

- **Zpět / Znovu** – Vrátí nebo znovu provede změny. Můžete také použít **Ctrl+Z** pro krok zpět a **Ctrl+Y** pro krok vpřed
- **Seskupit / Rozdělit skupinu** – Sloučí vybrané objekty do skupiny, která se přesouvá a pracuje jako jeden celek, nebo skupinu rozdělí
- **Kopírovat / Odstranit** – Duplikuje nebo odebere vybrané objekty. Fungují i standardní zkratky **Ctrl+C**, **Ctrl+X** a **Ctrl+V**
- **Zarovnat** – Umístí více objektů vůči sobě navzájem
- **Booleovské operace** – [Sloučit](../operations/boolean/combine.md), [Odečíst](../operations/boolean/subtract.md), [Průnik](../operations/boolean/intersect.md) a [Odečíst a nahradit](../operations/boolean/subtract-and-replace.md)
- **Pole** – Vytvoří [lineární, radiální, křivkové a transformační vzory](../operations/array/array.md) duplikovaných objektů
- **Transformace** – Použije operace [Otočit](../operations/transform/rotate.md), [Měřítko](../operations/transform/scale.md), [Zrcadlit](../operations/transform/mirror.md) a další úpravy

## Vytváření složitých tvarů

Většina návrhů v MatterCADu vzniká kombinováním jednoduchých tvarů:

1. **Začněte základními tělesy** – Přidejte základní tvary, které potřebujete
2. **Umístěte je** – Přesuňte a otočte objekty tak, aby se překrývaly tam, kde potřebujete
3. **Použijte booleovské operace** – Pomocí operace [Sloučit](../operations/boolean/combine.md) tvary spojíte dohromady nebo pomocí operace [Odečíst](../operations/boolean/subtract.md) vyříznete jeden tvar z druhého
4. **Dolaďte** – Pomocí operací [Přetvarovat](../operations/reshape/index.md), jako jsou Zkosení, Křivka nebo Zkroucení, přidejte detaily

## Související

- [Základní tělesa](../primitives/index.md) – Kompletní přehled všech základních těles
- [Přidávání existujících objektů](adding-existing-objects.md) – Importujte soubory místo vytváření od nuly
- [Booleovské operace](../operations/boolean/index.md) – Spojujte tvary do složitých forem
- [Úpravy objektů](editing-objects.md) – Přesouvejte, otáčejte a měňte měřítko objektů po jejich vytvoření
