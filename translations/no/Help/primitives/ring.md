---
title: Ring
articleKey: RingObject3D
parent: "Primitives"
nav_order: 13
source_hash: fd16c400f3d8c8af13416ab57ddd8407e761d93a
source_lang: en
---
# Ring

En hul sylinder (rør) med uavhengig innvendig og ytre diameter og en angitt høyde. Også kjent som en rør- eller slangeform.

<!--  Screenshot of a Ring primitive on the workspace -->
![20260318 183848 paste 20260318 183848](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183848-paste-20260318-183848.jpg)


## Parametere

- **Ytre diameter** - Ringens utvendige bredde (standard: 20mm)
- **Innvendig diameter** - Diameteren på det hule senteret (standard: 15mm)
- **Høyde** - Hvor høy ringen er (standard: 5mm)
- **Sider** - Antall segmenter rundt omkretsen (standard: 40)

### Avanserte parametere

Aktiver **Avansert**-modus for flere kontroller:

- **Startvinkel** - Vinkelen der ringen begynner (standard: 0)
- **Sluttvinkel** - Vinkelen der ringen slutter (standard: 360). Sett den lavere enn 360 for en delvis ring
- **Rund** - Legg til avrunding på kantene (Ingen, Opp eller Ned)
- **Retning** - Rund mot den indre eller ytre kanten (synlig når Rund er aktivert)
- **Runde segmenter** - Hvor glatt avrundingen blir (synlig når Rund er aktivert)

## Tips

- Veggtykkelsen tilsvarer (Ytre diameter - Innvendig diameter) / 2
- Bruk denne til skiver, avstandsstykker, foringer og rørlignende elementer
- Sett høyden stor for rør eller liten for flate skiver
- Bruk Startvinkel og Sluttvinkel for delvise ringformer som C-klips

## Relatert

- [Torus](torus.md) - En smultringformet ring med rundt tverrsnitt
- [Sylinder](cylinder.md) - En massiv rund søyle (uten hult senter)
