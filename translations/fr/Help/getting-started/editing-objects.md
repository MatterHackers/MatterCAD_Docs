---
title: Modifier les objets
parent: "Getting Started"
nav_order: 3
source_hash: 5190f3e59be7ea02497903b15c1956ed68b4d270
source_lang: en
---
# Modifier les objets

MatterCAD propose des commandes intuitives intégrées directement à la vue 3D pour déplacer, faire pivoter et mettre à l'échelle vos objets. Vous pouvez aussi modifier les paramètres d'un objet dans le panneau Propriétés.

## Déplacer les pièces


- **Glisser sur le plateau** - Cliquer-glisser n'importe quel objet pour le faire glisser sur la surface de l'espace de travail
- **Déplacer vers le haut et vers le bas** - Utilisez la flèche verticale située en haut d'un objet sélectionné pour ajuster sa hauteur (position Z)
- Pour un positionnement précis, utilisez l'opération [Déplacer](../operations/transform/translate.md) ou saisissez des valeurs exactes dans le panneau Propriétés

## Faire pivoter les pièces

![20260324 080843 paste 20260324 080843](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080843-paste-20260324-080843.jpg)

Cliquez sur l'une des **poignées de rotation d'angle** qui apparaissent lorsque vous sélectionnez un objet. Elles permettent de faire pivoter l'objet dans le plan de la poignée concernée.

- Passez la souris sur l'un des indicateurs d'angle pour aligner la rotation par **incréments de 45 degrés**
- Pour une rotation précise, utilisez l'opération [Pivoter](../operations/transform/rotate.md) et saisissez un angle exact

## Mettre les pièces à l'échelle

![20260324 080819 paste 20260324 080819](https://matterhackers.github.io/MatterCAD_Docs/assets/20260324-080819-paste-20260324-080819.jpg)


Cliquez sur l'une des **poignées de mise à l'échelle d'angle** pour redimensionner votre pièce dans l'espace de travail.

- Faites glisser un coin pour mettre à l'échelle proportionnellement
- Pour un dimensionnement précis ou une mise à l'échelle non uniforme, utilisez l'opération [Échelle](../operations/transform/scale.md), qui permet de définir des dimensions exactes ou de mettre chaque axe à l'échelle indépendamment

## Modifier les paramètres

Lorsque vous sélectionnez un objet, ses paramètres apparaissent dans le panneau Propriétés, à droite de l'écran. Par exemple :

- Un **Cube** affiche les paramètres Largeur, Profondeur, Hauteur ainsi que des commandes d'arrondi optionnelles
- Un **Cylindre** affiche les paramètres Diamètre, Hauteur et Côtés
- Un objet **Texte** affiche le contenu du texte, la police, la taille et la hauteur

Vous pouvez saisir les valeurs directement, utiliser les curseurs ou entrer des [expressions](../workspace/expressions.md) pour créer des relations paramétriques.

## Menu contextuel

Cliquez avec le bouton droit sur un objet pour accéder à des options supplémentaires, notamment :

- Copier, Couper, Supprimer
- Grouper / Dissocier
- Les opérations disponibles pour l'objet sélectionné
- L'aide correspondant au type d'objet (lorsqu'elle est disponible)

## Astuces

- Maintenez **Maj** enfoncée en cliquant pour sélectionner plusieurs objets, puis déplacez-les ou traitez-les ensemble
- Appuyez sur **Ctrl+Z** pour annuler la modification que vous venez d'effectuer
- Utilisez [Aligner](../operations/placement/align.md) pour positionner précisément plusieurs objets les uns par rapport aux autres
- Appuyez sur **Espace** pour effacer votre sélection

## Voir aussi

- [Navigation dans la vue 3D](viewport-navigation.md) - Comment faire pivoter, faire un panoramique et zoomer dans la vue
- [Sélection](../workspace/selection.md) - Comportement détaillé de la sélection
- [Opérations Transformer](../operations/transform/index.md) - Commandes de transformation précises
- [Raccourcis clavier](../workspace/keyboard-shortcuts.md) - Tous les raccourcis disponibles
