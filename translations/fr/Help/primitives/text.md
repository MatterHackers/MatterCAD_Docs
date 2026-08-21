---
title: Texte
articleKey: TextObject3D_2
parent: "Primitives"
nav_order: 16
source_hash: 526f3190c7b2150243499b5874ac455d74810bb2
source_lang: en
---
# Texte

Créez du texte 3D extrudé avec un contenu, une police, une taille et une hauteur personnalisables. Les objets Texte sont parfaits pour les étiquettes, les panneaux, les plaques nominatives et les lettrages décoratifs.

<!--  Screenshot of a 3D Text object on the workspace showing extruded letters -->
![20260318 184207 paste 20260318 184207](https://matterhackers.github.io/MatterCAD_Docs/assets/20260318-184207-paste-20260318-184207.jpg)


## Utilisation

1. Ajoutez une primitive **Texte** depuis le panneau Primitives
2. Saisissez votre texte dans le champ **Nom** du panneau Propriétés
3. Ajustez la police, la taille et la hauteur d'extrusion selon vos besoins

## Paramètres

- **Nom** - Le contenu textuel à afficher
- **Taille du point** - La taille de la police. Elle est exacte par rapport aux tailles d'impression standard : une taille de 12 points dans MatterCAD correspond à un corps de 12 points sur une imprimante 2D
- **Hauteur** - La hauteur d'extrusion (de combien le texte dépasse de la surface)
- **Police** - Sélectionnez parmi les polices système disponibles

## Astuces

- Utilisez [Soustraire](../operations/boolean/subtract.md) pour graver le texte dans une surface au lieu de le mettre en relief
- Pour un texte très petit, augmentez la Taille du point puis réduisez l'[Échelle](../operations/transform/scale.md) de l'objet entier pour obtenir de meilleurs détails
- Chaque lettre du texte est un tracé distinct qui est extrudé avec les autres

## Voir aussi

- [Braille](braille.md) - Générer du texte en Braille imprimable en 3D
- [Code QR](qr-code.md) - Générer un code QR sous forme d'objet 3D
- [Objet Image](image-object.md) - Convertir des images en 3D
