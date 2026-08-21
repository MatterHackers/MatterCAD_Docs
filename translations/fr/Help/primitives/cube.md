---
title: Cube
articleKey: CubeObject3D
parent: "Primitives"
nav_order: 4
source_hash: a376a9c78d88d995f3c6ce21dd5098672d6c1dfb
source_lang: en
---
# Cube

Une forme de boîte rectangulaire avec largeur, profondeur et hauteur réglables, ainsi que des arêtes arrondies en option. Le Cube est l'une des primitives les plus utilisées pour construire des conceptions.

<!--  Screenshot of a Cube primitive on the workspace -->
![20260318 183230 paste 20260318 183230](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183230-paste-20260318-183230.jpg)


## Paramètres

- **Largeur** - Taille le long de l'axe X (par défaut : 20mm)
- **Profondeur** - Taille le long de l'axe Y (par défaut : 20mm)
- **Hauteur** - Taille le long de l'axe Z (par défaut : 20mm)
- **Arrondir** - Active les arêtes arrondies
- **Rayon** - Taille de l'arrondi (visible lorsque Arrondir est activé)
- **Segments d'arrondi** - Finesse de l'arrondi, plus de segments = courbes plus lisses (visible lorsque Arrondir est activé)

## Astuces

- Utilisez un Cube comme point de départ pour des boîtes, plaques, supports et boîtiers
- Activez Arrondir pour obtenir des arêtes lisses et d'aspect professionnel
- Le Rayon ne peut pas dépasser la moitié de la plus petite dimension
- Combinez un Cube avec [Soustraire](../operations/boolean/subtract.md) pour créer des découpes et des rainures rectangulaires

## Voir aussi

- [Cylindre](cylinder.md) - Forme de colonne ronde
- [Pyramide](pyramid.md) - Forme à quatre faces effilée
- [Trou](hole.md) - Un cube préconfiguré pour la soustraction booléenne
