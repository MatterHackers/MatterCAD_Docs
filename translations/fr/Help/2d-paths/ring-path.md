---
title: Chemin Anneau
articleKey: RingPathObject3D
parent: "2D Paths"
nav_order: 4
source_hash: 3ee3dd9ab102cfabf1e79d1093b237fb90f12aca
source_lang: en
---
# Chemin Anneau

Une forme d'anneau 2D -- un cercle percé d'un trou circulaire en son centre. À utiliser avec [Extrusion linéaire](../operations/path/linear-extrude.md) pour créer des formes de tube ou de rondelle.

<!-- Screenshot of a Ring Path on the workspace -->
![20260506 080211 paste 20260506 080211](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080211-paste-20260506-080211.jpg)

## Paramètres

- **Diamètre extérieur** - Le diamètre extérieur de l'anneau
- **Diamètre intérieur** - Le diamètre du trou central

## Astuces

- L'épaisseur de paroi de l'anneau vaut (Diamètre extérieur - Diamètre intérieur) / 2
- L'extrusion d'un Chemin Anneau crée un tube semblable à la primitive [Anneau](../primitives/ring.md)

## Voir aussi

- [Chemin Cercle](circle-path.md) - Un cercle plein (sans trou)
- [Anneau](../primitives/ring.md) - Une forme de tube 3D prête à l'emploi
- [Extrusion linéaire](../operations/path/linear-extrude.md) - Donner de la hauteur aux chemins
