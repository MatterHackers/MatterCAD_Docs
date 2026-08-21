---
title: Stjerne-bane
articleKey: StarPathObject3D
parent: "2D Paths"
nav_order: 5
source_hash: 74d92e4171c452cd10069921636e45d7ef9dc70e
source_lang: en
---
# Stjerne-bane

En stjerneformet 2D-bane med konfigurerbart antall punkter og indre/ytre radius. Brukes sammen med [Lineær ekstrudering](../operations/path/linear-extrude.md) for å lage 3D-stjerneformer.

<!-- Screenshot of a Star Path on the workspace -->
![20260506 080319 paste 20260506 080319](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080319-paste-20260506-080319.jpg)


## Parametere

- **Punkter** - Antall stjernespisser
- **Ytre radius** - Avstand fra sentrum til spissen av hvert punkt
- **Indre radius** - Avstand fra sentrum til dalene mellom punktene

## Tips

- Forholdet mellom Indre og Ytre radius bestemmer hvor "spiss" stjernen er. En liten Indre radius gir skarpe, markerte spisser.
- Sett Punkter til 5 for en klassisk stjerne, 6 for en davidsstjerne, eller høyere for tannhjullignende former
- Bruk [Glatt bane](../operations/path/smooth-path.md) på en Stjerne-bane for å lage avrundede stjerneformer

## Relatert

- [Sirkel-bane](circle-path.md) - En glatt sirkel
- [Tannhjul 2D](../mechanical/gear-2d.md) - En ekte tannhjulprofil
- [Lineær ekstrudering](../operations/path/linear-extrude.md) - Gi baner høyde
