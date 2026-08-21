---
title: Anneau
articleKey: RingObject3D
parent: "Primitives"
nav_order: 13
source_hash: fd16c400f3d8c8af13416ab57ddd8407e761d93a
source_lang: en
---
# Anneau

Un cylindre creux (tube) doté de diamètres intérieur et extérieur indépendants et d'une hauteur définie. Également appelé forme de tuyau ou de tube.

<!--  Screenshot of a Ring primitive on the workspace -->
![20260318 183848 paste 20260318 183848](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-183848-paste-20260318-183848.jpg)


## Paramètres

- **Diamètre extérieur** - Largeur extérieure de l'anneau (par défaut : 20mm)
- **Diamètre intérieur** - Diamètre du centre creux (par défaut : 15mm)
- **Hauteur** - Hauteur de l'anneau (par défaut : 5mm)
- **Côtés** - Nombre de segments sur le pourtour (par défaut : 40)

### Paramètres avancés

Activez le mode **Avancé** pour accéder à des commandes supplémentaires :

- **Angle de départ** - Angle où commence l'anneau (par défaut : 0)
- **Angle final** - Angle où se termine l'anneau (par défaut : 360). Définissez une valeur inférieure à 360 pour obtenir un anneau partiel
- **Arrondir** - Ajoute un arrondi aux arêtes (Aucun, Haut ou Bas)
- **Direction** - Arrondit vers l'arête interne ou externe (visible lorsque Arrondir est activé)
- **Segments d'arrondi** - Régularité de l'arrondi (visible lorsque Arrondir est activé)

## Astuces

- L'épaisseur de paroi est égale à (Diamètre extérieur - Diamètre intérieur) / 2
- Utilisez cette forme pour des rondelles, des entretoises, des bagues et des éléments tubulaires
- Définissez une hauteur importante pour des tuyaux ou faible pour des rondelles plates
- Utilisez l'Angle de départ et l'Angle final pour créer des anneaux partiels, comme des circlips

## Voir aussi

- [Tore](torus.md) - Un anneau en forme de beignet avec une section circulaire
- [Cylindre](cylinder.md) - Une colonne ronde pleine (sans centre creux)
