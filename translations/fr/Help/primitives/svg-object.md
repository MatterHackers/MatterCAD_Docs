---
title: Objet SVG
articleKey: SvgObject3D
parent: "Primitives"
nav_order: 15
source_hash: dab97cdde74d938b5612d959f83b54b4a04a49da
source_lang: en
---
# Objet SVG

Importez des fichiers SVG (Scalable Vector Graphics) et utilisez-les comme trajectoires 2D dans votre conception. Les SVG peuvent ensuite être extrudés en formes 3D à l'aide d'[Extrusion linéaire](../operations/path/linear-extrude.md) ou de [Révolution](../operations/path/revolve.md).

<!--  Screenshot showing an imported SVG path being extruded into a 3D shape -->
![20260318 184807 paste 20260318 184807](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184807-paste-20260318-184807.jpg)



## Utilisation

1. Importez un fichier SVG en le faisant glisser sur l'espace de travail ou en utilisant le bouton Ouvrir
2. Le SVG est importé en tant que trajectoire 2D
3. Appliquez [Extrusion linéaire](../operations/path/linear-extrude.md) pour lui donner de la hauteur, ou utilisez d'autres [opérations de chemin](../operations/path/index.md)

## Conseils

- Les fichiers SVG doivent contenir des formes pleines ou des trajectoires fermées pour de meilleurs résultats
- Les SVG complexes comportant de nombreuses trajectoires peuvent être plus longs à traiter
- Utilisez [Sélectionner des trajectoires](../operations/path/select-paths.md) pour travailler sur des parties spécifiques d'un SVG à trajectoires multiples
- De nombreux fichiers SVG gratuits sont disponibles en ligne pour les logos, les icônes et les motifs décoratifs

## Voir aussi

- [Image vers tracé](../operations/image/image-to-path.md) - Convertir des images matricielles en trajectoires au lieu d'utiliser un SVG
- [Texte](text.md) - Créer du texte directement sans avoir besoin d'un SVG
- [Extrusion linéaire](../operations/path/linear-extrude.md) - Donner de la hauteur à des trajectoires planes
- [Trajectoires 2D](../2d-paths/index.md) - Primitives de trajectoire intégrées
