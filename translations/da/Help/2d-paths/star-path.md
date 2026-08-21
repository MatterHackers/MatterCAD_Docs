---
title: Stjernesti
articleKey: StarPathObject3D
parent: "2D Paths"
nav_order: 5
source_hash: 74d92e4171c452cd10069921636e45d7ef9dc70e
source_lang: en
---
# Stjernesti

En stjerneformet 2D-sti med konfigurerbart antal punkter og indre/ydre radius. Brug den sammen med [Lineær ekstrudering](../operations/path/linear-extrude.md) til at skabe 3D-stjerneformer.

<!-- Screenshot of a Star Path on the workspace -->
![20260506 080319 paste 20260506 080319](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080319-paste-20260506-080319.jpg)


## Parametre

- **Punkter** - Antal stjernespidser
- **Ydre radius** - Afstand fra centrum til spidsen af hvert punkt
- **Indre radius** - Afstand fra centrum til dalene mellem punkterne

## Tips

- Forholdet mellem indre og ydre radius bestemmer, hvor "spids" stjernen er. En lille indre radius giver skarpe, markante spidser.
- Sæt Punkter til 5 for en klassisk stjerne, 6 for en Davidsstjerne eller højere for tandhjulslignende former
- Brug [Udjævn sti](../operations/path/smooth-path.md) på en stjernesti for at skabe afrundede stjerneformer

## Relateret

- [Cirkelsti](circle-path.md) - En glat cirkel
- [Tandhjul 2D](../mechanical/gear-2d.md) - En egentlig tandhjulsprofil
- [Lineær ekstrudering](../operations/path/linear-extrude.md) - Giv stier højde
