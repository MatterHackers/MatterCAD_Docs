---
title: Seskupování
parent: "Workspace"
nav_order: 3
source_hash: 82b506a886e270535b5bd58c3913f49328abc4d5
source_lang: en
---
# Seskupování

Seskupování spojuje více objektů do jediného celku, který lze přesouvat, kopírovat a upravovat jako jeden objekt. Na rozdíl od operace [Sloučit](../operations/boolean/combine.md) seskupení geometrii nespojí -- každý objekt zůstává uvnitř skupiny samostatný.

<!-- Screenshot showing objects before and after grouping, with the design tree showing the group hierarchy -->
![20260318 193104 paste 20260318 193104](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193104-paste-20260318-193104.jpg)

![20260318 193235 paste 20260318 193235](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193235-paste-20260318-193235.jpg)

![20260318 193138 paste 20260318 193138](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193138-paste-20260318-193138.jpg)


## Jak na to

### Seskupení objektů

1. Vyberte dva nebo více objektů (pro vícenásobný výběr použijte Shift-klik nebo Ctrl-klik)
2. Klikněte na tlačítko **Seskupit** na panelu nástrojů
3. Objekty jsou nyní seskupené -- pohybují se společně jako jeden celek

### Rozdělení skupiny objektů

1. Vyberte skupinu
2. Klikněte na tlačítko **Rozdělit skupinu** na panelu nástrojů
3. ![20260318 193354 paste 20260318 193354](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-193354-paste-20260318-193354.jpg)
4. Jednotlivé objekty jsou obnoveny jako samostatné položky

Rozdělení skupiny se také pokusí oddělit více těles v rámci jednoho importovaného souboru STL, pokud takový obsahuje.

## Seskupit vs. Sloučit

| Vlastnost | Seskupit | Sloučit |
|---------|-------|---------|
| Objekty zůstávají samostatné | Ano | Ne |
| Lze později rozdělit skupinu | Ano | Ne (destruktivní) |
| Spojuje překrývající se geometrii | Ne | Ano |
| Objekty mohou mít různé barvy | Ano | Barvy zachovány pro jednotlivé plochy |
| Použití | Organizace a přesouvání | Vytváření jednolitých těles |

## Tipy

- Skupiny lze vnořovat -- můžete seskupit objekty, které už ve skupinách jsou
- Vyberte skupinu a podívejte se do stromu návrhu, kde uvidíte a můžete vybrat jednotlivé objekty uvnitř ní
- Seskupování je nedestruktivní a vždy je lze vrátit zpět pomocí funkce Rozdělit skupinu

## Související

- [Sloučit](../operations/boolean/combine.md) - Sloučí objekty do jednoho tělesa namísto jejich seskupení
- [Výběr](selection.md) - Jak vybrat více objektů pro seskupení
- [Komponenty](components.md) - Vytvářejte opakovaně použitelné parametrické skupiny
