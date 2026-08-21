---
title: Chemin Cercle
articleKey: CirclePathObject3D
parent: "2D Paths"
nav_order: 2
source_hash: 587edab627246f47731f9dbde2a13a00dd464807
source_lang: en
---
# Chemin Cercle

Un chemin 2D circulaire. À utiliser avec [Extrusion linéaire](../operations/path/linear-extrude.md) pour créer des cylindres, ou [Révolution](../operations/path/revolve.md) pour créer des formes de type tore.

<!-- Screenshot of a Circle Path on the workspace -->
![20260506 080110 paste 20260506 080110](https://matterhackers.github.io/MatterCAD_Docs/assets/20260506-080110-paste-20260506-080110.jpg)


## Paramètres

- **Diamètre** - Le diamètre du cercle (par défaut : 20mm)
- **Segments** - Nombre de segments de ligne composant le cercle. Plus = plus lisse

## Astuces

- Un Chemin Cercle combiné à une Extrusion linéaire produit un cylindre, semblable à la primitive [Cylindre](../primitives/cylinder.md) mais avec plus de souplesse pour construire à partir de celui-ci
- À utiliser comme base pour une Révolution afin de créer des formes d'anneau

## Voir aussi

- [Chemin Boîte](box-path.md) - Un chemin 2D rectangulaire
- [Chemin Anneau](ring-path.md) - Un cercle percé d'un trou
- [Extrusion linéaire](../operations/path/linear-extrude.md) - Donner de la hauteur aux chemins
