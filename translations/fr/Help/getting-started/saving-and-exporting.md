---
title: Enregistrement et exportation
parent: "Getting Started"
nav_order: 4
source_hash: 020d4bf43f07d3ab7dbd7d585e13c99309f0c0b8
source_lang: en
---
# Enregistrement et exportation

MatterCAD prend en charge plusieurs formats de fichier pour enregistrer et exporter vos conceptions. Le format à choisir dépend de l'usage que vous comptez faire du fichier.

## Formats d'enregistrement

### MCX (format natif)

MCX est le format de fichier natif de MatterCAD et le meilleur choix pour les conceptions que vous souhaitez continuer à modifier ultérieurement. Il conserve :

- L'arborescence de conception complète avec tous les objets et leur hiérarchie
- Tous les paramètres et réglages de chaque objet
- Les opérations booléennes, les réseaux et les autres opérations sous forme modifiable
- Les relations entre composants

**Utilisez le format MCX lorsque :** vous souhaitez enregistrer votre travail et continuer à le modifier plus tard.

### STL

STL est le format le plus répandu pour l'impression 3D. Il ne contient que la géométrie finale du maillage triangulaire, sans historique de conception ni paramètres.

**Utilisez le format STL lorsque :** vous souhaitez imprimer votre conception en 3D ou la partager avec une personne qui n'utilise pas MatterCAD.

### OBJ

OBJ (Wavefront) est un format 3D courant pris en charge par la plupart des logiciels 3D. Comme le format STL, il ne contient que la géométrie du maillage.

**Utilisez le format OBJ lorsque :** vous devez ouvrir votre conception dans un autre logiciel 3D comme Blender ou un moteur de jeu.

### SVG

L'exportation SVG crée un fichier vectoriel 2D à partir de la vue de dessus de votre conception. C'est utile pour la découpe laser ou le fraisage CNC.

**Utilisez le format SVG lorsque :** vous avez besoin d'un contour 2D de votre conception pour la découpe ou la gravure laser.

## Comment enregistrer

![20260324 080726 paste 20260324 080726](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080726-paste-20260324-080726.jpg)

1. Ouvrez le **menu de la marque** (le logo MatterCAD dans le coin supérieur gauche)
2. Sélectionnez **Enregistrer sous** pour choisir un emplacement et un format
3. Sélectionnez le format de fichier dans la liste déroulante des formats
4. Choisissez l'emplacement d'enregistrement du fichier et cliquez sur **Enregistrer**

Votre conception est également enregistrée automatiquement pendant que vous travaillez : vous ne perdrez donc pas vos modifications si vous fermez l'application.

## Conseils

- Enregistrez toujours une copie MCX de votre conception avant de l'exporter en STL ou en OBJ, afin de pouvoir y apporter des modifications plus tard
- Lors de l'exportation en STL, tous les objets de la scène sont fusionnés en un seul maillage
- Si vous devez partager une conception avec une personne qui utilise MatterCAD, envoyez-lui le fichier MCX pour préserver toutes les possibilités de modification
- Vous pouvez aussi enregistrer vos conceptions dans votre [Bibliothèque cloud](../library/cloud-library.md) pour y accéder depuis n'importe quel ordinateur

## Voir aussi

- [Ajouter des objets existants](adding-existing-objects.md) - Importer des fichiers dans MatterCAD
- [Bibliothèque](../library/index.md) - Organiser vos conceptions enregistrées
- [Bibliothèque cloud](../library/cloud-library.md) - Stocker vos conceptions dans le cloud
