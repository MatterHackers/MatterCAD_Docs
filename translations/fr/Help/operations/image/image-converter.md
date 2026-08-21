---
title: Convertisseur d'images
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 1
source_hash: c1a05f9688ebe115babfad5d63fc49445af7c449
source_lang: en
---
# Convertisseur d'images

Le Convertisseur d'images transforme une image matricielle en un relief 3D où la luminosité des pixels détermine la hauteur. Les zones claires sont surélevées et les zones sombres abaissées (ou l'inverse).

![20260323 210414 paste 20260323 210414](https://matterhackers.github.io/MatterCAD_Docs/assets/20260323-210414-paste-20260323-210414.jpg)


## Utilisation

1. Ajoutez un Convertisseur d'images depuis le panneau Primitives, ou faites glisser un fichier image sur l'espace de travail
2. L'image est convertie en carte de hauteurs 3D
3. Ajustez la hauteur et les autres paramètres

## Conseils

- Les images très contrastées aux formes nettes donnent les meilleurs résultats
- Pour tracer les contours d'une image sous forme de chemins plats plutôt qu'en carte de hauteurs, utilisez [Image vers tracé](image-to-path.md)
- Pour créer des images rétroéclairées, utilisez [Lithophanie](lithophane.md)
- Vous pouvez faire glisser des images directement depuis votre bureau vers l'espace de travail
- Ajoutez une base en combinant le relief de l'image avec un [Cube](../../primitives/cube.md)

## Voir aussi

- [Image vers tracé](image-to-path.md) - Tracer les contours au lieu de créer une carte de hauteurs
- [Lithophanie](lithophane.md) - Créer des images rétroéclairées
- [Objet image](../../primitives/image-object.md) - La version primitive de l'importation d'image
