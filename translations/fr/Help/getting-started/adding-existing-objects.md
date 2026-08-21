---
title: Ajouter des objets existants
parent: "Getting Started"
nav_order: 1
source_hash: e384a5c024336c3c58343d262d914fa40e0b0426
source_lang: en
---
# Ajouter des objets existants

Vous pouvez importer des modèles 3D existants dans MatterCAD en important des fichiers depuis votre ordinateur ou en ajoutant du contenu depuis la bibliothèque intégrée.

## Depuis votre ordinateur

![20260324 081143 paste 20260324 081143](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081143-paste-20260324-081143.jpg)

![20260324 081240 paste 20260324 081240](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081240-paste-20260324-081240.jpg)


Cliquez sur le bouton **Ouvrir** de la barre d'outils pour parcourir et ajouter des fichiers depuis votre ordinateur. MatterCAD prend en charge les formats d'importation suivants :

- **STL** (.stl) - Format de modèle 3D standard de l'industrie, largement utilisé pour l'impression 3D
- **AMF** (.amf) - Format avancé prenant en charge les couleurs et les objets multi-matériaux
- **OBJ** (.obj) - Format graphique 3D Wavefront (géométrie de maillage uniquement)
- **3MF** (.3mf) - 3D Manufacturing Format avec une prise en charge riche des métadonnées
- **MCX** (.mcx) - Format natif de MatterCAD, qui conserve toutes les données de conception et les paramètres
- **SVG** (.svg) - Scalable Vector Graphics, importé sous forme de tracés 2D
- **TTF / OTF** (.ttf, .otf) - Fichiers de police à utiliser avec l'outil Texte

## Glisser-déposer

Vous pouvez aussi glisser-déposer des fichiers directement depuis votre bureau ou votre explorateur de fichiers dans l'espace de travail MatterCAD. Les types de fichiers pris en charge seront importés automatiquement.

![20260324 081416 paste 20260324 081416](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081416-paste-20260324-081416.jpg)

## Depuis la Bibliothèque

### La Barre latérale Bibliothèque

Cliquez sur le bouton **Ajouter du contenu** de la barre d'outils pour ouvrir le panneau de navigation de la bibliothèque. Depuis cet emplacement, vous pouvez :

- Parcourir vos conceptions enregistrées
- Accéder à la bibliothèque Primitives pour les formes intégrées
- Accéder à votre Bibliothèque cloud si vous êtes connecté
- Glisser-déposer n'importe quel élément de la bibliothèque directement dans votre espace de travail

![20260324 081446 paste 20260324 081446](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081446-paste-20260324-081446.jpg)

### L'onglet Bibliothèque

Vous pouvez aussi utiliser l'onglet Bibliothèque pour parcourir vos collections. Faites un clic droit sur n'importe quel objet de la bibliothèque et sélectionnez **Ajouter à la scène** pour l'importer dans votre espace de travail de conception actuel.

![20260324 081536 paste 20260324 081536](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-081536-paste-20260324-081536.jpg)

## Astuces

- MCX est le meilleur format pour modifier à nouveau vos conceptions par la suite, car il conserve tous les paramètres ainsi que l'arborescence de conception
- Les fichiers STL ne contiennent que la géométrie de maillage. Si vous importez un STL, vous pouvez toujours lui appliquer des opérations, mais vous ne pouvez pas modifier les paramètres d'origine
- Lors de l'importation de plusieurs fichiers, chacun devient un objet distinct dans votre scène. Utilisez [Grouper](../workspace/grouping.md) pour les organiser

## Voir aussi

- [Créer de nouveaux objets](creating-new-objects.md) - Démarrer une conception à partir de zéro avec des primitives
- [Enregistrement et exportation](saving-and-exporting.md) - Enregistrer et exporter vos conceptions terminées
- [Bibliothèque](../library/index.md) - En savoir plus sur l'organisation de votre bibliothèque de conceptions
