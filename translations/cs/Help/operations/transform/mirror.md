---
title: Zrcadlit
articleKey: MirrorObject3D_2
parent: "Transform Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: 8a8de28f5e429177d4b0092d0756387eb6b83a70
source_lang: en
---
# Zrcadlit

Zrcadlit vytvoří odraženou kopii objektu podle jedné ze tří hlavních os. Výsledkem je zrcadlově převrácená verze původního tvaru.

<!--  Before and after showing an object mirrored across the X axis -->
![20260506 160651 paste 20260506 160651](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-160651-paste-20260506-160651.jpg)


## Jak to použít

1. Vyberte objekt
2. Použijte operaci **Zrcadlit** z nabídky Transformace
3. Zvolte osu, podle které se má zrcadlit

## Parametry

- **Zrcadlení zapnuto** – Osa, podle které se zrcadlí:
  - **Osa X** – Převrátí objekt zleva doprava
  - **Osa Y** – Převrátí objekt zepředu dozadu
  - **Osa Z** – Převrátí objekt shora dolů

## Tipy

- Zrcadlení je vystředěno podle ohraničujícího kvádru objektu, takže zrcadlený výsledek zabírá stejný prostor jako originál
- Normály stěn se po zrcadlení automaticky opraví, aby zůstalo zachováno správné vykreslování
- Pomocí operace Zrcadlit vytvoříte symetrické návrhy – vymodelujte jednu polovinu, poté ji zrcadlete a použijte [Sloučit](../boolean/combine.md) s originálem
- Zrcadlit je nedestruktivní operace: osu zrcadlení můžete kdykoli změnit

## Související

- [Otočit](rotate.md) – Otočení objektu místo zrcadlení
- [Měřítko](scale.md) – Změna velikosti objektu
- [Sloučit](../boolean/combine.md) – Sloučení originálu a zrcadlené kopie do jednoho objektu
