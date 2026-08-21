---
title: Ring
articleKey: RingObject3D
parent: "Primitives"
nav_order: 13
source_hash: fd16c400f3d8c8af13416ab57ddd8407e761d93a
source_lang: en
---
# Ring

En hul cylinder (rør) med uafhængige indvendige og ydre diametre og en angivet højde. Kendes også som en rør- eller slangeform.

<!--  Screenshot of a Ring primitive on the workspace -->
![20260318 183848 paste 20260318 183848](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183848-paste-20260318-183848.jpg)


## Parametre

- **Ydre diameter** - Ringens udvendige bredde (standard: 20mm)
- **Indvendig diameter** - Diameteren på det hule center (standard: 15mm)
- **Højde** - Hvor høj ringen er (standard: 5mm)
- **Sider** - Antal segmenter rundt langs omkredsen (standard: 40)

### Avancerede parametre

Aktivér tilstanden **Avanceret** for yderligere indstillinger:

- **Startvinkel** - Vinklen hvor ringen begynder (standard: 0)
- **Slutvinkel** - Vinklen hvor ringen slutter (standard: 360). Sæt den til mindre end 360 for en delvis ring
- **Rund** - Tilføj afrunding til kanterne (Ingen, Op eller Ned)
- **Retning** - Afrund mod den indre eller ydre kant (vises når Rund er aktiveret)
- **Rundingssegmenter** - Afrundingens glathed (vises når Rund er aktiveret)

## Tips

- Vægtykkelsen svarer til (Ydre diameter - Indvendig diameter) / 2
- Brug denne til spændskiver, afstandsstykker, bøsninger og rørlignende detaljer
- Sæt højden højt for rør eller lavt for flade spændskiver
- Brug Startvinkel og Slutvinkel til delvise ringformer som C-clips

## Relateret

- [Torus](torus.md) - En donutformet ring med rundt tværsnit
- [Cylinder](cylinder.md) - En massiv rund søjle (uden hult center)
