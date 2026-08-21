---
title: Text
articleKey: TextObject3D_2
parent: "Primitives"
nav_order: 16
source_hash: 526f3190c7b2150243499b5874ac455d74810bb2
source_lang: en
---
# Text

Vytvořte 3D vytlačený text s přizpůsobitelným obsahem, písmem, velikostí a výškou. Textové objekty jsou skvělé pro popisky, cedule, jmenovky a dekorativní nápisy.

<!--  Screenshot of a 3D Text object on the workspace showing extruded letters -->
![20260318 184207 paste 20260318 184207](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184207-paste-20260318-184207.jpg)


## Jak jej používat

1. Přidejte základní těleso **Text** z panelu Základní tělesa
2. Do pole **Název** v panelu Vlastnosti napište svůj text
3. Podle potřeby upravte písmo, velikost a výšku vytlačení

## Parametry

- **Název** – Obsah textu, který se má zobrazit
- **Velikost bodu** – Velikost písma. Odpovídá standardnímu tiskovému měřítku – velikost 12 bodů v MatterCAD odpovídá 12bodovému písmu na 2D tiskárně
- **Výška** – Výška vytlačení (jak vysoko text vystupuje nad povrch)
- **Font** – Vyberte z dostupných systémových písem

## Tipy

- Pomocí operace [Odečíst](../operations/boolean/subtract.md) text do povrchu vyryjete, místo abyste jej nechali vystupovat
- U velmi malého textu zvyšte Velikost bodu a poté celý objekt zmenšete pomocí operace [Měřítko](../operations/transform/scale.md) – získáte lepší detaily
- Každé písmeno v textu je samostatná cesta, která se vytlačuje společně s ostatními

## Související

- [Braille](braille.md) – Generovat text v Braillově písmu vhodný pro 3D tisk
- [QR kód](qr-code.md) – Generovat QR kód jako 3D objekt
- [Objekt z obrázku](image-object.md) – Převod obrázků do 3D
