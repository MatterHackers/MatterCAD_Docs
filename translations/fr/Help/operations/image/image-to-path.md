---
title: Image vers tracé
articleKey: ImageToPathObject3D_2
parent: "Image Operations"
grand_parent: "Operations"
nav_order: 2
source_hash: 0145587f635ede68bfc1df37b4f0d366a03d3a6c
source_lang: en
---
# Image vers tracé

Image vers tracé trace les contours d'une image pour créer des chemins 2D. Ces chemins peuvent ensuite être extrudés, révolutionnés ou utilisés avec n'importe quelle autre opération de chemin. C'est la solution idéale pour convertir des logos, des silhouettes et des graphiques simples en objets 3D.

![20260324 075521 paste 20260324 075521](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-075521-paste-20260324-075521.jpg)


## Utilisation

1. Sélectionnez un objet image dans votre espace de travail
2. Appliquez **Image vers tracé** depuis le menu des opérations d'image
3. Choisissez le type d'analyse et ajustez la plage de sélection

## Paramètres

- **Type d'analyse** - Méthode d'analyse de l'image pour le tracé :
  - **Transparence** - Trace en fonction des zones transparentes et opaques (idéal pour les PNG à fond transparent)
  - **Couleurs** - Trace en fonction des régions de couleur
  - **Intensité** - Trace en fonction des niveaux de luminosité (idéal pour la plupart des images)
- **Sélectionner une plage** - Un contrôle en histogramme permettant de choisir les valeurs de luminosité/couleur à inclure dans le tracé
- **Surface min.** - Surface minimale requise pour qu'une boucle de chemin soit incluse. Augmentez cette valeur pour filtrer les petits artefacts de bruit

## Astuces

- Les images nettes et très contrastées, aux formes simples, donnent les meilleurs résultats
- Utilisez le mode Transparence pour les images PNG à fond transparent
- Utilisez le mode Intensité pour les photographies et les images sans transparence
- Après le tracé, appliquez [Extrusion linéaire](../path/linear-extrude.md) pour donner de la hauteur au chemin
- Augmentez la valeur de Surface min. pour supprimer du tracé les petits détails indésirables

## Voir aussi

- [Convertisseur d'images](image-converter.md) - Créer un relief à partir d'une carte de hauteur plutôt que des chemins plats
- [Lithophanie](lithophane.md) - Créer des images rétroéclairées
- [Objet SVG](../../primitives/svg-object.md) - Importer directement des graphiques vectoriels (aucun tracé nécessaire)
- [Extrusion linéaire](../path/linear-extrude.md) - Donner de la hauteur au chemin tracé
