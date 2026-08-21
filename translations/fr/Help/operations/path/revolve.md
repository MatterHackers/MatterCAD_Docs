---
title: Révolution
articleKey: RevolveObject3D
parent: "Path Operations"
grand_parent: "Operations"
nav_order: 6
source_hash: a63ebb08d982178e0e59f0b9f07c3c0dca53148b
source_lang: en
---
# Révolution

La révolution fait tourner un chemin 2D autour d'un axe pour créer un solide de révolution 3D. C'est ainsi que l'on crée des vases, des bols, des roues et d'autres objets à symétrie de révolution.

<!--  Before and after showing a profile path being revolved into a vase shape -->
![20260506 102004 paste 20260506 102004](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-102004-paste-20260506-102004.jpg)


## Utilisation

1. Sélectionnez un chemin 2D
2. Appliquez **Révolution** depuis le menu des opérations de chemin
3. Ajustez la plage de rotation, la position de l'axe et le nombre de côtés

## Paramètres

- **Rotation** - Angle de rotation total de la révolution (par défaut : 0, plage : 0-360). Réglez sur 360 pour une révolution complète.
- **Position de l'axe** - Décalage de l'axe de rotation par rapport au centre du chemin (par défaut : 0, plage : -30 à 30). Une valeur positive éloigne l'axe du chemin, créant une ouverture plus grande.
- **Angle de départ** - Point où commence la révolution (par défaut : 0)
- **Angle final** - Point où se termine la révolution (par défaut : 45). Réglez sur 360 pour une révolution complète.
- **Côtés** - Nombre de segments autour de la révolution (par défaut : 30). Plus il y en a, plus la surface est lisse.

## Astuces

- Utilisez la Position de l'axe pour contrôler le diamètre intérieur de la forme obtenue par révolution
- Réglez l'Angle de départ et l'Angle final à moins de 360 pour créer des révolutions partielles (arches, gouttières)
- Dessinez le profil de votre vase ou de votre bol, puis appliquez-lui une révolution pour obtenir une symétrie parfaite
- Un [Chemin en cercle](../../2d-paths/circle-path.md) soumis à une révolution crée un tore

## Voir aussi

- [Extrusion linéaire](linear-extrude.md) - Extruder tout droit vers le haut au lieu d'effectuer une révolution
- [Chemins 2D](../../2d-paths/index.md) - Créer des profils à faire tourner en révolution
- [Tore](../../primitives/torus.md) - Une forme d'anneau de révolution prête à l'emploi
